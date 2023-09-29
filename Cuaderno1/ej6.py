Dist = int(input("Kilometros recorridos?\n"))
L_gastados = int(input("Litros de combustible gastados?\n"))
Precio_combustible = float(input("Precio del litro de combustible?\n"))
Gastos_camion = int(input("Coste del mantenimineto del camión?\n"))

Km_Litro = Dist/L_gastados
Costes = float((Precio_combustible + Gastos_camion))
Km_precio = Costes/Dist

print(f"Kilómetros recorridos por litro: {Km_Litro} Km/L\nCoste total del viaje: {Costes}€\nCoste total por kilómetro: {Km_precio}€")