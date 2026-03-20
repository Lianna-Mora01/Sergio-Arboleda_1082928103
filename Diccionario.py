persona = {"nombre": "Lianna", "edad": 17, "ciudad": "Santa Marta"}
#Iterar sobre las claves del diccionario
for clave in persona:
    print(clave)
#Iterar sobre valores pares clave-valor
for clave, valor in persona.items():
    print(clave + ": " + str(valor))
