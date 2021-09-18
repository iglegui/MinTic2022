tieneLicencia = bool(int(input("Indique si tiene licencia: (Si=1 No=0) ")))
cantidadMultas = int(input("Indique si tiene multas: (Si=1 No=0) "))
grados_alcohol = float(input("Indique los grados de alcohol: "))
velocidad = float(input("Indique la velocidad: "))
papelesEnRegla = bool(int(input("Indique si tiene papeles en regla: (Si=1 No=0) ")))
tieneVidrioPolarizados = bool(int(input("Indique si tiene vidrios polarizados: (Si=1 No=0) ")))
edad = int(input("Ingrese la edad: "))

puede_conducir = bool(tieneLicencia == True and cantidadMultas == 0 and grados_alcohol == 0 and 
                    0 < velocidad <= 80 and papelesEnRegla == True and tieneVidrioPolarizados == False and
                    75 > edad >= 18)

print(puede_conducir)