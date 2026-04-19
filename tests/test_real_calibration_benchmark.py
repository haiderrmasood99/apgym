from __future__ import annotations

from pathlib import Path
import tempfile
from unittest import TestCase

from apgym.simulator import find_models_exe
from apgym.validation import TutorialCalibrationConfig, run_tutorial_calibration


class TestRealCalibrationBenchmark(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.models_exe = find_models_exe()
        except FileNotFoundError:
            cls.models_exe = None

    def test_tutorial_calibration_run(self) -> None:
        if self.models_exe is None:
            self.skipTest("APSIM Models.exe not available on this machine")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = TutorialCalibrationConfig(
                output_dir=root / "out",
                work_dir=root / "work",
            )
            result = run_tutorial_calibration(config)
            self.assertTrue(result["passes_thresholds"])
            self.assertIn("markdown", result["outputs"])
            self.assertTrue(Path(result["outputs"]["markdown"]).exists())
            self.assertTrue(Path(result["outputs"]["json"]).exists())
            self.assertTrue(Path(result["outputs"]["aligned_csv"]).exists())

