"""Escriba un programa que “codifique” una frase modificando todas las vocales
según el siguiente código: a por 4, e por 3, i por 1, o por 0 y u por el símbolo #.
Por ejemplo, la frase: “Un perro del hortelano”, deberá devolverse: “#n p3rr0 d3l
h0rt3l4n0”."""

def codificador(texto: str)->str:
    vocales= "aeioU" #U mayus pq no quiero poner upper y demas...
    texto_codificado=[]
    texto= texto.split()
    for palabra in texto:
        for vocal in vocales:
            if vocal in palabra:
                palabra= palabra.replace("a","4")
                palabra= palabra.replace("e","3")
                palabra= palabra.replace("i","1")
                palabra= palabra.replace("o","0")
                palabra= palabra.replace("U","#") 
        texto_codificado.append(palabra)
    texto= " ".join(texto_codificado)
    return texto

texto= "Un perro del hortelano"
print(codificador(texto))