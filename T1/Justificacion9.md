# Práctica 9 Análisis de Texto

La tarea fue generar una nube de palabras y hacer un análisis exploratorio sobre datos textuales, y el corpus que se uso ya estaba en el proyecto desde la práctica 1 sin que nadie lo hubiera leído como texto, que es la columna place.

## El corpus que ya teníamos

Cada place es una frase escrita por el USGS con su propia gramática, una distancia en kilómetros, una dirección de brújula, un pueblo de referencia y un estado o país al final, como en "25 km NE of Pijijiapan, Mexico", esas mismas palabras son las que en la práctica 2 convertimos en categorías de país, así que leerlas ahora como texto conecta con ese trabajo anterior. 


El corpus son 7893 lugares de los cuales solo una parte son cadenas distintas, y esa diferencia entre lugares totales y lugares únicos ya anticipa el análisis de repetidos que viene más abajo (los números exactos de esto y de todo lo demás quedan en las capturas de ejecución).

## Qué dice el texto sin limpiar

Antes de tocar nada se imprimieron los 15 tokens más frecuentes del texto tal cual viene, y ahí domina el formato. La palabra of aparece en casi todos los lugares y la km también, porque la gramática del USGS casi siempre incluye distancia y rumbo, y las direcciones de brújula suman otro tanto entre todas, así que sin limpieza la nube se pintaría con palabras de formato y no diría nada de dónde tiembla.


## La limpieza y lo que queda

La limpieza pasa todo a minúsculas y quita los números, la palabra km, las palabras vacías (of, the, and) y las direcciones de brújula con sus combinaciones, y lo que queda son nombres de pueblos, estados y países, y el top 20 limpio los muestra ordenados por frecuencia en la salida. El número de palabras distintas baja poco en el vocabulario, de 859 a 828, porque lo que se quita son apenas unas 31 palabras de formato, pero esas pocas concentraban buena parte de todas las apariciones, ya que solo of y km juntan más de 15 mil de las cerca de 47 mil palabras del corpus, y ahí sí se ve cuánto del texto era formato y no contenido.

## Las nubes

La nube general se dibuja con las frecuencias limpias y deja ver los topónimos del catálogo por tamaño. 


La rejilla 2x2 repite el ejercicio por país y ahí cada subconjunto pinta sus propias palabras, EEUU con sus estados y pueblos, México y Guatemala con sus municipios, y Honduras con una nube muy flaca porque apenas aporta 34 sismos, 85 palabras contra las 14096 de EEUU según los títulos de la propia rejilla. Para no depender solo de la imagen, el top 8 de tokens por país queda también impreso en la salida.

La rejilla deja además dos detalles que vale la pena leer, en la nube de EEUU las palabras new y mexico salen enormes porque el USGS escribe esos lugares como New Mexico, y el token mexico aparece miles de veces en un país que no es México, justo el caso que la regla de la práctica 2 ya resolvía al dejar esos places del lado de EEUU, así que la nube confirma con sus propias palabras por qué esa regla era necesaria. Y en las nubes de Guatemala y México se ven tokens cortados como concepci o amatit, porque la limpieza solo acepta letras de la a a la z y al toparse con un acento parte la palabra y tira el pedazo final, una limitación que no cambia las conclusiones pero vale la pena aclarar.

## Lugares repetidos y secuencias de réplicas

Contar cuántas veces se repite cada cadena de place exacta muestra que hay lugares que aparecen cientos de veces, y el caso más extremo es la secuencia de Whites City, New Mexico, que ocupa cinco de los diez primeros lugares con variantes de distancia que juntas pasan de mil sismos, y detrás aparecen western Texas, Toyah y la región de Revilla Gigedo. Un place idéntico cientos de veces no es coincidencia, es una secuencia de réplicas del mismo epicentro, los mismos enjambres que vemos desde la práctica 3 pero detectados ahora con puro texto. 


La salida deja el top 10 de lugares repetidos y cuántos lugares se repiten 50 veces o más, junto con cuántos sismos juntan entre todos.


## Conclusión

La columna place resultó ser texto de verdad y no solo una etiqueta, y ya limpio, sus palabras más frecuentes son los pueblos y estados donde tiembla, coherente con lo que el proyecto ya sabía de países y regiones, y sus cadenas repetidas detectan secuencias de réplicas sin usar tiempo ni coordenadas, solo texto. La nube sirve como vista de conjunto del catálogo y el exploratorio es la parte que la explica, con el detalle de que Honduras apenas pinta porque 34 sismos no alcanzan para más.

## Notas

1. Del material (word_cloud.py y text_cloud.py) se tomó la idea del min_font_size y el flujo de frecuencias, nube y png.
2. Los valores exactos de frecuencias, lugares repetidos y conteos de palabras quedan en las capturas de ejecución.
3. Referencias consultadas
   - https://github.com/ppGodel/data_mining (word_cloud.py y text_cloud.py)
   - https://en.wikipedia.org/wiki/Word_cloud (qué representa una nube de palabras y cómo se define el tamaño)
   - https://wordcloud.readthedocs.io/ (librería wordcloud, generate_from_frequencies y sus parámetros)
