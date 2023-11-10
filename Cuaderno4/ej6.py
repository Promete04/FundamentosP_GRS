"""Implementar una función que compruebe si una palabra es un palíndromo.
Atención, no hagas más trabajo del necesario. """

def palindromo(vocablo:str)->bool:
    inversa= vocablo[::-1]
    result=False
    if vocablo == inversa:
        result=True
    return result

print(palindromo("neuquen"))
print(palindromo("casa"))
