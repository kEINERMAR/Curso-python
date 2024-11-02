def calcular_pago(horas_trabajadas, valor_por_hora):
    return horas_trabajadas * valor_por_hora

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
valor_por_hora = float(input("Ingrese el valor por hora: "))

total_a_pagar = calcular_pago(horas_trabajadas, valor_por_hora)

print(f"El monto total a pagar es: ${total_a_pagar:.2f}")
