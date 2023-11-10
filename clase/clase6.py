import random

"""def fill_zeroes_average3(coll):
    avg= sum(coll)/len(coll)
    new_coll = coll.copy()
    for idx, elem in enumerate(coll):
        if elem == 0:
            new_coll[idx] = avg
            return new_coll
numbers = random.numbers(2,10)
print(numbers)
new_numbers = fill_zeroes_average3(numbers)
print(new_numbers)"""


"""Para evitar que las listas se modifiquen se puede asignar a cada valor detro de cada valo de la lista origina una variable
 y crear una lista con ellas, el problema reside en lo acotado que esté ell problema"""

"""la tuplas son SOLO inmutables al primer nivel"""

t= ([1,2],2,3)
t[0][0]= 99
print (t)

"""para evitar problemas utilizar tmb el for idx, entry in enumerate()..., entry es la lista dentro de la lista"""

def filtrar_ceros (numbers):
    for idx,elem in enumerate(numbers):
        if elem == 0:
            numbers.pop(idx)
        
    numbers = random.randomnumbers(2,10)
    print(numbers)
    new_numbers = filtrar_ceros(numbers)




"""tmb podemos crear una lista lista_nueva=[] y irle poniendo con .apend los numeros distintos de 0"""#lo mejor


"""o se usa filter""" 
#filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6]
def is_even(n):
    return n % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]



ones = [1] * 10
zeros = [0] * 5
def interleave_lists(seq1,seq2):
    result = []
    for i in range(max(len(seq1), len(seq2))):
        if i < len(seq1):
            result.append(seq1[i])
        if i < len(seq2):
            result.append(seq2[i])
    return result

print(interleave_lists(ones,zeros))
print(ones)
print(zeros)

