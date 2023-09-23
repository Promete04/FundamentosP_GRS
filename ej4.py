Ingresos_anuales = int(input ("Dime tus ingresos anuales\n"))

Nº_hijos = int(input ("¿Cuantos hijos tienes?\n"))

Ingreso_imponible = Ingresos_anuales/3
Impuesto_a_pagar = (Ingreso_imponible-600)/3 - 60 * Nº_hijos
print(f"Debes en impuestos: {Impuesto_a_pagar} euros")
