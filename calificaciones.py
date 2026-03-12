mayor = -1
menor = 6
nombre_mayor = ""
nombre_menor = ""
suma = 0

for i in range(5):
    nombre = input("Nombre del estudiante: ")

    edad = int(input("Edad: "))
    while edad < 5 or edad > 100:
        print("Edad inválida. Intente de nuevo.")
        edad = int(input("Edad: "))

    nota = float(input("Calificación: "))
    while nota < 0 or nota > 5:
        print("Calificación inválida. Intente de nuevo.")
        nota = float(input("Calificación: "))

    suma = suma + nota

    if nota > mayor:
        mayor = nota
        nombre_mayor = nombre
        
    if nota < menor:
        menor = nota
        nombre_menor = nombre

promedio = suma / 5

print("Estudiante con mayor calificación:", nombre_mayor, mayor)
print("Estudiante con menor calificación:", nombre_menor, menor)
print("Promedio de calificaciones:", promedio)