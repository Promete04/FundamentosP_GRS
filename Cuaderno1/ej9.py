"""Por consideraciones históricas, un programador suele interpretar que los
identificadores i, j, k, l, m, n corresponden a datos enteros, mientras que a,
b, c, x, y, z son identificadores que suelen asociarse con valores reales.
Escribe un programa que, a partir de 3 números reales que inicializarás,
calcule su media, suma total y producto total y muestre todos estos datos por
pantalla."""


Nº1 = float(input("Nº1:\n"))
Nº2 = float(input("Nº2:\n"))
Nº3 = float(input("Nº3:\n"))

Media = float((Nº1+No2+No3)/3)
Suma = float(Nº1+No2+No3)
Producto = float(Nº1*No2*No3)

print(f"La media de los números es: {Media}\n La suma total de los números es: {Suma}\n El producto totas de los números es: {Producto}")