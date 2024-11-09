empleados = [
    {"nombre": "Juan", "horas_laborales": 40, "horas_extras_nocturnas": 5},
    {"nombre": "María", "horas_laborales": 35, "horas_extras_nocturnas": 3},
    {"nombre": "Pedro", "horas_laborales": 42, "horas_extras_nocturnas": 6},
    {"nombre": "Laura", "horas_laborales": 38, "horas_extras_nocturnas": 4}
]
print("|Nombre     | Horas laborales | Horase extras nocturnas|")
print("|-----------|-----------------|------------------------|")

for empleado in empleados:
    print(f"|{empleado['nombre']:^10} | {empleado['horas_laborales']:^15} |  {empleado['horas_extras_nocturnas']:^20}  |")