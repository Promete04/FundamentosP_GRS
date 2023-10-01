"""Haz la tabla de verdad de p and not q or r teniendo en cuenta el orden de
prelación de los operadores en Python. """

si_o_no = [True,False]

print("p\tq\tr\tp nand q or r\t")   #creamos la parte superior de la tabla con los datos
print("-"*37)   #colocamos la barra
for p in si_o_no:
    for q in si_o_no:
        for r in si_o_no:
            print(p, q, r, p and not q or r, sep = "\t")

    