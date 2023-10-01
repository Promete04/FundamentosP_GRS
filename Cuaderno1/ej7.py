"""Python permite convertir elementos de un tipo en otro. Lleva a cabo las
siguientes conversiones y comenta los resultados:
texto_numerico = "45"
int (texto_numerico)
int ("Hola")
int (3.99999)
int(-3.99999)
float (34)
int("diez")"""

texto_numerico = "45"          
print(int (texto_numerico))    # Pasa el número de tipo "str" a "int"

"""print(int ("Hola")) no puede pasar un str a int si es texto. Un "literal" inválido"""

print(int (3.99999)) # trunca el numero 
print(int (-3.99999)) #trunca el número 

print(float (34)) #lo convierte en tipo float le añade un .0

"""print(int("diez")) no puede convertir diez en 10. Un "literal" inválido"""
