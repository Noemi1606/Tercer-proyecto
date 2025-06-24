# Solicita tres números que representan longitudes y determina si pueden formar un triángulo (la suma de dos lados debe ser mayor que el tercero).
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Sí, las longitudes pueden formar un triángulo.")
else:
    print("No, las longitudes no pueden formar un triángulo.")
