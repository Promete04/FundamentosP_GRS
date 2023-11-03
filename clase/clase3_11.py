"""print([1,2,3]*3)

numbers = list(range(0,20+1))

print(numbers[::-2])

slice([1,3,7,8,9,6,4,7,2],1,4)


some_index=numbers.index(1)

print(some_index)


def __index(seq, o,i=0):
    enc = False
    while not enc and i < len(seq):
        enc = seq[i] == o
        i +=1
    return i -1 if enc else None
some_index = __index(numbers,3)
print(some_index)
print(__index(numbers,3,some_index+1))
"""        

