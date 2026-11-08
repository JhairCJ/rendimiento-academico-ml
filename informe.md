# Rendimiento escolar: hábitos y resultados académicos

## 1. Antecedentes, problema y objetivos

El rendimiento escolar puede relacionarse con aspectos muy distintos de la vida de un estudiante. En esta práctica nos interesa explorar algunas de esas relaciones, en especial el tiempo de estudio, las salidas con amigos, el consumo de alcohol y las ausencias. También consideramos los fracasos académicos anteriores como parte del contexto escolar.

Para ello elegimos el conjunto Student Performance, publicado en Kaggle y procedente del repositorio de la Universidad de California en Irvine (UCI). Reúne información de dos centros de educación secundaria de Portugal, obtenida mediante registros escolares y cuestionarios. Incluye dos archivos: Matemáticas y Portugués. Los datos son históricos y describen a esos centros; no representan necesariamente a otros países, colegios o períodos.

El objetivo es describir los datos, explorar la relación entre hábitos y nota final y preparar una tabla útil para cada asignatura. Buscamos comparar grupos y detectar patrones que merezcan atención, sin presentar esas diferencias como causas del rendimiento.

### 1.1 Contexto del estudio

Conocer el rendimiento de un estudiante no consiste solamente en mirar su nota. En el proceso intervienen el tiempo disponible para estudiar, la asistencia, el apoyo familiar, las actividades fuera de clase y experiencias escolares anteriores. Algunas de estas condiciones aparecen en la base elegida; otras, como la calidad de la enseñanza o los cambios personales durante el año, no están medidas de forma suficiente.

En este trabajo usamos los registros de dos asignaturas para explorar cómo se distribuyen las notas y cómo cambian sus promedios entre grupos. Elegimos estos datos porque permiten practicar la revisión y preparación de un conjunto real y, al mismo tiempo, plantear preguntas cercanas al ámbito educativo. La base está disponible públicamente, pero su disponibilidad no elimina la responsabilidad de interpretar con cuidado información sobre estudiantes.


### 1.2 Problema y alcance

El problema que abordamos es descriptivo: no sabemos de antemano qué diferencias encontraremos entre los grupos de hábitos presentes en esta base. Queremos identificar patrones que puedan servir para formular preguntas educativas, sin convertir una característica individual en una etiqueta de éxito o fracaso.

El estudio se limita a los archivos de Matemáticas y Portugués y a las variables disponibles en ellos. Cada archivo se trata como una fuente independiente para el análisis de su asignatura. Esto permite comparar resultados sin afirmar que todos los registros pertenecen a personas distintas. Tampoco intentamos representar al conjunto de estudiantes de Bolivia ni estimar resultados actuales de colegios que no participaron en la recolección.

El resultado esperado es un análisis que pueda revisarse y reproducirse: fuentes identificadas, variables explicadas, gráficos y resúmenes interpretados, decisiones de preparación documentadas y dos tablas finales. Una diferencia entre promedios es un punto de partida para entender los datos, no una recomendación automática para intervenir sobre una persona.


### 1.3 Objetivos específicos

Primero, describimos el tamaño de las fuentes, su estructura y las variables que permiten estudiar hábitos y resultados. Después revisamos los valores faltantes, las filas duplicadas y la distribución de las principales medidas.

A continuación comparamos la nota final con el tiempo de estudio, las salidas, el consumo de alcohol, las ausencias y los fracasos anteriores. Por último, conservamos y documentamos las variables útiles en archivos CSV que puedan servir como punto de partida para otras actividades de análisis.


## 2. Hipótesis y enfoque

Planteamos como hipótesis inicial que los estudiantes que dedican más tiempo a estudiar tienden a obtener mejores notas, mientras que las ausencias, las salidas frecuentes y el consumo de alcohol podrían relacionarse con notas menores. También esperamos encontrar diferencias según el número de materias reprobadas anteriormente. Estas ideas se contrastan con comparaciones descriptivas, no con un experimento.

