"""APSIM run orchestration for APGym environments."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
import shutil
import subprocess
import tempfile
import uuid
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from apgym.simulator.apsim_apply import PatchLike, apply_patches
from apgym.simulator.apsim_locator import find_models_exe
from apgym.simulator.datastore import DataStoreReader


@dataclass
class ApsimRunRequest:
    template_path: Path
    patches: list[PatchLike] = field(default_factory=list)
    report_tables: list[str] = field(default_factory=lambda: ["Report", "SeasonSummary"])
    export_csv: bool = False
    timeout_sec: int = 300
    run_name: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ApsimRunResult:
    run_id: str
    run_dir: Path
    apsimx_path: Path
    datastore_path: Path | None
    reports: dict[str, pd.DataFrame]
    stdout: str
    stderr: str
    returncode: int
    command: list[str]
    is_dry_run: bool = False

    @property
    def ok(self) -> bool:
        return self.returncode == 0


class ApsimRunner:
    """Execute APSIM template runs and load report outputs."""

    def __init__(
        self,
        models_exe: str | Path | None = None,
        work_root: str | Path | None = None,
        keep_runs: bool = True,
        dry_run: bool = False,
    ):
        self.models_exe = None if dry_run else find_models_exe(models_exe)
        self.keep_runs = keep_runs
        self.dry_run = dry_run
        if work_root is None:
            self.work_root = Path(tempfile.gettempdir()) / "apgym_runs"
        else:
            self.work_root = Path(work_root).expanduser().resolve()
        self.work_root.mkdir(parents=True, exist_ok=True)

    def _create_run_dir(self, run_name: str | None) -> tuple[str, Path]:
        run_id = run_name or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "_" + uuid.uuid4().hex[:8]
        run_dir = self.work_root / run_id
        run_dir.mkdir(parents=True, exist_ok=False)
        return run_id, run_dir

    @staticmethod
    def _resolve_datastore(apsimx_path: Path) -> Path:
        return apsimx_path.with_suffix(".db")

    def _load_reports(
        self, datastore_path: Path, report_tables: list[str]
    ) -> dict[str, pd.DataFrame]:
        if not datastore_path.exists():
            return {}
        reader = DataStoreReader(datastore_path)
        reports: dict[str, pd.DataFrame] = {}
        for table in report_tables:
            if reader.table_exists(table):
                reports[table] = reader.read_table(table)
        return reports

    def _dry_run_result(
        self,
        request: ApsimRunRequest,
        run_id: str,
        run_dir: Path,
        apsimx_path: Path,
    ) -> ApsimRunResult:
        total_n = float(request.metadata.get("total_n_applied", 0.0))
        season_days = int(request.metadata.get("season_days", 180))
        start_date = datetime.fromisoformat(
            str(request.metadata.get("season_start", "2020-04-15"))
        )

        # Smooth response curve: yield improves then plateaus with excess-N penalty.
        yield_t_ha = max(0.0, 2.5 + 0.05 * total_n - 0.00012 * (total_n**2))
        leaching_kg_ha = max(0.0, 0.015 * max(total_n - 120.0, 0.0) ** 1.2)

        dates = [start_date + timedelta(days=i) for i in range(season_days + 1)]
        progress = np.linspace(0.0, 1.0, num=len(dates))
        report = pd.DataFrame(
            {
                "Date": [d.date().isoformat() for d in dates],
                "DayOfYear": [d.timetuple().tm_yday for d in dates],
                "Rain": 2.0 + 6.0 * np.sin(progress * np.pi),
                "SoilWaterTop": 70.0 + 10.0 * np.sin(progress * 4.0),
                "SoilN": np.clip(total_n * (1.0 - progress) + 20.0, 0.0, None),
                "LAI": np.clip(np.sin(progress * np.pi) * 5.0, 0.0, None),
                "Biomass": np.clip(progress * 15000.0, 0.0, None),
                "StageCode": np.floor(progress * 7).astype(int),
            }
        )
        season_summary = pd.DataFrame(
            [
                {
                    "Yield_t_ha": yield_t_ha,
                    "TotalNApplied_kg_ha": total_n,
                    "Leaching_kg_ha": leaching_kg_ha,
                    "SeasonET_mm": 500 + 0.2 * total_n,
                }
            ]
        )
        reports = {
            "Report": report,
            "SeasonSummary": season_summary,
        }
        selected_reports = {
            name: table for name, table in reports.items() if name in request.report_tables
        }
        return ApsimRunResult(
            run_id=run_id,
            run_dir=run_dir,
            apsimx_path=apsimx_path,
            datastore_path=None,
            reports=selected_reports,
            stdout="dry-run",
            stderr="",
            returncode=0,
            command=["dry-run"],
            is_dry_run=True,
        )

    def run(self, request: ApsimRunRequest) -> ApsimRunResult:
        template_path = Path(request.template_path).expanduser().resolve()
        if not template_path.exists():
            raise FileNotFoundError(f"APSIM template not found: {template_path}")

        run_id, run_dir = self._create_run_dir(request.run_name)
        run_template = run_dir / template_path.name
        shutil.copy2(template_path, run_template)

        if request.patches:
            apply_patches(run_template, request.patches, output_path=run_template)

        if self.dry_run:
            return self._dry_run_result(request, run_id, run_dir, run_template)

        command = [str(self.models_exe), str(run_template)]
        if request.export_csv:
            command.append("--csv")

        process = subprocess.run(
            command,
            cwd=run_dir,
            capture_output=True,
            text=True,
            timeout=request.timeout_sec,
        )

        datastore_path = self._resolve_datastore(run_template)
        reports = self._load_reports(datastore_path, request.report_tables)

        result = ApsimRunResult(
            run_id=run_id,
            run_dir=run_dir,
            apsimx_path=run_template,
            datastore_path=datastore_path if datastore_path.exists() else None,
            reports=reports,
            stdout=process.stdout,
            stderr=process.stderr,
            returncode=process.returncode,
            command=command,
            is_dry_run=False,
        )

        if not self.keep_runs and result.ok:
            shutil.rmtree(run_dir, ignore_errors=True)
        return result
