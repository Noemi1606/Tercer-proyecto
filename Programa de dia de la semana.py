#Escribe un programa que solicite un número del 1 al 7 y muestre el día de la semana correspondiente (1 es lunes, 7 es domingo).
numero = int(input("Ingresa un número del 1 al 7: "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miércoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
else:
    print("Número fuera de rango. Debe ser del 1 al 7.")
