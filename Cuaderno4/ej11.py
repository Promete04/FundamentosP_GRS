"""Un texto contiene comandos en forma de frases separadas por puntos. En cada
frase, la primera palabra contiene el código de la operación y la última el
resultado. Ejemplo:
SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200. Etc.
Cree una lista de parejas [código-resultado] utilizando como entrada un texto
con el formato indicado. """

def lista_comandos(texto:str)->list:
    operaciones= texto.split(". ")
    comandos = []
    for i in range(len(operaciones)):
        comandos.append(operaciones[i].split(' '))
    lista = []
    for i in range(len(comandos)):
        lista.append([comandos[i][0], comandos[i][-1]])
    lista.pop()
    return lista

texto ="SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200. RESTA 20 10 10. "
print(lista_comandos(texto))
    
    
    

texto= "SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200. "
print(lista_comandos)