#Solicita la calificación de un estudiante (0-100) y determina si aprobó (mínimo 60) o reprobó.
calificacion = int(input("Ingresa tu calificación (0-100): "))

if calificacion >= 60:
    print("¡Aprobaste!")
else:
    print("Reprobaste.")
