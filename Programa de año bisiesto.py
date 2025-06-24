#Solicita al usuario un año y determina si es bisiesto o no. (Es bisiesto si es divisible por 4, pero no por 100, salvo que también sea divisible por 400).
anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
