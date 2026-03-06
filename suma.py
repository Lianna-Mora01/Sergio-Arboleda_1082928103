total = 0
numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    total += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))

print(f"La suma total es: {total}")