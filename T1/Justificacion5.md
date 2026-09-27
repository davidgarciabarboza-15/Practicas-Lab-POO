# Práctica 5 --- Modelos Lineales y Correlación (Justificaciones)

El script de esta práctica es `Modelos_Lineales.py`. Los valores exactos (matrices de correlación, top de pares, R2 y p de cada modelo) quedan en las capturas de ejecución, y las dos gráficas se guardan en `img/` como `lr_conteo_mensual_vs_indice_tiempo.png` y `lr_dmin_vs_gap_azimutal.png`. El trabajo fue: primero ver cuáles variables numéricas se correlacionan, y después ajustar dos modelos lineales con su gráfica y su R2.

## Cómo se eligió el par del segundo modelo

En vez de escoger un par a mano, se sacó la matriz de correlación de Pearson y de Spearman sobre las variables numéricas (mag, depth, nst, gap, dmin, rms, magNst), y se dejó que ganara el par con correlación más fuerte en valor absoluto de Spearman. Spearman manda para elegir porque desde la práctica 4 sabemos que los datos no son normales, y Spearman no asume normalidad ni línea recta, solo que la relación sea monotónica. El par ganador fue gap contra dmin, y el script imprime un top 5 de pares para que la elección se pueda ver completa y no parezca un truco de magia.

¿Por qué correlacionan esas dos? Las dos describen qué tan bien la red "vio" el sismo: dmin es la distancia a la estación más cercana que lo registró, y gap es el hueco azimutal más grande que queda entre las estaciones que reportaron. Si un sismo ocurre lejos de cualquier estación, la cobertura es pobre y el gap crece; por eso la relación positiva. No es una ley física, es una consecuencia operativa de cómo se construye el catálogo, y por eso es defendible.

El código revisa además dos trampas antes de confiar en el par: avisa si el ganador involucra depth (las profundidades por defecto del USGS podrían inflar la correlación) y avisa si Pearson y Spearman discrepan mucho (señal de que la relación no es lineal). En esta corrida el ganador no lleva depth, así que la primera trampa no se activó.

## Modelo 1: conteo mensual contra tiempo, al estilo del material

Este imita el ejemplo de la materia: se agrupa por mes, se cuentan los sismos, y como el mes no es numérico se convierte en un índice 0, 1, 2, ... para poder regresionarlo (el mismo truco de transform_variable del material). Después un OLS con statsmodels y la gráfica con la dispersión, la recta roja de la regresión y la línea verde del promedio de y.

Lo que se ve en la gráfica es justo lo que ya sospechábamos desde la práctica 3: la recta roja queda casi plana y pegada a la verde. Hay meses con enjambres (los picos de alrededor de 250 sismos) y meses tranquilos, pero alrededor de un piso de unos 100 sismos que no crece ni decrece con los años. La conclusión es que no hay tendencia lineal: el conteo mensual no va subiendo ni bajando sistemáticamente, y el R2 salió casi cero. La regresión aquí no le gana al modelo ingenuo de "predice siempre el promedio".

## Modelo 2: dmin contra gap azimutal, el par de la matriz

La gráfica de este modelo se ve distinta: una nube que se abre en abanico. Con gap chico, dmin está casi obligado a ser chico (buena cobertura implica una estación cerca), y con gap grande, dmin puede ser casi cualquier cosa aunque en promedio crece. La recta roja con pendiente positiva se separa claramente de la verde, así que sí hay una tendencia que la recta captura, pero la dispersión es enorme: el R2 queda moderado, no alto. La forma de abanico lo explica: la relación es más de tendencia monotónica que de línea apretada, y por eso se eligió con Spearman.

Un detalle que vale la pena dejar escrito: con 7893 datos, la pendiente de este modelo sale significativa (p minúsculo), pero el R2 moderado recuerda que significativo no es lo mismo que ajustar bien. La significancia dice "la tendencia no es casualidad"; el R2 dice "cuánta de la dispersión alcanza a explicar la recta". Aquí la tendencia existe, pero la recta solo explica una parte.

## La línea verde y contra qué compara el R2

La línea verde es el modelo base o modelo nulo: el que siempre predice el promedio de y sin mirar x. No es decoración: el R2 se define comparando contra ese modelo, R2 = 1 menos (el error de tu recta) entre (el error del promedio). Por eso en el modelo 1, donde la roja queda pegada a la verde, el R2 es casi cero, y en el modelo 2, donde se separan, el R2 sí sube. Ver las dos líneas dibujadas deja leer el R2 con los ojos antes de leer el número.

## Qué nos dejan estos dos modelos

Por un lado, la actividad sísmica del catálogo no tiene tendencia lineal en el tiempo: es estacionaria, con picos de enjambres y réplicas, coherente con lo que ya habíamos visto en las prácticas 3 y 4. Por otro, las métricas de cobertura de la red (gap y dmin) sí se relacionan positivamente, pero con una forma de abanico que ninguna recta aprieta del todo. Y como lección de la práctica: una recta puede ser significativa y aun así explicar poco, y la línea verde del promedio está ahí para que no se nos olvide.

## Notas

1. El script está inspirado en el ejemplo de Linear Regression del material de la materia (lo de volver la fecha índice, la dispersión con recta roja y el guardado del png), pero los coeficientes se sacan directo con model.params en vez del hack de read_html del material, que aventaba warnings, y la línea verde del promedio se tomó de la variante L2 del mismo material.
2. El par del modelo 2 lo eligió la matriz de correlación en la ejecución, no se fijó a mano; el top 5 impreso y las matrices quedan en las capturas.
3. Referencias consultadas:
   - https://github.com/ppGodel/data_mining (material de la materia; ejemplo de regresión lineal con datos de UANL)
   - https://en.wikipedia.org/wiki/Coefficient_of_determination (contra qué compara exactamente el R2 y por qué la línea del promedio es la base)
   - https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html (OLS de statsmodels)
