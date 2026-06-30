import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "Monitoring and Auditing Data Access (Big Data)" / "Anomaly_detection.py"


class AnomalyDetectionPathTests(unittest.TestCase):
    def test_script_runs_from_outside_project_directory(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            result = subprocess.run(
                [sys.executable, str(SCRIPT)],
                cwd=tmp_dir,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr or result.stdout)
            self.assertIn("Total alerts generated:", result.stdout)

            output_log = SCRIPT.parent / "alerts.log"
            self.assertTrue(output_log.exists())
            output_log.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
