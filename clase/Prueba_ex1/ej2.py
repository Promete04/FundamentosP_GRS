
n= int(input("Dime el orden de la matriz\n"))
mid= n//2

def cruz(n:int) -> str:
    for  i in range (mid):
        print(" " * mid *3 + " * ")
    print(" * " * n)
    for  i in range (mid):
        print(" " * mid *3+ " * ")
cruz(n)


def aspa(n:int)-> str:
    for i in range(n):
        for j in range(n):
            if i==j or i+j == n-1:
                print(" * ",end= "")
            else:
                print("  ",end= "")
        print()
aspa(n)         