La variable principal de resultado es G3, la nota final de la asignatura, en una escala de 0 a 20. G1 y G2 son notas de períodos anteriores. Si se quisiera predecir G3, el problema podría abordarse como una regresión; antes habría que definir en qué momento se haría la predicción, pues no tendría sentido usar G1 o G2 si todavía no están disponibles.

### 2.1 Hipótesis y forma de revisarlas

Las hipótesis nos ayudan a decidir qué mirar, pero no obligan a que los datos confirmen lo esperado. Para el tiempo de estudio comparamos la media de G3 entre los cuatro intervalos registrados y revisamos cuántos casos hay en cada uno. Para las demás variables observamos sus categorías, promedios y correlaciones con la nota final.

Una relación positiva significa que, en términos generales, valores mayores de una variable tienden a acompañar valores mayores de la otra. Una relación negativa apunta en sentido contrario. En ambos casos puede haber muchas excepciones: el resultado de un grupo no describe necesariamente a cada estudiante.

Esperábamos una relación negativa entre ausencias y nota final, pero el resultado no es igual en ambas asignaturas. Esa diferencia nos obliga a no presentar la hipótesis como una regla general. De forma similar, una correlación pequeña no prueba que una variable no importe; indica que, en esta muestra y con esta medida, no aparece una relación ordenada fuerte.


### 2.2 Variable objetivo y momento de uso

G3 es una nota numérica, por lo que podría utilizarse como resultado en un problema de regresión. También sería posible convertirla en categorías, pero eso exigiría acordar un criterio de corte y perdería parte del detalle de la escala. Para esta práctica conservamos la nota original de 0 a 20.

G1 y G2 ofrecen información de períodos previos de la misma asignatura. Su utilidad depende del momento en que se quiera realizar una predicción: para una estimación al inicio del curso no estarían disponibles de la misma manera que al final del segundo período. En este informe las conservamos como variables del conjunto, sin afirmar que se haya desarrollado o evaluado un modelo predictivo.


## 3. Metodología CRISP-DM

### 3.1 Comprensión del problema

Desde la perspectiva educativa, el proyecto busca comprender mejor qué patrones aparecen en los datos y entregar bases preparadas para continuar el análisis. Consideramos terminado el trabajo cuando se hayan revisado las fuentes, sus variables y su calidad, se hayan interpretado las comparaciones principales y se hayan generado tablas reproducibles.

El alcance es académico. Los datos son públicos y las herramientas utilizadas son Python y sus bibliotecas de análisis. No se cuenta con un presupuesto de intervención ni con información suficiente para calcular beneficios económicos, por lo que no corresponde afirmar una rentabilidad. El acceso depende de la disponibilidad de la fuente y de un entorno de ejecución compatible.

Entre los riesgos están interpretar una asociación como causa, extraer conclusiones de grupos pequeños y contar dos veces a estudiantes presentes en ambas asignaturas. Para reducirlos analizamos los archivos por separado, mostramos el tamaño de cada grupo y explicamos las limitaciones de los resultados.

CRISP-DM comprende la comprensión del problema y de los datos, la preparación, el modelado, la evaluación y el despliegue. En esta práctica desarrollamos las tres primeras fases para el caso elegido. Un eventual modelo necesitaría una división entre entrenamiento y prueba, un criterio de evaluación y una revisión de su uso y sus riesgos; no se ha entrenado ni implementado un modelo para este conjunto.

#### 3.1.1 Objetivo educativo y criterios de éxito

En un contexto educativo, el interés de un análisis como este sería comprender mejor las condiciones que acompañan distintas trayectorias escolares. Un docente podría usar información agregada para plantear preguntas y orientar una conversación con sus estudiantes; los resultados no deberían utilizarse para decidir quién merece apoyo o para clasificar a una persona de forma definitiva.

Para la práctica, el criterio de éxito es más concreto: que otra persona pueda localizar las fuentes, ejecutar el análisis, entender qué se comparó y comprobar las cifras. La tabla final debe conservar la relación entre cada registro y su asignatura, y las conclusiones deben corresponder a lo observado. Un gráfico sin explicación o una limpieza sin criterio no serían suficientes para cumplir ese objetivo.


#### 3.1.2 Recursos, riesgos y plan

