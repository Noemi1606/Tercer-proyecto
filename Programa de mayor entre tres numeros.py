# Pide al usuario tres números y muestra el mayor de ellos.
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print("El primer número es el mayor.")
elif num2 >= num1 and num2 >= num3:
    print("El segundo número es el mayor.")
else:
    print("El tercer número es el mayor.")
