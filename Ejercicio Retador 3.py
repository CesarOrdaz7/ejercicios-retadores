peso_cemento_kg = 40
peso_yeso_kg = 30

capacidad_camion_kg = 3254

costales_cemento = int(input("Ingrese el numero de costales de cemento: "))
costales_yeso = int(input("Ingrese el numero de costales de yeso: "))

peso_total_kg = costales_cemento * peso_cemento_kg + costales_yeso * peso_yeso_kg

print(f"El peso total en kg es de: {peso_total_kg}")

print(f"¿Se puede realizar el envio?: {peso_total_kg >= capacidad_camion_kg*0.5 and peso_total_kg <= capacidad_camion_kg}")