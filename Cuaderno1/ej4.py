"""Escribe un programa en Python que calcule el impuesto que debe pagar un
contribuyente a partir de sus ingresos anuales y el número de hijos. El
impuesto a pagar es un tercio del ingreso imponible, siendo este último igual
a los ingresos totales menos una deducción personal de 600€ y otra deducción
de 60€ por hijo"""

Ingresos_anuales = int(input ("Dime tus ingresos anuales\n"))

Nº_hijos = int(input ("¿Cuantos hijos tienes?\n"))

Ingreso_imponible = Ingresos_anuales/3
Impuesto_a_pagar = (Ingreso_imponible-600)/3 - 60 * Nº_hijos
print(f"Debes en impuestos: {Impuesto_a_pagar} euros")
