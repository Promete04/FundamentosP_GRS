"""El salario base de un vendedor es de 2.000 euros mensuales. A este salario
se le suma un 3% de comisión sobre el total de las ventas que ha realizado,
pero al total obtenido hay que descontarle un 32% del IRPF. Escribe un
programa que, a partir del importe de las ventas que ha realizado el vendedor
durante el último mes y escriba el salario neto que cobrará ese mes.
"""

salario_base = 2000
ventas = int(input("Ventas hechas\n"))
bonus = float(ventas*0.03)
bruto = float(salario_base+bonus)
neto = bruto-bruto*0.32

print(f"Tu salario neto es de {neto} euros")