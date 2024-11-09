
tarifas = {
    "Bronce": 5000,
    "Plata": 3500,
    "Oro": 2000
}
def calcular_factura(nombre, horas):
    
    if 0 < horas <= 15:
        categoria = "Bronce"
        tarifa = tarifas["Bronce"]
    elif 15 < horas <= 30:
        categoria = "Plata"
        tarifa = tarifas["Plata"]
    else:
        categoria = "Oro"
        tarifa = tarifas["Oro"]
    
    total = horas * tarifa
    
    print(f"{nombre} estuvo en el gimnasio {horas} horas en el mes.\n"
          f"Por lo tanto, se le aplica factura de suscripción {categoria}, "
          f"por un valor de {tarifa} / hora.\n"
          f"{horas} * {tarifa} = ${total}")
    return total

# Factura para Juan
calcular_factura("Juan", 25)
print() 

# Factura para Mary
calcular_factura("Mary", 10)
print()

# Factura para Daniel
calcular_factura("Daniel", 35)
