# Rendimiento académico y hábitos

Análisis del conjunto Student Performance para explorar la relación entre hábitos y resultados escolares.

## Datos

Los archivos originales se descargaron de [Kaggle: Student Performance Data Set by UCI](https://www.kaggle.com/datasets/dskagglemt/student-performance-data-set). `student-mat.csv` corresponde a Matemáticas y `student-por.csv` a Portugués; `student.txt` documenta las variables. La fuente indica que 382 estudiantes aparecen en ambos archivos, por lo que la suma de filas no representa estudiantes únicos.

Fuente original: [UCI Machine Learning Repository, Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance). Cortez y Silva (2008), *Using Data Mining to Predict Secondary School Student Performance*.

## Ejecución

Con Python 3.10 a 3.13, crear un entorno virtual e instalar las dependencias con `python -m pip install -r requirements.txt`. Ejecutar `python analisis.py` para generar los resúmenes, gráficos y tablas preparadas por asignatura en `resultados/`. Ejecutar `python -m unittest discover -s tests -v` para comprobar las salidas principales.

Para generar los perfiles automáticos exigidos por el laboratorio, ejecutar `python analisis.py --perfilado`. Se genera un archivo HTML por asignatura dentro de `resultados/`.

Las tablas conservan las variables originales y añaden `studytime_hours`, una etiqueta legible del tiempo de estudio. No se imputan valores ni se eliminan filas sin evidencia; si se usan ambas versiones del tiempo de estudio para modelar, debe elegirse una para evitar duplicar la misma información. Las notas de períodos anteriores (`G1`, `G2`) deben usarse como predictores únicamente si están disponibles en el momento de la predicción.