El proyecto utiliza archivos públicos, Python y bibliotecas de análisis de datos. La ejecución depende de contar con las versiones y dependencias necesarias, incluido ydata_profiling para generar los informes de perfilado. Las instrucciones de ejecución y los archivos empleados se encuentran en el proyecto.

Entre los riesgos metodológicos, el más importante es confundir una asociación con una causa. También existe el riesgo de comparar grupos muy pequeños, mezclar las asignaturas sin reconocer estudiantes compartidos o interpretar códigos ordinales como medidas exactas. Para reducir estos problemas mantenemos separadas las fuentes, mostramos el número de registros y revisamos las definiciones antes de interpretar.

En las fases de CRISP-DM, este trabajo llega hasta la comprensión y preparación de los datos y presenta la exploración necesaria para interpretar sus resultados. No se ejecutó la fase de modelado para este caso. Si se ampliara el ejercicio con un modelo, correspondería definir primero la pregunta, separar los datos antes de ajustar transformaciones y evaluar el resultado con registros no usados en el entrenamiento.


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

#### 3.2.1 Fuentes y unidad de análisis

Los dos archivos usan las mismas 33 variables y el separador de punto y coma. Matemáticas contiene 395 registros y Portugués contiene 649. Cada fila representa la información de un estudiante en la asignatura correspondiente; la unidad de análisis es, por tanto, el registro de estudiante por materia.

La documentación del conjunto advierte que 382 estudiantes aparecen en ambos archivos. No contamos con un identificador personal único dentro de las tablas que permita tratarlos como dos muestras completamente independientes sin un procedimiento adicional. Por esa razón no unimos las filas ni sumamos los tamaños para hablar de 1.044 personas. La suma de registros sí es útil para describir el volumen de archivos procesados.

La información original combina datos de cuestionarios con notas y registros escolares. Esto amplía el contexto del análisis, pero algunas respuestas sobre hábitos dependen de lo que cada estudiante declaró. No conocemos cómo habría respondido cada persona en otro momento ni podemos comprobar individualmente todas las respuestas.


#### 3.2.2 Variables y tipos de datos

Las columnas incluyen categorías escritas como texto, códigos numéricos de categorías ordenadas y medidas numéricas. School identifica el centro; sex y address describen características registradas en la fuente; studytime, goout, Dalc y Walc son escalas de categorías; absences cuenta ausencias; y G1, G2 y G3 contienen notas.

Es importante distinguir el tipo que reconoce Python del significado de la variable. Por ejemplo, studytime aparece como un número del 1 al 4, pero cada número representa un intervalo de horas, no una cantidad exacta de horas. Del mismo modo, los valores de consumo del 1 al 5 indican niveles ordenados; no describen la cantidad exacta de bebidas. Esta diferencia evita hacer afirmaciones que la base no permite.

La base también contiene información familiar y apoyos educativos. No todas las columnas responden directamente a la pregunta sobre hábitos, pero se conservan en las tablas preparadas para que su uso pueda decidirse según la pregunta concreta. Antes de usar datos personales en otro contexto habría que revisar la finalidad, la privacidad y los posibles efectos de las decisiones tomadas con ellos.


#### 3.2.3 Distribución de edades y notas

En ambos archivos las edades van de 15 a 22 años y la mediana es 17. La edad media es aproximadamente 16,70 en Matemáticas y 16,74 en Portugués. Esto describe a los registros disponibles; no significa que ambas asignaturas tengan exactamente los mismos estudiantes o que los grupos puedan compararse como si hubieran sido asignados al azar.

La nota final de Matemáticas tiene una mediana de 11 y la mitad central de los valores se encuentra entre 8 y 14. En Portugués la mediana es 12 y la mitad central está entre 10 y 14. Estas medidas ayudan a complementar la media: la primera señala un valor central y el intervalo muestra dónde se concentra la parte intermedia de las notas.

Las notas iguales a cero se conservaron porque forman parte de la escala declarada. Sin información adicional no sabemos si cada cero responde a la misma situación académica. Por eso sería incorrecto convertirlos automáticamente en datos faltantes o atribuirles una causa específica.


