"""Escribir una función que permita mostrar los caracteres de una cadena del final
al principio, pero nunca mostrando la letra “a”. Ejemplo: si la entrada es “barco
amarillo”, la función devolverá: “ollirm ocrb”. """

def inversa_anti_a (texto:str)->str:
    texto= texto.split()
    nuevo_texto=[]
    for palabra in texto:
        if "a" in palabra:
            palabra= palabra.replace("a","")
        nuevo_texto.append(palabra)
    nuevo_texto= " ".join(nuevo_texto)
    nuevo_texto= nuevo_texto[::-1]
    return nuevo_texto
texto= "barco amarillo"
print(inversa_anti_a(texto))

        