"""Implementa un programa que, dado un número finito de fechas, nos permita
buscar una fecha por año, mes o día, así como la ordenación de las mismas
por año. Nota: emplea el método de búsqueda binaria.
"""
fechas = [
    {"año": 2018, "mes": 8, "día": 14},{"año": 2017, "mes": 7, "día": 12},
    {"año": 2016, "mes": 6, "día": 9},{"año": 2015, "mes": 5, "día": 6},
    {"año": 2014, "mes": 4, "día": 4},{"año": 2013, "mes": 1, "día": 1},
]

def bin_search(lista:list, año:int, mes:int, dia:int, bot=0, top=None):
    if top is None:
        top = len(lista) - 1

    if bot <= top:
        mid = (top + bot) // 2
        if (año == lista[mid]["año"] and mes == lista[mid]["mes"] and dia == lista[mid]["día"]):
            return lista[mid], True
        elif (año > lista[mid]["año"] or (año == lista[mid]["año"] and mes > lista[mid]["mes"]) or (año == lista[mid]["año"] and mes == lista[mid]["mes"] and dia > lista[mid]["día"])):
            return bin_search(lista, año, mes, dia, bot, mid - 1)
        else:
            return bin_search(lista, año, mes, dia, mid + 1, top)
    else:
        return None     

print(bin_search(fechas, 2013, 1, 1))

