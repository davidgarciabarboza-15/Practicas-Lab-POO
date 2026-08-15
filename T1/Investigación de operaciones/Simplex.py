from fractions import Fraction as F   # fracciones exactas

ganancias   = [3, 5]        # Z = 3x1 + 5x2
consumos    = [[1, 0],      # CPU:     x1 usa 1, x2 usa 0
               [0, 2],      # Memoria: x1 usa 0, x2 usa 2
               [3, 2]]      # Banda:   x1 usa 3, x2 usa 2
disponibles = [4, 12, 18]

n = len(ganancias)      # cuántas variables (2)
m = len(disponibles)    # cuántas restricciones (3)

tabla = []

for i in range(m): # una fila por restricción
    fila = []

    # coeficientes de x1 y x2
    for j in range(n):
        fila.append(F(consumos[i][j]))

    # columnas de holguras (s1,s2,s3) agrega 1 solo en su propia fila
    for k in range(m): 
        if i == k:
            fila.append(F(1))
        else:
            fila.append(F(0))

    # lado derecho (lo disponible)
    fila.append(F(disponibles[i]))
    tabla.append(fila)

# fila Z: ganancias negativas + ceros + Z actual (0)
fila_Z = []
for g in ganancias:
    fila_Z.append(F(-g))
for k in range(m):
    fila_Z.append(F(0))
fila_Z.append(F(0))
tabla.append(fila_Z)          # la fila Z queda en el índice m (la última)

# etiquetas
base = []                     # variable "activa" de cada fila
for k in range(m):
    base.append("s" + str(k + 1))

columnas = ["x1", "x2", "s1", "s2", "s3", "RHS"]   # fijas, nunca cambian

#Simplex
numero_tabla = 0

while True:
    numero_tabla += 1
    #imprimir la tabla actual
    print("\n--- Tabla", numero_tabla)
    encabezado = "    |"
    for nombre in columnas:
        encabezado = encabezado + f"{nombre:>6}"     # >6 = alinear a la derecha
    print(encabezado)

    for i in range(m + 1):
        if i == m:
            etiqueta = "Z"
        else:
            etiqueta = base[i]
        linea = f"{etiqueta:>3} |" #alinea el texto a la derecha ocupando exactamente 3 espacios
        for valor in tabla[i]:
            linea = linea + f"{str(valor):>6}"
        print(linea)

    #1) ya es óptimo? (sin negativos en la fila Z)
    hay_negativo = False
    for j in range(n + m):              # todas las columnas menos RHS = 5
        if tabla[m][j] < 0:
            hay_negativo = True

    if not hay_negativo:
        break            

    #2) variable que ENTRA: la más negativa de la fila Z 
    entra = 0 #Guarda el índice de la columna ganadora
    for j in range(1, n + m):
        if tabla[m][j] < tabla[m][entra]: #-5 < -3 Si
            entra = j

    #3) prueba de la razón: cuánto deja crecer cada fila
    razones = []
    for i in range(m):
        coef = tabla[i][entra]
        if coef > 0:
            razones.append(tabla[i][-1] / coef)   # RHS / coeficiente
        else:
            razones.append(None)                  # esa fila no limita

    # variable que SALE: la fila con la razón más chica
    sale = None
    mejor_razon = None
    for i in range(m):
        r = razones[i]
        if r is not None:
            if mejor_razon is None or r < mejor_razon:
                mejor_razon = r
                sale = i

    texto = ""
    for i in range(m):
        if razones[i] is not None:
            if texto != "":
                texto = texto + ", "
            texto = texto + base[i] + "=" + str(razones[i])

    print("Entra", columnas[entra] + ", sale", base[sale] +
          ", pivote", tabla[sale][entra], "| razones:", texto)

    #4) pivote: convertir el pivote en 1 y limpiar su columna (Gauss-Jordan)
    pivote = tabla[sale][entra]
    nueva_fila = []
    for valor in tabla[sale]:
        nueva_fila.append(valor / pivote)
    tabla[sale] = nueva_fila

    for i in range(m + 1):                       # todas las filas, incluida Z
        if i != sale:
            factor = tabla[i][entra]
            if factor != 0:
                nueva = []
                for j in range(len(tabla[i])):
                    nueva.append(tabla[i][j] - factor * tabla[sale][j])
                tabla[i] = nueva

    #cambiar la etiqueta de la fila (ejemplo: base = ['s1','s2','s3'] ----> base = ['s1','x2','s3'])
    base[sale] = columnas[entra]

# las que no están en base valen 0; las básicas valen su RHS
valor = {"x1": F(0), "x2": F(0)}
for i in range(m):
    valor[base[i]] = tabla[i][-1]

print("\nÓptimo: x1=" + str(valor["x1"]) + ", x2=" + str(valor["x2"]),
      "| Z =", tabla[m][-1])