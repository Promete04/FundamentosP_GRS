""".Se desea conocer el importe en Libras Esterlinas (GBP) al cambio de una
cantidad en Euros (EUR). Escribe un programa que, a partir de una cierta
cantidad en euros y del tipo de cambio del día, muestre el equivalente en
libras teniendo en cuenta que la casa de cambio retiene una comisión del 2%
sobre el total de la operación.
"""

euros_a_cambiar = float(input("Cuantos euros desea cambiar?\n"))
cambio_dia = float(input("Cuanto vale la libra respecto del euro?\n ")) 
cambio = float((euros_a_cambiar*cambio_dia))
post_comision = round(float(cambio-cambio*0.02),2)
print(f"Tus {euros_a_cambiar} euros se convierten en {post_comision} libras esterlinas")
