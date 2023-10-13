"""for i in range (2,11,2):
    for j in range (1,11):
        print (i, "x", j, "=", i * j)
    print ("--------------")


heigh = int(input("Altura?\n"))

for i in range (1, heigh+1):
    for j in range (i):
        print("*", end= " ")
    print()

for i in range (1, heigh+1):
    print(i*"* ")  

n=max([22,56,87,45,258,6985,25,12,4,1,5,2,3,6,52,8,])
print(n)
 

def max_(xs:list)-> list:
    current_max = xs[0]
    for x in xs:
        if x> current_max:
            current_max = max
    return (current_max)


def get_random_numbers(n,lower,upper):
    return

def is_inside(x,xs):
    return x in xs

#esto no, mejor while.

def is_inside(x,xs):
    found = False
    index = 0
    while not found and index < len(xs):
        found = x in xs
        index = index+1
    return found

numbers = get_random_numbers (10,1,15)
print (is_inside(12,numbers))
print(numbers)


num_sec = 20
adivinado = False
while not adivinado:
    ...

"""

try: 
    some_integer = int(input("Enter a integer: "))
except ValueError:
    print("Thats not a valid number. Try again...")
print(some_integer)

#No sustituir if con while






