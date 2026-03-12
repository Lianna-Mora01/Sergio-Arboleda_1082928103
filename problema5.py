cantidad = 0
suma = 0
pares = 0
impares = 0
mayor = None
menor = None

while True:

    numero = int(input("Ingrese un número (0 para terminar): "))

    if numero == 0:
        break

    cantidad += 1
    suma += numero

    if mayor is None or numero > mayor:
        mayor = numero

    if menor is None or numero < menor:
        menor = numero

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

if cantidad > 0:
    promedio = suma / cantidad
else:
    promedio = 0

print("Cantidad de números:", cantidad)
print("Suma total:", suma)
print("Promedio:", promedio)
print("Número mayor:", mayor)
print("Número menor:", menor)
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)