# Rendimiento escolar: hábitos y resultados académicos

## 1. Antecedentes, problema y objetivos

El rendimiento escolar puede relacionarse con aspectos muy distintos de la vida de un estudiante. En esta práctica nos interesa explorar algunas de esas relaciones, en especial el tiempo de estudio, las salidas con amigos, el consumo de alcohol y las ausencias. También consideramos los fracasos académicos anteriores como parte del contexto escolar.

Para ello elegimos el conjunto Student Performance, publicado en Kaggle y procedente del repositorio de la Universidad de California en Irvine (UCI). Reúne información de dos centros de educación secundaria de Portugal, obtenida mediante registros escolares y cuestionarios. Incluye dos archivos: Matemáticas y Portugués. Los datos son históricos y describen a esos centros; no representan necesariamente a otros países, colegios o períodos.

El objetivo es describir los datos, explorar la relación entre hábitos y nota final y preparar una tabla útil para cada asignatura. Buscamos comparar grupos y detectar patrones que merezcan atención, sin presentar esas diferencias como causas del rendimiento.

## 2. Hipótesis y enfoque

Planteamos como hipótesis inicial que los estudiantes que dedican más tiempo a estudiar tienden a obtener mejores notas, mientras que las ausencias, las salidas frecuentes y el consumo de alcohol podrían relacionarse con notas menores. También esperamos encontrar diferencias según el número de materias reprobadas anteriormente. Estas ideas se contrastan con comparaciones descriptivas, no con un experimento.

La variable principal de resultado es G3, la nota final de la asignatura, en una escala de 0 a 20. G1 y G2 son notas de períodos anteriores. Si se quisiera predecir G3, el problema podría abordarse como una regresión; antes habría que definir en qué momento se haría la predicción, pues no tendría sentido usar G1 o G2 si todavía no están disponibles.

## 3. Metodología CRISP-DM

### 3.1 Comprensión del problema

Desde la perspectiva educativa, el proyecto busca comprender mejor qué patrones aparecen en los datos y entregar bases preparadas para continuar el análisis. Consideramos terminado el trabajo cuando se hayan revisado las fuentes, sus variables y su calidad, se hayan interpretado las comparaciones principales y se hayan generado tablas reproducibles.

El alcance es académico. Los datos son públicos y las herramientas utilizadas son Python y sus bibliotecas de análisis. No se cuenta con un presupuesto de intervención ni con información suficiente para calcular beneficios económicos, por lo que no corresponde afirmar una rentabilidad. El acceso depende de la disponibilidad de la fuente y de un entorno de ejecución compatible.

Entre los riesgos están interpretar una asociación como causa, extraer conclusiones de grupos pequeños y contar dos veces a estudiantes presentes en ambas asignaturas. Para reducirlos analizamos los archivos por separado, mostramos el tamaño de cada grupo y explicamos las limitaciones de los resultados.

CRISP-DM comprende la comprensión del problema y de los datos, la preparación, el modelado, la evaluación y el despliegue. En esta práctica desarrollamos las tres primeras fases para el caso elegido. Un eventual modelo necesitaría una división entre entrenamiento y prueba, un criterio de evaluación y una revisión de su uso y sus riesgos; no se ha entrenado ni implementado un modelo para este conjunto.

### 3.2 Comprensión y exploración de los datos

El archivo de Matemáticas contiene 395 filas y el de Portugués 649; cada uno tiene 33 columnas. Cada fila describe un registro de estudiante en una asignatura. La documentación original indica que 382 estudiantes aparecen en ambos archivos. Por eso 1.044 es el número de registros sumados, no el número de personas diferentes. No fusionamos los archivos ni suponemos que sus filas son independientes entre asignaturas.

Las variables incluyen datos personales y familiares, hábitos, apoyos educativos, ausencias y notas. Entre las más útiles para nuestra pregunta están studytime (tiempo de estudio semanal), goout (salidas con amigos), Dalc y Walc (consumo de alcohol entre semana y en fin de semana), absences (ausencias), failures (materias reprobadas antes) y G3 (nota final). Las categorías de estudio representan intervalos de horas; las escalas de salidas y consumo van de 1 a 5 y son ordinales.

En la revisión inicial no encontramos valores nulos ni filas completamente duplicadas en ninguno de los dos archivos. Una fila igual a otra no demostraría por sí sola que se trata de la misma persona, pero en esta revisión no hubo casos que resolver. Consultamos las definiciones disponibles y conservamos las variables con sus escalas originales. No contamos con información externa para verificar la precisión de cada respuesta del cuestionario.

La tabla resume los resultados generales de cada asignatura.

**Tabla 1. Datos y notas finales por asignatura**

| Indicador | Matemáticas | Portugués |
|---|---:|---:|
| Registros | 395 | 649 |
| Variables originales | 33 | 33 |
| Nota media | 10,42 | 11,91 |
| Mediana | 11 | 12 |
| Notas de cero | 38 | 15 |

Las notas de cero están dentro de la escala. Por eso las conservamos y no asumimos que sean errores. Las estadísticas detalladas acompañan al código.

### 3.3 Hábitos y nota final

La tabla compara la nota final media según el tiempo de estudio semanal. El tamaño de cada grupo se indica junto al promedio.

**Tabla 2. Tiempo de estudio y nota final**

