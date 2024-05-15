#Ejnum: 1 
import random
def menu():
    print("\nOpciones:")
    print("a. Mostrar los números ingresados.")
    print("b. Mostrar el promedio del arreglo.")
    print("c. Mostrar la longitud del arreglo.")
    print("d. Encontrar y mostrar:")
    print("   1. La suma de posiciones pares")
    print("   2. La suma de posiciones impares")
    print("x. Salir")

def main():
    print("Semana No. 16: Ejercicio 1")

    numeros = [random.randint(1, 100) for _ in range(10)]

    while True:
        menu()
        opcion = input("Ingrese una opción: ").lower()

        if opcion == 'a':
            print("Números ingresados:", numeros)
        elif opcion == 'b':
            promedio = sum(numeros) / len(numeros)
            print("El promedio del arreglo es:", promedio)
        elif opcion == 'c':
            longitud = len(numeros)
            print("La longitud del arreglo es:", longitud)
        elif opcion == 'd':
            sumapares = sum(numeros[::2])  
            sumaimpares = sum(numeros[1::2])  
            print("La suma de posiciones pares es:", sumapares)
            print("La suma de posiciones impares es:", sumaimpares)
        elif opcion == 'x':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

##Ejnum: 2

import random

def main():
    print("Semana No. 16: Ejercicio 2")

    filas = int(input("Ingrese la cantidad de filas: "))
    columnas = int(input("Ingrese la cantidad de columnas: "))
    matriz = [[0] * columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = random.randint(0, 1000)
    numpares = 0
    numimpares = 0
    nummayor = None
    nummenor = None

    for fila in matriz:
        for numero in fila:
            if numero % 2 == 0:
                numpares += 1
            else:
                numimpares += 1
            if nummayor is None or numero > nummayor:
                nummayor = numero
            if nummenor is None or numero < nummenor:
                nummenor = numero
    print("\nEstadísticas:")
    print("Cantidad de números pares:", numpares)
    print("Cantidad de números impares:", numimpares)
    print("Número mayor:", nummayor)
    print("Número menor:", nummenor)
if __name__ == "__main__":
    main()

