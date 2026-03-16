def validar_cedula(cedula):
    if cedula.isdigit() and 8 <= len(cedula) <= 10:
        return True
    else:
        return False


# 2. Validar email
def validar_email(email):
    if "@" in email and email.endswith(".com"):
        return True
    else:
        return False


# 3. Validar calificaciones
def validar_calificaciones(calificaciones):
    for nota in calificaciones:
        if nota < 0 or nota > 5:
            return False
    return True


# 5. Calcular promedio
def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return round(promedio, 2)


# 6. Clasificar desempeño
def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"


# 4. Crear estudiante
def crear_estudiante(cedula, nombre, email, calificaciones):

    if not validar_cedula(cedula):
        return None

    if not validar_email(email):
        return None

    if not validar_calificaciones(calificaciones):
        return None

    promedio = calcular_promedio(calificaciones)

    estudiante = {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio
    }

    return estudiante


# 7. Listar estudiantes
def listar_estudiantes(lista_estudiantes):

    print("Cedula | Nombre | Promedio | Desempeño")

    for e in lista_estudiantes:
        desempeño = clasificar_desempeño(e["promedio"])
        print(e["cedula"], "|", e["nombre"], "|", e["promedio"], "|", desempeño)


# 8. Programa principal
def main():

    estudiantes = []

    while True:

        print("\nMENU")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            notas_texto = input("Calificaciones separadas por coma: ")

            lista_notas = notas_texto.split(",")

            calificaciones = []
            for n in lista_notas:
                calificaciones.append(float(n))

            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)

            if estudiante == None:
                print("Error: datos inválidos")
            else:
                estudiantes.append(estudiante)
                promedio = estudiante["promedio"]
                desempeño = clasificar_desempeño(promedio)

                print("Estudiante agregado exitosamente")
                print("Promedio:", promedio, "| Desempeño:", desempeño)

        elif opcion == "2":
            listar_estudiantes(estudiantes)

        elif opcion == "3":

            buscar = input("Cédula a buscar: ")
            encontrado = False

            for e in estudiantes:
                if e["cedula"] == buscar:
                    desempeño = clasificar_desempeño(e["promedio"])
                    print(e["nombre"], "| Promedio:", e["promedio"], "| Desempeño:", desempeño)
                    encontrado = True

            if not encontrado:
                print("Estudiante no encontrado")

        elif opcion == "4":
            print("Programa finalizado")
            break

        else:
            print("Opción inválida")


# Ejecutar programa
main()