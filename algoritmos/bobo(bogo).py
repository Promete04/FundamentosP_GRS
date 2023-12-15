import random

def bogo_sort(a):
    n = len(a)
    while (is_sorted(a)== False):
        shuffle(a)

def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i] 

a = [ 0, 5, 7, 6, 9, 8]
bogo_sort(a)
print(a)