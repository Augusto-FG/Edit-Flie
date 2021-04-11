import random

def crear_matriz (n):
    matriz = []
    filas = n
    columnas = n
    for f in range(filas):
        matriz.append([0]*columnas)
    return matriz



def rellenar_matriz(matriz,n):
    filas = len(matriz)
    columnas = len(matriz)
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c]=random.randint(0, 10)
    

def imprimir (matriz):
    filas = len (matriz)
    columnas = len (matriz[0])
    for f in range (filas):
        for c in range (columnas):
            print ("%3d" %matriz[f][c], end ="")
        print ()
         
def sumar_filas(matriz):
    sumas = [0] * len(matriz)
    for f in range(len(matriz)):
        sumas[f] = sum(matriz[f])
    return sumas

def sumar_columnas(matriz):
    sumas = [0] * len(matriz)
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            sumas[c] += matriz[f][c]
    return sumas

def suma_diag_ID(matriz):
    suma=0
    for f in range(len(matriz)):
        suma += matriz[f][f]
    return suma

def suma_diag_DI(matriz):
    suma=0
    col = len(matriz)-1
    for f in range(len(matriz)):
        suma += matriz[f][col]
        col -=1
    return suma

n = int (input("Ingrese tamaño matriz:"))
print("")

matriz = crear_matriz(n)

rellenar_matriz(matriz,n)

imprimir (matriz)

print("")

suma_filas = sumar_filas(matriz)
print("Suma de las filas:", suma_filas)

suma_columnas = sumar_columnas(matriz)
print("Suma de las columnas:",suma_columnas)

suma_dia_ID = suma_diag_ID(matriz)
print("Suma de la diagonal Izquierda - Derecha:", suma_dia_ID)

suma_dia_DI = suma_diag_DI(matriz)
print("Suma de la diagonal Derecha - Izquierda:", suma_dia_DI)

print ("")

if suma_filas == suma_columnas == suma_dia_ID == suma_dia_DI:
    print ("Es un cuadrado mágico") 
else:
    print("No es un cuadrado mágico")