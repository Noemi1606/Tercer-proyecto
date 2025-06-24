#Solicita el precio de un producto y aplica descuentos según el monto:
#Menos de $50: sin descuento
#Entre $50 y $100: 5%
#Más de $100: 10%

precio = float(input("Ingresa el precio del producto: "))

if precio < 50:
    descuento = 0
elif precio <= 100:
    descuento = precio * 0.05
else:
    descuento = precio * 0.10

precio_final = precio - descuento

print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Precio final: ${precio_final:.2f}")
