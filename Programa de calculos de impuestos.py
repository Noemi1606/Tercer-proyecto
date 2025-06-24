#Pide al usuario su salario mensual y aplica los siguientes impuestos:
#Menos de 10,000: 0%
#Entre 10,000 y 30,000: 10%
#Más de 30,000: 20%

salario = float(input("Ingresa tu salario mensual: "))

if salario < 10000:
    impuesto = 0
elif salario <= 30000:
    impuesto = salario * 0.10
else:
    impuesto = salario * 0.20

print(f"Impuesto a pagar: ${impuesto:.2f}")

