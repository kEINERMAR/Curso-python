
def calificacion(promedio):
    if 90 <= promedio <= 100:
        return "superior"
    elif 80 <= promedio < 90:
        return "alto"
    elif 70 <= promedio < 80:
        return "basico"
    elif 60 <= promedio < 70:
        return "bajo"
    elif 0 <= promedio < 60:
        return "insuficiente"
    else:
        return "promedio invalido"

def Dpromedio():
    
    nombre = input("Ingrese el nombre del estudiante: ")

    
    nota1 = float(input(f"Ingrese nota primer periodo de {nombre}: "))
    nota2 = float(input(f"Ingrese nota segundo periodo de {nombre}: "))
    nota3 = float(input(f"Ingrese nota tercer periodo de {nombre}: "))

   
    promedio = (nota1 + nota2 + nota3) / 3

   
    calificacionn = calificacion(promedio)

   
    print(f"\n{nombre} tiene un promedio de {promedio:.2f}. Su calificación final es: {calificacionn}")


Dpromedio()

