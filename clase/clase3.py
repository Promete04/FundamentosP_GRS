
"""booleanos = [False, True]

# Tabla de verdad de or

print('x\ty\tx or y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x or y, sep = '\t')

print()

# Tabla de verdad de and

print('x\ty\tx and y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x and y, sep = '\t')
        
print()
"""

x=10
if x>10:
    x=x+1
    print(x)
else:   #x <= 10
    if x!= 0:   #para evitar el 3/0
        x=3/x
    else:
        x=3

    print(x)
print(x)


