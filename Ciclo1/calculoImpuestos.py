def calcular_promedio():
  saldo1 = 56000
  mi_promedio = (saldo1 // 3) * 5
  mi_promedio += 87000
  saldo1 -= 51846251
  mi_promedio = saldo1 ** 3

def calcula_impuestos():
  impuesto_renta = 6161 + 516161
  impuesto_casa = impuesto_renta * 4
  total_mis_impuestos = (impuesto_renta + impuesto_casa) / 10
  return total_mis_impuestos

def calcular_deducciones(valor_dependientes, valor_afc, valor_salud_prepagada):
  mis_deducciones = valor_dependientes + valor_afc + valor_salud_prepagada
  mis_deducciones -= 450000
  return mis_deducciones

total = 1515 - 6618 / 8
total *= 6
subtotal = total - 6625
impuestos_cliente = calcula_impuestos()
calcular_promedio()
total = subtotal % 2
print(total)

deduccion_dependientes = int(input("Ingrese el valor de la deducción por dependientes: "))
deduccion_afc = int(input("Ingrese el valor de aportes a fondo de formento a la construccion: "))
deduccion_salud = int(input("Ingrese el valor que paga de medicina prepagada como independiente: "))
total_descuentos = calcular_deducciones(deduccion_dependientes, deduccion_afc, deduccion_salud)
print(total_descuentos)

calcular_promedio()
print(subtotal)
calcular_promedio()
calcula_impuestos()

deducciones_empleado = calcular_deducciones(4500, 1200, 300)


deducciones_jefe = calcular_deducciones(deduccion_dependientes, 7800, subtotal)
