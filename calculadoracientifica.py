import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return round(area, 2)

def calcular_hipotenusa(cateto1, cateto2):
    h = math.sqrt(cateto1*2 + cateto2*2)
    return round(h, 2)

def calcular_potencia(base, exponente):
    resultado = math.pow(base, exponente)
    return resultado

def main():

    opcion = 0

    while opcion != 4:

        print("\n--- CALCULADORA CIENTÍFICA ---")
        print("1. Calcular área de círculo")
        print("2. Calcular hipotenusa")
        print("3. Calcular potencia")
        print("4. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            radio = float(input("Ingrese el radio: "))
            area = calcular_area_circulo(radio)
            print("El área del círculo es:", area)

        elif opcion == 2:
            a = float(input("Ingrese el cateto 1: "))
            b = float(input("Ingrese el cateto 2: "))
            h = calcular_hipotenusa(a, b)
            print("La hipotenusa es:", h)

        elif opcion == 3:
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            resultado = calcular_potencia(base, exponente)
            print("Resultado:", resultado)

        elif opcion == 4:
            print("Saliendo del programa...")

        else:
            print("Opción no válida")

main()