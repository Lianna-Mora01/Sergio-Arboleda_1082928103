pares = [2,4,6,8,10]
impares = [1,3,5,7,9]

for i in range(10):
    numero = int(input(f"Ingresa el número {i+1}: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")