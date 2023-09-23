salario_base = 2000
ventas = int(input("Ventas hechas\n"))
bonus = float(ventas*0.03)
bruto = float(salario_base+bonus)
neto = bruto-bruto*0.32

print(f"Tu salario neto es de {neto} euros")