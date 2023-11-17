"""Crear una función que compruebe si dos cadenas de caracteres son iguales, sin
comparar las cadenas completas y sin usar el operador in"""


def comparar_cadenas(cadena1, cadena2):
    if len(cadena1) != len(cadena2):
        return False
    else:
        for i in range(len(cadena1)):
            if cadena1[i] != cadena2[i]:
                return False
        return True