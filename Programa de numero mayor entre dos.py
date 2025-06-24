# Pide al usuario que ingrese dos números y determina cuál es el mayor o si son iguales.
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 > num2:
    print("El primer número es mayor.")
elif num2 > num1:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
