estudiantes = ["Laura", "Valerie" , "Juan" , "Shayla" , "Valeri" , "Adriana", "Marcos" , "Xavi" , "Juan orozco" , "María"]  
estudiantes.append("Shayla")
print(estudiantes) # ['Laura', 'Valerie', 'Juan', 'Shayla', 'Valeri', 'Adriana', 'Marcos', 'Xavi', 'Juan orozco', 'María', 'Shayla']

#Cantidad de estudiantes
print(len(estudiantes)) # 11

# Buscar un estudiante
if "Xavi" in estudiantes:
    print("Xavi está en la lista de estudiantes.")
if "Shayla" in estudiantes:
    print("Shayla está en la lista de estudiantes.")
if "Valeri" in estudiantes:
    print("Valeri está en la lista de estudiantes.")
if "Adriana" in estudiantes:
    print("Adriana está en la lista de estudiantes.")
 # Eliminar un estudiante
estudiantes.remove("Juan orozco")
print(estudiantes) # ['Laura', 'Valerie', 'Juan', 'Shayla', 'Valeri', 'Adriana', 'Marcos', 'Xavi', 'María', 'Shayla']
estudiantes.remove("Shayla")
print(estudiantes) # ['Laura', 'Valerie', 'Juan', 'Valeri', 'Adriana', 'Marcos', 'Xavi', 'María', 'Shayla']

estudiantes.append("Edwin")
print(estudiantes) # ['Laura', 'Valerie', 'Juan', 'Valeri', 'Adriana', 'Marcos', 'Xavi', 'María', 'Shayla', 'Edwin']