def lista_clases(clases):
  resultado = []
  for j in clases:
    if j not in resultado:
      resultado.append(j)
  return resultado


def laminas_faltantes_por_clase(indices, clases, clase_a_verificar):
  resultado = []
  for i in indices:
    if clases[i] == clase_a_verificar:
      resultado.append(i)
  return resultado


def laminas_faltantes(laminas_persona_1, laminas_persona_2):
  resultado = []
  for k in laminas_persona_1:
    if k not in laminas_persona_2:
      resultado.append(k)
  return resultado


def cantidad_laminas_cambiables(laminas_persona_1, laminas_persona_2):
  
  counter1 = 0
  counter2 = 0

  for k in laminas_persona_1:
    if k not in laminas_persona_2:
      counter1 += 1
  for k in laminas_persona_2:
    if k not in laminas_persona_1:
      counter2 += 1
  return (counter1 if counter1 < counter2 else counter2)