def bisiesto(year):
    if year % 4 != 0: 
	    print(f"{year} no es bisiesto.")
    elif year % 4 == 0 and year % 100 != 0: 
	    print(f"{year} es bisiesto.")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: 
	    print(f"{year} no es bisiesto.")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
	    print(f"{year} es bisiesto.")

y = int(input("Ingrese el año para comprobar si es bisiesto o no: "))

bisiesto(y)