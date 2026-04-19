from __future__ import annotations

from pathlib import Path
import unittest

from apgym.simulator import (
    ApsimManagerParameterPatch,
    ApsimModelPropertyPatch,
    ApsimRunRequest,
    ApsimRunner,
    find_models_exe,
)


class TestRealApsimSmoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.models_exe = find_models_exe()
        except FileNotFoundError:
            cls.models_exe = None
        cls.template = (
            Path(__file__).resolve().parents[1] / "templates" / "maize_n_real.apsimx"
        )

    def test_real_apsim_response_to_topdress_schedule(self) -> None:
        if self.models_exe is None:
            self.skipTest("APSIM Models.exe not available on this machine")
        if not self.template.exists():
            self.skipTest("maize_n_real.apsimx template not found")

        runner = ApsimRunner(models_exe=self.models_exe, dry_run=False, keep_runs=False)

        def run_yield(schedule_csv: str) -> float:
            patches = [
                ApsimModelPropertyPatch(
                    model_name="Clock",
                    property_name="Start",
                    value="1990-01-01T00:00:00",
                    type_contains="Models.Clock",
                    simulation_name="Simulation",
                ),
                ApsimModelPropertyPatch(
                    model_name="Clock",
                    property_name="End",
                    value="1991-12-31T00:00:00",
                    type_contains="Models.Clock",
                    simulation_name="Simulation",
                ),
                ApsimManagerParameterPatch(
                    manager_name="Fertilise at sowing",
                    parameter_key="Amount",
                    value=0.0,
                    simulation_name="Simulation",
                    zone_name="Field",
                ),
                ApsimManagerParameterPatch(
                    manager_name="APGym TopDress N",
                    parameter_key="ScheduleCsv",
                    value=schedule_csv,
                    simulation_name="Simulation",
                    zone_name="Field",
                ),
            ]
            result = runner.run(
                ApsimRunRequest(
                    template_path=self.template,
                    patches=patches,
                    report_tables=["Report"],
                    timeout_sec=300,
                )
            )
            self.assertTrue(result.ok, msg=result.stderr)
            report = result.reports["Report"]
            return float(report["Yield"].max())

        low_n_yield = run_yield("")
        high_n_yield = run_yield("1990-06-20:160")
        self.assertGreater(high_n_yield, low_n_yield)


if __name__ == "__main__":
    unittest.main()
