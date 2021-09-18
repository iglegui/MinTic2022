def ordenInverso(palabra1):
    palabraAlReves =''.join(reversed(palabra1))
    print(palabraAlReves) 

palabra = str(input("Ingrese una palabra: "))

print(f"{palabra} al revés es: ", end='')
print(ordenInverso(palabra), end='')