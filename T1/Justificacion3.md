# Práctica 3 --- Visualización de Datos (Justificaciones)

El script de esta práctica es `Visualizacion.py`. Todas las gráficas se guardan en `img/` y pueden verse en las capturas de ejecución del repositorio.

La práctica pide al menos 5 tipos de gráficas distintas usando ciclos o automatización. Se generaron: histogramas, pasteles, dispersión (mapa), barras y línea. Los ciclos se usaron donde tenía sentido para no escribir el mismo código varias veces (histogramas, pasteles y el mapa por país).

---

## 1. Histogramas (uno por variable numérica)

Se hicieron en un ciclo para `mag`, `depth`, `nst` y `rms`, cada uno con un color distinto para distinguirlos entre sí.

- `hist_mag.png`: deja ver que la mayoría de los sismos son pequeños y los grandes son raros.
- `hist_depth.png`: casi todos los sismos son superficiales, con una cola larga de pocos sismos muy profundos.
- `hist_nst.png` y `hist_rms.png`: de apoyo, para ver cómo se distribuyen las estaciones que miden cada sismo y el residuo.

Se usaron 25 barras porque con 50 se veían demasiado cargados.

---

## 2. Pasteles (proporciones por categoría)

Se hicieron en un ciclo para `pais` y `net_clean`. Se eligió el pastel porque son pocas categorías (4) y la proporción de cada una se ve de un vistazo.

- `pastel_pais.png`: muestra que la mayoría de los sismos del catálogo ocurren en EEUU, seguido de México, y muy pocos en Centroamérica.
- `pastel_net_clean.png`: muestra qué redes registran más sismos (tx y us concentran la mayor parte).

Se quitaron las categorías con poquísimos sismos (menos de 30) porque su rebanada ni se vería y solo ensuciaría la gráfica. El texto se puso un poco más grande para que se lea bien.

---

## 3. Dispersión: mapa de sismos

`mapa.png` grafica latitud contra longitud, que es básicamente un mapa de dónde tiembla. Cada país va con su color (EEUU azul, México verde, Guatemala naranja, Honduras rojo).

Se usaron puntos chiquitos y con transparencia (alpha) porque con casi 8000 sismos, con puntos normales todo se vuelve una mancha y no se aprecian las zonas donde se concentra más actividad.

Lo que se ve: los clusters de Texas, el sur de California, el norte de México y la franja de Centroamérica, coherente con lo que muestran las barras por país.

---

## 4. Barras: sismos por año

`barras_anio.png` cuenta cuántos sismos hubo por año, con un color distinto por año para distinguirlas mejor.

Nota: 2026 sale más bajo porque el año está incompleto (solo hasta agosto); no es un error de los datos.

---

## 5. Barras: magnitud media por país

`barras_mag_pais.png` compara qué tan fuertes son en promedio los sismos de cada zona. Cada país lleva el mismo color que en el mapa para poder relacionar ambas gráficas.

Lo que se ve: EEUU tiene la magnitud media más baja (muchos sismos chicos) y México y Guatemala tienen promedios más altos (menos sismos pero más fuertes).

---

## 6. Línea: sismos por mes

`linea_mes.png` muestra el conteo mensual para ver la tendencia en el tiempo con más detalle que la gráfica por año. Como son 80 meses, se puso una etiqueta cada 12 para que el eje no se amontonara.

---

## 7. Notas

1. Se reutilizó la función `categorize_pais` de la Práctica 2 para poder colorear el mapa y hacer las barras por país; al ser el mismo proyecto, tiene sentido aprovechar el código propio.
2. No se repitió el boxplot aquí porque ya se generó en la Práctica 2 (`img/boxplot_pais.png` e `img/boxplot_red.png`); con histogramas, pasteles, dispersión, barras y línea quedan cubiertos los 5 tipos pedidos.
3. Referencias consultadas:
   - https://matplotlib.org/stable/plot_types/index.html (para elegir el tipo de gráfica adecuado según el dato)
