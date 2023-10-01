"""Una industria mantiene una flota de camiones para repartir productos. En
cada viaje, el conductor anota la distancia recorrida en kilómetros, los litros
de gasoil utilizados, el coste del litro de gasoil y los demás costes de
mantenimiento del camión (agrupados). Como parte del proceso de
contabilidad, el controlador necesita calcular, para cada camión y para cada
viaje, los kilómetros recorridos por litro, el coste total del viaje y el coste total
por kilómetro (incluidos los gastos de mantenimiento). Diseña un programa
sencillo que lleve a cabo estos cálculos para un camión en un viaje.
"""

Dist = int(input("Kilometros recorridos?\n"))
L_gastados = int(input("Litros de combustible gastados?\n"))
Precio_combustible = float(input("Precio del litro de combustible?\n"))
Gastos_camion = int(input("Coste del mantenimineto del camión?\n"))

Km_Litro = Dist/L_gastados
Costes = float((Precio_combustible + Gastos_camion))
Km_precio = Costes/Dist

print(f"Kilómetros recorridos por litro: {Km_Litro} Km/L\nCoste total del viaje: {Costes}€\nCoste total por kilómetro: {Km_precio}€")