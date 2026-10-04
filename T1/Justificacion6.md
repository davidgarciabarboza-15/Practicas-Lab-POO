# Práctica 6 --- Clasificación de Datos (Justificaciones)

El script de esta práctica es KNN.py. Los números exactos (accuracy de cada experimento, k elegido, matriz de confusión y reporte por clase) quedan en las capturas de ejecución, y las dos gráficas se guardan como knn_barrido_k.png y knn_clases_mag_depth.png. La tarea fue clasificar de qué país es un sismo usando únicamente cómo se registró, con el algoritmo KNN.

## La tarea y cómo se armó

La etiqueta es el país (la categoría que arrastramos desde la práctica 2), recortada a tres clases: EEUU, MEXICO y GUATEMALA. Honduras quedó fuera de la clasificación a propósito: con apenas 34 sismos, ningún vecino votaría jamás por esa clase y el modelo nomás se la tragaría; es más honesto excluirla y decirlo aquí que aparentar que se clasifica una clase sin soporte.

Las características son cómo se registró el sismo: profundidad, magnitud, número de estaciones (nst y magNst), gap azimutal (el hueco de dirección más grande entre las estaciones que reportaron), distancia a la estación más cercana (dmin) y rms. Latitud y longitud se dejaron fuera a propósito, y eso es importante: con ellas, el país es simplemente geografía (un sismo en Texas es de EEUU porque está en Texas), y el modelo acertaría casi todo sin aprender nada. Sin ellas, la pregunta que queda es la interesante: si la huella de cómo se registró el sismo alcanza para revelar el país.

Los datos se parten 70/30 en entrenamiento y prueba, de forma estratificada (cada parte conserva la misma proporción de clases que el total) y con semilla 42 para que la partición sea la misma en cada ejecución.

## KNN en corto y por qué escalar

KNN clasifica por votación: para un sismo nuevo busca los k sismos ya conocidos más parecidos (los más cercanos en características) y la clase mayoritaria entre esos vecinos gana. Y "cercanos" se mide con distancias, lo que trae el punto central de la práctica: la escala de cada característica. El gap vive entre 0 y 360 y el dmin entre 0 y 8; sin tocar nada, la distancia entre dos sismos sería básicamente el gap y las demás características ni participarían. Por eso el mismo KNN se corrió con y sin StandardScaler (que deja cada característica con media 0 y varianza 1), comparado con validación cruzada sobre el entrenamiento: la versión escalada es la que gana, y por cuánto queda en las capturas. El scaler se ajusta solo con entrenamiento para no espiar el test.

## Cómo se eligió k y por qué el test no se toca hasta el final

El k se eligió barriendo valores (1, 3, 5, hasta 15) y evaluando cada candidato con validación cruzada de 5 folds sobre el entrenamiento nada más: el entrenamiento se parte 5 veces en 4 pedazos para ajustar y 1 para medir, y se promedian las 5 mediciones. La curva de accuracy contra k queda en knn_barrido_k.png y el valor elegido aparece en las capturas.

La razón de no elegir k mirando el accuracy del test es que el test es el árbitro: sirve para estimar cómo le va al modelo con datos que nunca vio. Si se le consulta para tomar decisiones (como con qué k quedarnos), deja de ser imparcial y el accuracy final sale optimista. Con validación cruzada, todas las decisiones (escalar, elegir k) se toman mirando solo el entrenamiento, y el test se evalúa una única vez, al final, con el modelo ya cerrado.

Junto al accuracy del modelo final se imprime el piso a vencer: un modelo tonto que siempre diga la clase mayoritaria (EEUU) acierta esa proporción sin aprender nada. Si el KNN no le ganara a ese piso, no serviría. Después vienen la matriz de confusión (quién se confundió con quién) y el reporte por clase (precisión y recall de cada país).

## Cómo se leen los resultados

El patrón que aparece en la matriz tiene explicación clara. Guatemala se clasifica casi sin error porque sus sismos viven en otra parte del espacio de características: profundidad mediana de unos 74 km contra unos 7 km de EEUU y unos 10 km de MEXICO, una diferencia que ya teníamos desde la práctica 4. EEUU y MEXICO en cambio se prestan a confusión: ambos son sismos mayormente someros y con coberturas parecidas, y sus nubes se traslapan. La dispersión por clases (knn_clases_mag_depth.png, con los mismos colores de todo el proyecto) enseña justo eso: Guatemala en su zona profunda y los otros dos mezclados en la parte somera.

Como verificación final se implementó un KNN a mano (distancia euclidiana y votación por mayoría, la misma lógica del classification.org del material de la materia) y se comparó contra sklearn sobre una muestra de 200 sismos del test: ambos coinciden, lo que confirma que la librería está haciendo lo que creemos que hace. La muestra es de 200 y no todo el test porque a mano y con ciclos, la comparación completa tardaría minutos.

## Notas

1. Del classification.org del material de la materia se rescataron dos ideas: la dispersión coloreada por clase y el KNN a mano como verificación. No se rescató lo demás: los datos sintéticos (tenemos datos reales), el get_cmap que está deprecado, y usar el KNN a mano como modelo principal, que no tiene evaluación y con 7893 sismos en ciclos puros tardaría minutos.
2. Los valores exactos de accuracy, k y matriz quedan en las capturas de ejecución; aquí se explica qué significa cada uno y por qué sale así.
3. Referencias consultadas:
   - https://github.com/ppGodel/data_mining (material de la materia; classification.org con el KNN a mano y la dispersión por clase)
   - https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm (concepto de KNN: votación de los vecinos más cercanos)
   - https://en.wikipedia.org/wiki/Cross-validation_(statistics) (validación cruzada y por qué las decisiones se toman en entrenamiento)
   - https://scikit-learn.org/stable/modules/preprocessing.html (por qué escalar en métodos que viven de distancias)
