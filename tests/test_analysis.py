import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


class AnalysisTest(unittest.TestCase):
    def test_public_analysis_outputs(self):
        with tempfile.TemporaryDirectory() as temp:
            run = subprocess.run(
                [sys.executable, str(ROOT / 'analisis.py'), '--output', temp],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            output = Path(temp)
            report = json.loads((output / 'resumen.json').read_text(encoding='utf-8'))
            for subject, count in [('matematicas', 395), ('portugues', 649)]:
                self.assertEqual(report[subject]['filas'], count)
                self.assertEqual(report[subject]['nulos'], 0)
                self.assertEqual(report[subject]['duplicados'], 0)
                table = pd.read_csv(output / f'tabla_minable_{subject}.csv')
                self.assertEqual(len(table), count)
                self.assertEqual(table.isna().sum().sum(), 0)
                self.assertIn('G3', table)
                self.assertEqual(set(table.studytime_hours), {'<2', '2-5', '5-10', '>10'})
                self.assertTrue((output / f'habitos_{subject}.png').is_file())


if __name__ == '__main__':
    unittest.main()
