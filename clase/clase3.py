"""
booleanos = [False, True]

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


a=input("Cuanto mide un lado?\t" )
b=input("Cuanto mide otro lado?\t " )
c=input("Cuanto mide el último lado?\t")
def classify_triangle(a,b,c)-> str:
    if a == b == c:
        return("Es equílátero")
    elif a==b or b==c or c==a:
        return("Es isósceles")
    else:
        return("Es escaleno")
print (classify_triangle(a,b,c))


print(list(range(10)))
print(list(range(11)))
print(list(range(0,30,5)))
print(list(range(0,10,3)))
print(list(range(0,-10,-1)))

for i in range(3):
    print (i)

for i in range(0):
    print(i)

def par(x:int):
    return x%2 ==0

acc = 0 
for i in range(10):
    if par(i):
        acc +=i
print(acc) #acc = acc+i


def factorial (n:int) -> int:
    result = 1
    for i in range(1, 1+n):
        result = result * i
    return result
print(factorial(5))
"""

import random
some = 0
NTRIALS = 10
NSIDES = 6

for i in range(NTRIALS):
    some= some+random.randint(1,NSIDES)
print(some/NTRIALS)