#### 3.2.4 Frecuencia de hábitos y antecedentes

El tiempo de estudio más frecuente en los dos cursos es el intervalo de 2 a 5 horas semanales: reúne 198 registros en Matemáticas y 305 en Portugués. En el extremo de más de 10 horas hay 27 y 35 registros, respectivamente. La diferencia de tamaño es importante cuando se comparan promedios, porque una media basada en pocos casos puede cambiar más al variar unos cuantos resultados.

En las dos asignaturas predomina el nivel 1 de consumo de alcohol entre semana: 276 registros en Matemáticas y 451 en Portugués. Las categorías más altas tienen menos casos. Esto limita la precisión con la que podemos describir esos grupos y hace especialmente importante mostrar el número de registros junto con sus promedios.

Los fracasos anteriores también están concentrados en una categoría. En Matemáticas, 312 de 395 registros indican cero; en Portugués son 549 de 649. Los grupos con dos o tres fracasos son mucho más pequeños. El análisis bivariado debe leerse con esa distribución en mente.


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

#### 3.3.1 Tiempo de estudio

Los resultados de la tabla 2 muestran una diferencia entre los grupos de menos de 2 horas y los de 5 a 10 horas. En Matemáticas las medias son 10,05 y 11,40; en Portugués son 10,84 y 13,23. La comparación es consistente con la idea de que el tiempo dedicado al estudio puede estar relacionado con el resultado, especialmente en Portugués.

Sin embargo, el promedio del grupo de más de 10 horas no supera al del grupo de 5 a 10 horas en ninguna de las dos materias. No conocemos si esos estudiantes aumentaron su tiempo por encontrar mayor dificultad, si disponían de distintos apoyos o qué otras circunstancias influyeron. La tabla, por sí sola, no permite establecer una explicación.

La diferencia de tamaños también importa: el grupo de 2 a 5 horas reúne a más estudiantes que el de más de 10 horas. Por ello no debemos tomar la última media como una conclusión firme sobre todas las personas que estudian ese tiempo.


#### 3.3.2 Salidas con amigos

La frecuencia de salidas está registrada en una escala del 1 al 5. En Matemáticas, el grupo con nivel 2 tiene una nota media de 11,19 y el de nivel 5 una media de 9,04. En Portugués las medias son 12,67 y 10,87, respectivamente.

No obstante, la pauta no es una línea descendente perfecta. En ambas materias el nivel 1 tiene una media menor que el nivel 2. Además, en Matemáticas ese primer grupo tiene solo 23 registros, frente a 103 en el segundo. Los promedios describen lo que ocurre dentro de cada categoría, pero no demuestran que salir con amigos produzca una determinada nota.

La correlación resumida en la tabla 3 es negativa en ambas asignaturas, aunque de baja magnitud. Esto es compatible con cierta tendencia general, pero no permite ignorar las variaciones entre grupos ni otras condiciones de la vida escolar.


#### 3.3.3 Consumo de alcohol

La base distingue el consumo declarado entre semana y durante el fin de semana. Son escalas ordinales de 1 a 5, por lo que las categorías indican un nivel relativo y no una cantidad exacta. Conviene conservar esa distinción al leer los resultados.

En Portugués, el grupo con nivel 1 de consumo durante el fin de semana tiene una media de 12,36, mientras que el nivel 5 presenta 10,56. Los grupos reúnen 247 y 45 registros, respectivamente. En Matemáticas las medias correspondientes son 10,74 y 10,14, con 151 y 28 registros. El patrón en Portugués aparece más ordenado; en Matemáticas los promedios suben y bajan entre categorías.

La información no permite concluir que el consumo sea la causa directa de las diferencias. Pueden influir simultáneamente el tiempo de estudio, las circunstancias familiares, la asistencia y otros factores no observados. También es posible que la declaración de hábitos no refleje de igual manera la conducta de todas las personas.


#### 3.3.4 Ausencias

La distribución de ausencias tiene varios valores bajos y algunos más altos. En Matemáticas la media es 5,71 y la mediana es 4; en Portugués la media es 3,66 y la mediana es 2. Que la media supere a la mediana sugiere que los valores altos tienen influencia en el promedio.

