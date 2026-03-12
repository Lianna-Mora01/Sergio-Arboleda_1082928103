edad=17
if edad>18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
for i in range(5): 
    print("Hola Mundo")
contador=1
while contador<=5:
 print("Númmero:" + str(contador))
 contador = contador + 1

 for i in range(5):
        print("Número:" + str(i))

for i in range(0,12, 6):
        print("Número:" + str(i))

 

enconrtado=False
numerobuscado=7
numeros =[1,3,5,7,9]
for numero in numeros:
        if numero==numerobuscado:
         encontrado=True
         break
print ("Número", numerobuscado, "encontrado:", encontrado)

for i in range(3):
    for j in range(3):
         print("i=" + str(i) + ", j=" + str(j))