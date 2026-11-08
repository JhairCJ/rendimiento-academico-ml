# Rendimiento académico y hábitos

Análisis del conjunto Student Performance para explorar la relación entre hábitos y resultados escolares.

## Datos

Los archivos originales se descargaron de [Kaggle: Student Performance Data Set by UCI](https://www.kaggle.com/datasets/dskagglemt/student-performance-data-set). `student-mat.csv` corresponde a Matemáticas y `student-por.csv` a Portugués; `student.txt` documenta las variables. La fuente indica que 382 estudiantes aparecen en ambos archivos, por lo que la suma de filas no representa estudiantes únicos.

Fuente original: [UCI Machine Learning Repository, Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance). Cortez y Silva (2008), *Using Data Mining to Predict Secondary School Student Performance*.

## Notebooks

El análisis está dividido en cuatro cuadernos, con código, tablas, gráficos e interpretaciones:

1. `notebooks/01_comprension_datos.ipynb`: fuentes, variables y revisión inicial.
2. `notebooks/02_analisis_univariado.ipynb`: distribuciones y estadísticas.
3. `notebooks/03_bivariado_perfilado.ipynb`: comparaciones con la nota final y perfilado automático.
4. `notebooks/04_preparacion_tabla_minable.ipynb`: limpieza, valores extremos y exportación.

Con Python 3.10 a 3.13, crea y activa un entorno virtual. Desde la carpeta del proyecto, instala las dependencias con `python -m pip install -r requirements.txt`, inicia Jupyter con `jupyter lab` y ejecuta los cuatro notebooks en orden con **Ejecutar todas las celdas**. Selecciona el kernel de ese mismo entorno.

Los archivos se guardan en `resultados/`, incluidos gráficos, dos perfiles HTML y dos tablas minables en CSV. La prueba `python -m unittest discover -s tests -v` ejecuta los cuadernos con una copia temporal de los datos y comprueba sus resultados. El script `analisis.py` se conserva para quien necesite ejecutar el flujo anterior desde la terminal.

Las tablas conservan las variables originales y añaden `studytime_hours`, una etiqueta legible del tiempo de estudio. No se imputan valores ni se eliminan filas sin evidencia; si se usan ambas versiones del tiempo de estudio para modelar, debe elegirse una para evitar duplicar la misma información. Las notas de períodos anteriores (`G1`, `G2`) deben usarse como predictores únicamente si están disponibles en el momento de la predicción.
