"""Explore and prepare the two original Student Performance course datasets."""

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent
SOURCES = {'matematicas': 'student-mat.csv', 'portugues': 'student-por.csv'}
HABITS = ['studytime', 'goout', 'Dalc', 'Walc', 'absences', 'failures']


def chart(frame, path, title):
    """Display the mean final grade and sample size for each study-time group."""
    grouped = frame.groupby('studytime')['G3'].agg(['mean', 'count'])
    labels = {1: '<2 h', 2: '2–5 h', 3: '5–10 h', 4: '>10 h'}
    sns.set_theme(style='whitegrid', palette='deep')
    fig, ax = plt.subplots(figsize=(8, 4.6))
    bars = ax.bar([labels[i] for i in grouped.index], grouped['mean'], color='#327986')
    for bar, (_, values) in zip(bars, grouped.iterrows()):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.25,
                f"{values['mean']:.2f}\nn={int(values['count'])}", ha='center', fontsize=9)
    ax.set(title=title, xlabel='Horas de estudio por semana',
           ylabel='Nota final media (0 a 20)', ylim=(0, 20))
    fig.tight_layout()
    fig.savefig(path, dpi=160, bbox_inches='tight')
    plt.close(fig)


def analyze(subject, source, output, profiling):
    frame = pd.read_csv(ROOT / 'datos' / source, sep=';')
    if set(HABITS + ['G1', 'G2', 'G3']) - set(frame.columns):
        raise ValueError(f'Unexpected columns in {source}')
    output.mkdir(parents=True, exist_ok=True)
    prepared = frame.copy()
    prepared['studytime_hours'] = prepared['studytime'].map({1: '<2', 2: '2-5', 3: '5-10', 4: '>10'})
    if prepared['studytime_hours'].isna().any():
        raise ValueError(f'Unexpected studytime value in {source}')
    prepared.to_csv(output / f'tabla_minable_{subject}.csv', index=False, encoding='utf-8')
    frame.describe(include='all').to_csv(output / f'estadisticas_{subject}.csv', encoding='utf-8')
    frame.isna().sum().rename('nulos').to_csv(output / f'nulos_{subject}.csv', encoding='utf-8')
    for habit in HABITS:
        frame.groupby(habit)['G3'].agg(['count', 'mean', 'median']).round(3).to_csv(
            output / f'{subject}_{habit}_y_G3.csv', encoding='utf-8'
        )
    subject_name = {'matematicas': 'Matemáticas', 'portugues': 'Portugués'}[subject]
    chart(frame, output / f'habitos_{subject}.png', f'Tiempo de estudio y nota final · {subject_name}')
    if profiling:
        from ydata_profiling import ProfileReport
        ProfileReport(frame, title=f'Perfil de datos: {subject}', minimal=True).to_file(
            output / f'perfil_{subject}.html'
        )
    return {
        'filas': len(frame), 'columnas': len(frame.columns),
        'nulos': int(frame.isna().sum().sum()), 'duplicados': int(frame.duplicated().sum()),
        'nota_media': round(float(frame.G3.mean()), 3),
        'nota_mediana': float(frame.G3.median()),
        'notas_cero': int(frame.G3.eq(0).sum()),
        'correlaciones_spearman': frame[HABITS + ['G3']].corr(method='spearman')['G3'].round(4).to_dict(),
        'tiempo_estudio': frame.groupby('studytime')['G3'].agg(['count', 'mean']).round(3).to_dict('index'),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'resultados')
    parser.add_argument('--perfilado', action='store_true', help='Generate ydata-profiling reports')
    args = parser.parse_args()
    summary = {name: analyze(name, path, args.output, args.perfilado) for name, path in SOURCES.items()}
    (args.output / 'resumen.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Results written to {args.output}')


if __name__ == '__main__':
    main()
