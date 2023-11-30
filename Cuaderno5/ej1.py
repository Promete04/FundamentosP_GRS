"""Piensa en las estructuras de datos que permitan almacenar información sobre personas
con objeto de hacer un estudio estadístico. Así, se deberá almacenar el nombre, sexo y
edad de cada persona. Programa posteriormente una función para leer por teclado
datos relativos a una persona y otra que muestra dichos datos por pantalla."""

vault={}

def storage(vault:dict,nombre:str,sexo:int,edad:str)->dict:
    info= (sexo, edad)
    user={nombre:info}
    vault.update(user)

#n= int(input("Cuantos usuarios quieres introducir? "))


n=10
def introduce_user(n)->str:
    for i in range(n):
        nombre= input("Nombre del sujeto? ")
        sexo= input("Sexo del sujeto? ")
        edad= input("Edad del sujeto? ")
        storage(vault, nombre, sexo, edad)

introduce_user(n)

def find_info(vault,sujeto)->str:
    if sujeto in vault:
        result= vault[sujeto]
    else:
        result= "No information found for this name."
    return result

sujeto= "Paco"
print(find_info(vault))