Al agrupar los registros con diez o más ausencias, la nota media es 10,37 en Matemáticas y 11,13 en Portugués. Esos grupos contienen 83 y 70 registros, respectivamente. En Portugués la media de quienes tienen entre una y cuatro ausencias es 12,07, basada en 222 registros.

En Matemáticas, el grupo sin ausencias tiene una media de 8,44, menor que la de varios grupos con ausencias. Esta observación no debe interpretarse como que faltar mejora las notas: muestra que la relación no es simple y que puede haber situaciones no descritas por el número de ausencias. Sin información sobre el motivo de cada registro o de cada nota, no corresponde explicar la diferencia como un efecto causal.


#### 3.3.5 Fracasos anteriores

Los fracasos académicos previos muestran la relación negativa más clara entre las variables resumidas en la tabla 3. En Matemáticas, la media pasa de 11,25 en el grupo sin fracasos a 8,12 en el grupo con uno. En Portugués pasa de 12,51 a 8,64.

Las categorías con dos y tres fracasos contienen pocos registros: en Matemáticas hay 17 y 16; en Portugués, 16 y 14. Sus promedios pueden consultarse en los archivos de resultados, pero no conviene extrapolarlos a estudiantes fuera de esta muestra. El antecedente académico puede reflejar dificultades previas, condiciones personales u otros factores que la tabla no permite separar.

La comparación puede servir para plantear preguntas sobre apoyos educativos, siempre que se evite convertir un antecedente en un diagnóstico individual. Un promedio de grupo no determina el resultado de una persona concreta.


#### 3.3.6 Lectura conjunta de las relaciones

La comparación entre materias ayuda a ver que una misma variable no siempre se comporta igual. El tiempo de estudio presenta una relación positiva más visible en Portugués; las ausencias muestran una relación ordenada muy pequeña en Matemáticas y negativa en Portugués. Los fracasos previos presentan una asociación negativa en ambos casos.

Estas variables tampoco actúan de manera aislada. Un estudiante que declara más horas de estudio puede tener necesidades o condiciones distintas a las de otro, y varias características pueden estar relacionadas entre sí. El análisis presentado compara una variable a la vez; no estima el efecto independiente de cada una después de controlar por las demás.

Por ello mantenemos la interpretación en el nivel descriptivo. Los resultados sirven para orientar nuevas preguntas y para comprender mejor las dos bases, pero no para establecer qué factor causó la nota final.


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

#### 3.4.1 Qué aporta el perfilado

El perfilado automático reúne en un solo informe información que también revisamos de manera directa con pandas. Para cada archivo se generó un HTML con el tamaño de la base, los tipos detectados, valores ausentes, distribución de variables y alertas. El reporte corresponde a las 33 variables originales de cada asignatura.

La herramienta clasifica 17 variables como texto y 16 como numéricas. Esa clasificación es útil para explorar el archivo, pero no reemplaza la lectura del diccionario: algunas columnas numéricas representan categorías ordenadas y no cantidades continuas. Por ejemplo, una categoría 4 de tiempo de estudio no significa cuatro horas exactas.

Las alertas de valores cero son una invitación a revisar su significado. En failures y absences, el cero representa ausencia del evento registrado; en G3 es una nota posible dentro de la escala. Mantener estos valores evita cambiar la información sin una razón respaldada por la fuente.


#### 3.4.2 Revisión de calidad y límites

En los dos archivos no se encontraron celdas vacías ni filas idénticas en todas sus columnas. Eso simplifica la preparación, aunque no garantiza que no haya respuestas incorrectas, diferencias en la forma de registrar datos o estudiantes parecidos en la base.

Una fila idéntica tampoco bastaría, por sí sola, para demostrar que se trata de una persona repetida: dos estudiantes podrían compartir los mismos valores en un conjunto de variables. En esta revisión no apareció una fila completamente duplicada, por lo que no fue necesario tomar esa decisión.

Los datos originales y sus definiciones están disponibles para revisar las decisiones. Cuando falta información sobre el significado de un caso concreto, preferimos indicar el límite antes que inventar una explicación o eliminar el registro por parecer inusual.


