import datetime

def crear_evento(nombre, dia, mes, año):
    fecha = datetime.date(año, mes, dia)
    evento = {"nombre": nombre, "fecha": fecha}
    return evento

def dias_hasta_evento(fecha_evento):
    hoy = datetime.date.today()
    diferencia = fecha_evento - hoy
    return diferencia.days

def evento_pasado(fecha_evento):
    hoy = datetime.date.today()
    if fecha_evento < hoy:
        return True
    else:
        return False

def main():

    nombre = input("Nombre del evento: ")

    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))

    evento = crear_evento(nombre, dia, mes, año)

    fecha_evento = evento["fecha"]

    dias = dias_hasta_evento(fecha_evento)

    if evento_pasado(fecha_evento):

        dias_pasados = abs(dias)
        print("El evento ya pasó. Fue hace", dias_pasados, "días.")

    else:

        print("Faltan", dias, "días para tu evento.")

main()