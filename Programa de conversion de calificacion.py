#Solicita la calificación numérica de un estudiante (0-100) y conviértela en una letra:
calificacion = int(input("Ingresa la calificación (0-100): "))

if calificacion < 0 or calificacion > 100:
    print("Calificación inválida. Debe estar entre 0 y 100.")
else:
    if calificacion >= 90:
        print("Calificación: A")
    elif calificacion >= 80:
        print("Calificación: B")
    elif calificacion >= 70:
        print("Calificación: C")
    elif calificacion >= 60:
        print("Calificación: D")
    else:
        print("Calificación: F")
