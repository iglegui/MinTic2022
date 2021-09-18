def calcular_parafiscales():
  salario = int(input("Salario Persona: "))

  indice_base_cotizacion = 0.4
  porcentaje_salud = 0.125
  porcentaje_pension = 0.16
  porcentaje_arl = 0.00522

  if salario <= 1000000:
    base_cotizacion = 0
  else:
    base_cotizacion = salario * indice_base_cotizacion

  print(f"El ingreso base de cotizacion es {base_cotizacion} pesos colombianos")

  salud = base_cotizacion * porcentaje_salud
  print(f"El aporte a salud es {salud} pesos colombianos, este valor se calculó en base al ingreso base de cotización que es de {base_cotizacion} pesos colombianos")

  pension = base_cotizacion * porcentaje_pension
  print(f"El aporte a pension es {pension} pesos colombianos")
  
  arl = base_cotizacion * porcentaje_arl
  print(f"El aporte a ARL es {arl} pesos colombianos")

  parafiscales = salud + pension + arl
  print(f"El total de parafiscales es {parafiscales} pesos colombianos")

conteo = 0
cantidad_empleados = int(input("Cantidad Empleados: "))

while cantidad_empleados <= 0:
  cantidad_empleados = int(input("Total de Empleados: "))

  if cantidad_empleados <= 0:
    print("El numero ingresado es INVALIDO!!!!")


while conteo < cantidad_empleados:
  print(f"Conteo: {conteo}")
  #calcular_parafiscales()

  if conteo == 1000:
    print("La version gratuita de este software solo calcula hasta un maximo de 1000 empleados, si necesita calcular los parafiscales de mas empleados, ingrese su tarjeta de credito")
    break

  conteo += 1


# Instruccion A
# Instruccion B