### 3.5 Preparación de los datos

Leímos los CSV con el separador indicado por los archivos y conservamos los dos conjuntos por separado. No fue necesaria una unión: hacerlo sin identificar correctamente a los estudiantes compartidos complicaría la interpretación. Los tipos numéricos y categóricos se revisaron según el diccionario; no hay fechas que convertir en estas fuentes.

No imputamos valores, ya que no se encontraron nulos, ni eliminamos filas por estar incompletas o duplicadas. Tampoco descartamos notas de cero ni registros extremos de ausencias solo por ser poco frecuentes: una cifra extrema no demuestra por sí sola que sea incorrecta. Las agrupaciones por tiempo de estudio, consumo, salidas, ausencias y fracasos anteriores permiten comparar cantidad de registros, media y mediana de G3.

Para facilitar la lectura añadimos studytime_hours, que traduce el código de tiempo de estudio a su intervalo en horas. La columna original se conserva. Si se entrena un modelo, convendría seleccionar una de las dos representaciones para no duplicar la misma información. Las tablas finales se exportaron en CSV, una por asignatura, con 395 y 649 filas y 34 columnas. Mantienen la variable objetivo G3 y los atributos originales; la selección definitiva de predictores dependerá del objetivo y del momento de uso del modelo.

Las fuentes se pueden leer y reproducir con los archivos disponibles. Como no hubo una fusión ni valores faltantes, esas operaciones no requirieron tratamiento adicional. Para un modelo posterior habría que codificar las categorías dentro de un proceso ajustado con los datos de entrenamiento y comprobar que ningún predictor aporte información que no estaría disponible al predecir.

#### 3.5.1 Selección y tratamiento por columnas

Al leer cada CSV, pandas identifica columnas de texto y numéricas a partir de sus valores. El análisis conserva los nombres originales para que se puedan relacionar con el diccionario de la fuente. No hay una columna de fechas que exija conversión temporal en este conjunto.

La variable añadida studytime_hours traduce los códigos de studytime en intervalos legibles: menos de 2 horas, de 2 a 5, de 5 a 10 y más de 10 horas por semana. La transformación no crea una medición nueva; presenta la misma información de una manera más fácil de interpretar. El código original se conserva para facilitar la comparación con la documentación.

Si en otro ejercicio se utilizara un algoritmo que requiera números, habría que elegir una representación adecuada para cada categoría. Las columnas de texto podrían codificarse dentro de un proceso ajustado con el conjunto de entrenamiento. No aplicamos una codificación general ni una normalización en esta práctica, ya que aún no se ha definido un modelo que las requiera.


#### 3.5.2 Valores faltantes y registros repetidos

Antes de imputar datos es necesario comprobar si existen valores faltantes y entender por qué faltan. Aquí el conteo fue cero en ambos archivos, por lo que rellenar valores no tendría un efecto justificado. Tampoco eliminamos columnas por falta de información.

La comprobación de filas completamente duplicadas dio cero. Por eso la tabla preparada conserva el número original de registros en cada asignatura. La coincidencia de estudiantes entre las dos materias es otro problema: no equivale a una fila duplicada dentro de un mismo archivo y no se resolvió eliminando registros.

Mantener las fuentes separadas evita presentar una suma de registros como si fuera un conteo de personas. Si se necesitara estudiar a un mismo estudiante en ambas materias, habría que documentar un criterio de correspondencia y revisar sus posibles errores antes de combinar la información.


#### 3.5.3 Valores extremos y preparación por filas

Las ausencias presentan valores altos respecto de la mayor parte de los registros. Para describirlos se revisó el rango intercuartílico: la diferencia entre el tercer y el primer cuartil. Una regla exploratoria señala valores superiores a Q3 más una vez y media esa diferencia.

En Matemáticas, Q1 es 0 y Q3 es 8; el límite de esa regla es 20 ausencias y 15 registros lo superan. En Portugués, Q1 es 0 y Q3 es 6; el límite es 15 y 21 registros lo superan. Estos conteos no identifican errores: solo señalan casos alejados de la parte central de cada distribución.

