def calculoFecha(numero):

    if (1 <= numero <= 31):
        print(f"El dia {numero} corresponde al {numero} de Enero de 2021.")
    elif (32 <= numero <= 59):
        dia = numero - 31
        print(f"El dia {numero} corresponde al {dia} de Febrero de 2021.")
    elif (60 <= numero <= 90):
        dia = numero - 59
        print(f"El dia {numero} corresponde al {dia} de Marzo de 2021.")
    elif (91 <= numero <= 120):
        dia = numero - 90
        print(f"El dia {numero} corresponde al {dia} de Abril de 2021.")
    elif (121 <= numero <= 151):
        dia = numero - 120
        print(f"El dia {numero} corresponde al {dia} de Mayo de 2021.")
    elif (152 <= numero <= 181):
        dia = numero - 151
        print(f"El dia {numero} corresponde al {dia} de Junio de 2021.")
    elif (182 <= numero <= 212):
        dia = numero - 181
        print(f"El dia {numero} corresponde al {dia} de Julio de 2021.")
    elif (213 <= numero <= 243):
        dia = numero - 212
        print(f"El dia {numero} corresponde al {dia} de Agosto de 2021.")
    elif (244 <= numero <= 273):
        dia = numero - 243
        print(f"El dia {numero} corresponde al {dia} de Septiembre de 2021.")
    elif (274 <= numero <= 304):
        dia = numero - 273
        print(f"El dia {numero} corresponde al {dia} de Octubre de 2021.")
    elif (305 <= numero <= 334):
        dia = numero - 304
        print(f"El dia {numero} corresponde al {dia} de Noviembre de 2021.")
    elif (335 <= numero <= 365):
        dia = numero - 334
        print(f"El dia {numero} corresponde al {dia} de Diciembre de 2021.")
    

numeroDia = int(input("Ingrese un número en el rango de 1 a 365: "))

while numeroDia <= 0 or numeroDia > 365:
  numeroDia = int(input("Ingrese un número entero desde 1 hasta 365: "))

  if numeroDia <= 0 or numeroDia > 365:
    print("El número ingresado es INVALIDO!!!!")

calculoFecha(numeroDia)