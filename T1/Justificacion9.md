# Práctica 9 Análisis de Texto

El script de esta práctica es Analisis_Texto.py y sus gráficas se guardan como nube_palabras_general.png y nube_palabras_por_pais.png. La tarea fue generar una nube de palabras y hacer un análisis exploratorio sobre datos textuales, y el corpus que usamos ya estaba en el proyecto desde la práctica 1 sin que nadie lo hubiera leído como texto, que es la columna place.

## El corpus que ya teníamos

Cada place es una frase escrita por el USGS con su propia gramática, una distancia en kilómetros, una dirección de brújula, un pueblo de referencia y un estado o país al final, como en "25 km NE of Pijijiapan, Mexico". Esas mismas palabras son las que en la práctica 2 convertimos en categorías de país con reglas, así que leerlas ahora como texto conecta con ese trabajo anterior. El corpus son 7893 lugares de los cuales solo una parte son cadenas distintas, y esa diferencia entre lugares totales y lugares únicos ya anticipa el análisis de repetidos que viene más abajo. Los números exactos de esto y de todo lo demás quedan en las capturas de ejecución.

## Qué dice el texto sin limpiar

Antes de tocar nada se imprimieron los 15 tokens más frecuentes del texto tal cual viene, y ahí domina el formato. La palabra km aparece una vez por lugar, la palabra of también, y las direcciones de brújula igual, así que sin limpieza la nube se pintaría con palabras de formato y no diría nada de dónde tiembla. Ese print es la evidencia que justifica la limpieza, y no una costumbre.

## La limpieza y lo que queda

La limpieza pasa todo a minúsculas y quita los números, la palabra km, las palabras vacías (of, the, and) y las direcciones de brújula con sus combinaciones. Lo que queda son topónimos, nombres de pueblos, estados y países, y el top 20 limpio los muestra ordenados por frecuencia en la salida. El número de palabras distintas baja mucho respecto al texto crudo, y esa bajada también es parte del resultado porque mide cuánto del texto era formato.

## Las nubes

La nube general se dibuja con las frecuencias limpias y deja ver los topónimos del catálogo por tamaño. La rejilla 2x2 repite el ejercicio por país y ahí cada subconjunto pinta sus propias palabras, EEUU con sus estados y pueblos, México y Guatemala con sus municipios, y Honduras con una nube muy flaca porque apenas aporta 34 sismos, 85 palabras contra las 14096 de EEUU según los títulos de la propia rejilla. Para no depender solo de la imagen, el top 8 de tokens por país queda también impreso en la salida.

La rejilla deja además dos detalles que vale la pena leer. En la nube de EEUU las palabras new y mexico salen enormes porque el USGS escribe esos lugares como New Mexico, y el token mexico aparece miles de veces en un país que no es México, justo el caso que la regla de la práctica 2 ya resolvía al dejar esos places del lado de EEUU, así que la nube confirma con sus propias palabras por qué esa regla era necesaria. Y en las nubes de Guatemala y México se ven tokens cortados como concepci o amatit, porque la limpieza solo acepta letras de la a a la z y al toparse con un acento parte la palabra y tira el pedazo final, una limitación que no cambia las conclusiones pero que queda escrita por honestidad.

## Lugares repetidos y secuencias de réplicas

Contar cuántas veces se repite cada cadena de place exacta muestra que hay lugares que aparecen cientos de veces. Un place idéntico cientos de veces no es coincidencia, es una secuencia de réplicas del mismo epicentro, los mismos enjambres que vemos desde la práctica 3 pero detectados ahora con puro texto. La salida deja el top 10 de lugares repetidos y cuántos lugares se repiten 50 veces o más, junto con cuántos sismos juntan entre todos.

## Qué se rescató del material de la materia

Del word_cloud.py y el text_cloud.py del material se rescató el min_font_size para que las palabras poco frecuentes también alcancen a verse, y la confirmación de que el flujo básico de la práctica es frecuencias, nube y png. No se rescató el open_file de un texto.txt porque nuestro corpus es una columna del csv, ni el generate con texto sin limpiar porque en nuestro corpus eso pintaría km y direcciones en grande, ni el ciclo redundante que re-une tokens que ya estaban separados, ni el plt.show antes del savefig. El código del profe no limpia nada y en su texto de cuatro palabras eso no se nota, pero con 7893 lugares la limpieza es lo que separa una nube informativa de un dibujo de formato.

## Conclusión

La columna place resultó ser texto de verdad y no solo una etiqueta. Ya limpio, sus palabras más frecuentes son los pueblos y estados donde tiembla, coherente con lo que el proyecto ya sabía de países y regiones, y sus cadenas repetidas detectan secuencias de réplicas sin usar tiempo ni coordenadas, solo texto. La nube sirve como vista de conjunto del catálogo y el exploratorio es la parte que la explica, con el detalle de que Honduras apenas pinta porque 34 sismos no alcanzan para más.

## Notas

1. Los valores exactos de frecuencias, lugares repetidos y conteos de palabras quedan en las capturas de ejecución.
2. Referencias consultadas
   - https://github.com/ppGodel/data_mining (material de la materia, word_cloud.py y text_cloud.py con el flujo básico de la nube)
   - https://en.wikipedia.org/wiki/Word_cloud (qué representa una nube de palabras y cómo se define el tamaño)
   - https://wordcloud.readthedocs.io/ (librería wordcloud, generate_from_frequencies y sus parámetros)
