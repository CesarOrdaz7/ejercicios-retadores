municipios = []
habitantes = []

municipio1 = input("Ingresa municipio 1: ")
municipios.append(municipio1)
habitantes1 = int(input("Ingresa habitantes del municipio 1: "))
habitantes.append(habitantes1)

municipio2 = input("Ingresa municipio 2: ")
municipios.append(municipio2)
habitantes2 = int(input("Ingresa habitantes del municipio 2: "))
habitantes.append(habitantes2)

municipio3 = input("Ingresa municipio 3: ")
municipios.append(municipio3)
habitantes3 = int(input("Ingresa habitantes del municipio 3: "))
habitantes.append(habitantes3)

print(municipios)
print(habitantes)

suma_habitantes = sum(habitantes[:])
print(suma_habitantes)
promedio_habitantes = (suma_habitantes/len(municipios))
print(promedio_habitantes)