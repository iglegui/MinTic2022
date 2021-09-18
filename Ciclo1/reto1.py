distance = int(input())

peso_carga_util = int(distance * 2 + 4)

combustible = int(1/5 * (distance + peso_carga_util))

cantidad_cohetes = ""

if combustible <= 20:
    cantidad_cohetes = "uno"
elif combustible <= 30:
    cantidad_cohetes = "dos"
elif combustible <= 50:
    cantidad_cohetes = "tres"
elif combustible > 50:
    cantidad_cohetes = "cuatro"


print(str(distance) + " " + str(peso_carga_util) + " " + str(combustible))
print(cantidad_cohetes)