No se eliminaron esas filas porque la fuente no aporta evidencia suficiente para considerarlas inválidas. La decisión conserva la variabilidad observada y permite que una persona revise posteriormente los casos si dispone de información adicional. Las agrupaciones de ausencias y hábitos se usan para describir los datos, no para modificar o borrar los registros originales.


#### 3.5.4 Control de las tablas finales

Las dos tablas exportadas mantienen 395 y 649 filas. Cada una contiene 34 columnas: las 33 originales más la etiqueta legible del tiempo de estudio. El análisis comprueba que las tablas puedan volver a leerse, que conserven G3 y que no tengan celdas faltantes tras la transformación.

La existencia de una tabla preparada no significa que ya se haya evaluado un modelo. Antes de usarla para predecir habría que seleccionar variables según la pregunta, definir la información disponible en el momento de predicción y separar entrenamiento y prueba. También habría que revisar los registros compartidos si se combinaran las asignaturas.

En esta entrega las tablas permiten reproducir las comparaciones del informe y disponer de una base ordenada. Las decisiones de limpieza se mantuvieron conservadoras: no se imputaron datos inexistentes, no se eliminaron casos sin evidencia y se documentó la única columna añadida.


## 4. Conclusiones y limitaciones

Encontramos que los grupos con más tiempo de estudio suelen presentar notas medias más altas, especialmente en Portugués, aunque el último grupo no mantiene un aumento continuo y tiene pocos registros. Los fracasos anteriores muestran una asociación negativa más clara con la nota final en ambas asignaturas. Las ausencias, las salidas y el consumo presentan relaciones que varían en intensidad según el curso.

Estos resultados ayudan a formular preguntas, no a identificar causas ni a juzgar estudiantes. Los datos proceden de dos centros y de un contexto histórico concreto; además, algunas respuestas son declaradas por los propios estudiantes y hay personas presentes en ambos archivos. Un uso responsable requeriría considerar el contexto educativo y evitar decisiones individuales basadas solo en estas variables.

### 4.1 Respuesta a la pregunta de trabajo

En las dos asignaturas se observan diferencias en la nota final al comparar grupos de tiempo de estudio. Los promedios más altos aparecen en los intervalos de 5 a 10 y más de 10 horas, aunque la relación no aumenta de forma perfectamente continua. La asociación es más visible en Portugués que en Matemáticas.

Los fracasos anteriores también muestran diferencias importantes en los promedios de G3. En cambio, los resultados de ausencias no siguen una pauta única en ambos cursos. Las salidas y el consumo presentan relaciones negativas en el resumen de correlaciones, pero sus categorías muestran variaciones y tamaños de grupo desiguales.

En conjunto, los resultados respaldan la utilidad de estudiar varias dimensiones al mismo tiempo. No permiten afirmar que una sola conducta explique el rendimiento ni recomendar una decisión individual basada únicamente en una variable.


### 4.2 Limitaciones y uso responsable

El conjunto procede de dos centros de Portugal y refleja un período y una población concretos. Las observaciones no se obtuvieron mediante una asignación experimental de hábitos. Por ello las diferencias entre grupos pueden estar relacionadas con otras características que no aparecen en el archivo o que no se controlaron en este análisis.

Otra limitación es la presencia de estudiantes en ambos archivos. Analizar cada materia por separado evita sumarlos como si fueran personas diferentes, pero no convierte automáticamente a ambas muestras en independientes. Las categorías con pocos registros también requieren cautela y no deberían recibir el mismo peso interpretativo que los grupos más numerosos.

El análisis puede ayudar a formular preguntas y a pensar en apoyos educativos, pero no sustituye el conocimiento del contexto de cada estudiante. Una aplicación responsable combinaría los datos con diálogo, criterios pedagógicos y protección de la información personal.


## 5. Fuentes

Cortez, P. y Silva, A. (2008). Using Data Mining to Predict Secondary School Student Performance.
UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/320/student+performance
Kaggle: https://www.kaggle.com/datasets/dskagglemt/student-performance-data-set
Archivos originales y código de análisis del proyecto.
