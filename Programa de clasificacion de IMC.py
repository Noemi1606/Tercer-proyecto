#Solicita el peso (kg) y la altura (m) de una persona, calcula su Índice de Masa Corporal (IMC = peso / altura²) y clasifícalo:
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc <= 24.9:
    print("Normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")
