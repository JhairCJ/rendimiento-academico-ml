import shutil
import tempfile
import unittest
from pathlib import Path

import nbformat
import pandas as pd
from nbclient import NotebookClient


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [
    '01_comprension_datos.ipynb',
    '02_analisis_univariado.ipynb',
    '03_bivariado_perfilado.ipynb',
    '04_preparacion_tabla_minable.ipynb',
]


class NotebookIntegrationTest(unittest.TestCase):
    def test_notebooks_execute_and_export_expected_results(self):
        with tempfile.TemporaryDirectory() as temp:
            workdir = Path(temp)
            shutil.copytree(ROOT / 'datos', workdir / 'datos')
            for filename in NOTEBOOKS:
                notebook = nbformat.read(ROOT / 'notebooks' / filename, as_version=4)
                NotebookClient(notebook, timeout=180, kernel_name='python3').execute(cwd=str(workdir))
            for subject, count in [('matematicas', 395), ('portugues', 649)]:
                results = workdir / 'resultados'
                data = pd.read_csv(results / f'tabla_minable_{subject}.csv')
                source_file = 'student-mat.csv' if subject == 'matematicas' else 'student-por.csv'
                original = pd.read_csv(workdir / 'datos' / source_file, sep=';')
                self.assertEqual(len(data), count)
                self.assertEqual(data.isna().sum().sum(), 0)
                self.assertIn('studytime_hours', data)
                pd.testing.assert_frame_equal(data[original.columns], original)
                self.assertEqual(data['studytime_hours'].tolist(),
                                 original['studytime'].map({1: '<2', 2: '2-5', 3: '5-10', 4: '>10'}).tolist())
                self.assertTrue((results / f'perfil_{subject}.html').stat().st_size > 1000)
                self.assertTrue((results / f'habitos_{subject}.png').stat().st_size > 1000)
                summary = pd.read_csv(results / f'{subject}_studytime_y_G3.csv', index_col=0)
                self.assertEqual(summary['count'].sum(), count)
                expected = original.groupby('studytime')['G3'].agg(['count', 'mean', 'median']).round(3)
                pd.testing.assert_frame_equal(summary, expected)
                absences = pd.read_csv(results / f'{subject}_ausencias_agrupadas.csv', index_col=0)
                self.assertEqual(absences['count'].sum(), count)
                self.assertEqual(absences.loc['0', 'count'], original['absences'].eq(0).sum())


if __name__ == '__main__':
    unittest.main()