| Estudio por semana | Matemáticas: media (n) | Portugués: media (n) |
|---|---:|---:|
| Menos de 2 horas | 10,05 (105) | 10,84 (212) |
| De 2 a 5 horas | 10,17 (198) | 12,09 (305) |
| De 5 a 10 horas | 11,40 (65) | 13,23 (97) |
| Más de 10 horas | 11,26 (27) | 13,06 (35) |

En general, los grupos que declaran más tiempo de estudio presentan promedios más altos. El aumento no es uniforme y los grupos de más de 10 horas son pequeños, así que conviene interpretar sus resultados con cuidado.

La correlación de Spearman resume la relación ordenada entre cada variable y la nota final. Los valores positivos indican que ambas tienden a aumentar juntas; los negativos, que una tiende a disminuir cuando aumenta la otra.

**Tabla 3. Relación de los hábitos y antecedentes con la nota final**

| Variable comparada con G3 | Matemáticas | Portugués |
|---|---:|---:|
| Tiempo de estudio | 0,105 | 0,275 |
| Salidas con amigos | −0,166 | −0,105 |
| Consumo entre semana | −0,121 | −0,208 |
| Fracasos anteriores | −0,361 | −0,448 |
| Ausencias | 0,018 | −0,159 |

Estas asociaciones son descriptivas: no demuestran que un hábito sea la causa de una nota.

Los fracasos anteriores presentan la relación negativa más marcada en ambos cursos. Entre quienes no registraban fracasos, la nota media fue 11,25 en Matemáticas y 12,51 en Portugués; entre quienes registraban uno, fue 8,12 y 8,64, respectivamente. Pueden intervenir otras condiciones que no medimos.

La relación con las ausencias es distinta en cada asignatura. Las comparaciones por categoría, con el tamaño de cada grupo, están disponibles en los archivos de resultados.

### 3.4 Perfilado y calidad

Además de la revisión con pandas, generamos un perfil automático con ydata_profiling para cada asignatura. Ambos perfiles confirman 33 variables y ninguna celda vacía; clasifican 17 variables como texto y 16 como numéricas. Algunas variables numéricas representan categorías ordenadas, por lo que su interpretación debe seguir el diccionario original.

El perfil automático destacó la frecuencia de algunos valores cero:

**Tabla 4. Valores cero señalados por el perfilado**

| Variable con valor cero | Matemáticas | Portugués |
|---|---:|---:|
| Fracasos anteriores | 312 | 549 |
| Ausencias | 115 | 244 |
| Nota final | 38 | 15 |

En fracasos y ausencias, cero indica que no se registraron esos eventos; en la nota final es un valor posible. Las alertas sirven para revisar las variables, pero no justifican eliminar esos registros. Los perfiles HTML completos están en la carpeta de resultados.

### 3.5 Preparación de los datos

Leímos los CSV con el separador indicado por los archivos y conservamos los dos conjuntos por separado. No fue necesaria una unión: hacerlo sin identificar correctamente a los estudiantes compartidos complicaría la interpretación. Los tipos numéricos y categóricos se revisaron según el diccionario; no hay fechas que convertir en estas fuentes.

No imputamos valores, ya que no se encontraron nulos, ni eliminamos filas por estar incompletas o duplicadas. Tampoco descartamos notas de cero ni registros extremos de ausencias solo por ser poco frecuentes: una cifra extrema no demuestra por sí sola que sea incorrecta. Las agrupaciones por tiempo de estudio, consumo, salidas, ausencias y fracasos anteriores permiten comparar cantidad de registros, media y mediana de G3.

Para facilitar la lectura añadimos studytime_hours, que traduce el código de tiempo de estudio a su intervalo en horas. La columna original se conserva. Si se entrena un modelo, convendría seleccionar una de las dos representaciones para no duplicar la misma información. Las tablas finales se exportaron en CSV, una por asignatura, con 395 y 649 filas y 34 columnas. Mantienen la variable objetivo G3 y los atributos originales; la selección definitiva de predictores dependerá del objetivo y del momento de uso del modelo.

Las fuentes se pueden leer y reproducir con los archivos disponibles. Como no hubo una fusión ni valores faltantes, esas operaciones no requirieron tratamiento adicional. Para un modelo posterior habría que codificar las categorías dentro de un proceso ajustado con los datos de entrenamiento y comprobar que ningún predictor aporte información que no estaría disponible al predecir.

## 4. Conclusiones y limitaciones

Encontramos que los grupos con más tiempo de estudio suelen presentar notas medias más altas, especialmente en Portugués, aunque el último grupo no mantiene un aumento continuo y tiene pocos registros. Los fracasos anteriores muestran una asociación negativa más clara con la nota final en ambas asignaturas. Las ausencias, las salidas y el consumo presentan relaciones que varían en intensidad según el curso.

Estos resultados ayudan a formular preguntas, no a identificar causas ni a juzgar estudiantes. Los datos proceden de dos centros y de un contexto histórico concreto; además, algunas respuestas son declaradas por los propios estudiantes y hay personas presentes en ambos archivos. Un uso responsable requeriría considerar el contexto educativo y evitar decisiones individuales basadas solo en estas variables.

## 5. Fuentes

Cortez, P. y Silva, A. (2008). Using Data Mining to Predict Secondary School Student Performance.
UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/320/student+performance
Kaggle: https://www.kaggle.com/datasets/dskagglemt/student-performance-data-set
Archivos originales y código de análisis del proyecto.
