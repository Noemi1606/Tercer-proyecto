# Escribe un programa que solicite un número al usuario y determine si es positivo, negativo o cero.
n = float(input("Ingresa un número: "))
if n > 0:
    print("Es positivo.")
elif n < 0:
    print("Es negativo.")
else:
    print("Es cero.")
