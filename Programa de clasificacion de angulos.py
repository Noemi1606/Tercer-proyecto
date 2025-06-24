#Solicita al usuario el valor de un ángulo en grados y determina si es agudo (<90°), recto (90°), obtuso (>90° y <180°) o llano (180°).
angulo = float(input("Ingresa el valor del ángulo en grados: "))

if angulo > 0 and angulo < 90:
    print("Es un ángulo agudo.")
elif angulo == 90:
    print("Es un ángulo recto.")
elif angulo > 90 and angulo < 180:
    print("Es un ángulo obtuso.")
elif angulo == 180:
    print("Es un ángulo llano.")
else:
    print("Ángulo fuera del rango válido (0° a 180°).")
