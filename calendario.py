def nueva_agenda() -> list:
    """Creates an empty agenda"""
    agenda_vacia=[]
    return agenda_vacia

def encontar_telefono(a:list,name: str) -> str:
    """Returns the phone associated to the name.
    if name not in the agenda, returns None.
    """
    contacto = None
    if name in a:
        pos= a.index(name)
        contacto= a[pos][1]
    return contacto

def add_entry(a: list, name: str, phone:str, overwrite:bool=True)->bool:
    """Adds an entry to the agenda with the pair name, phone
    if overwrite is True and the name was existing, replaces the phone.
    if overwrite is False and the name was existing, returns False.
    if the entry was added or changed, returns True
    """
    encontrado= False
    if overwrite==True:
        if encontar_telefono(a,name) != None:
            pos= a.index(name)
            phone= a[pos][1]
            encontrado= True
        else:
            a.append([name,phone])
            encontrado= True
    else:
        if encontar_telefono(a,name) != None:
            encontrado= False
        else:
            a.append([name,phone])
            encontrado= True
    return encontrado

def delete_entry(a: list, name: str):
 """Deletes an entry from the agenda.
 if the name was not existing, does nothing."""
 if name in a:
     a.remove(name)

def contains(a: list, name: str) -> bool:
    """Returns true if the name is in the agenda.
    """
    if name in a:
        return True

def find(a: list, name: str)-> int:
    """Returns the position of the name in the agenda, -1 if not found.
    """
    pos=-1
    for i, entry in enumerate(a):
        if entry[0] == name:
            pos = i
    return pos

def print_agenda(a: list)-> None:
    """Prints the agenda, an entry per line."""
    for i in a:
        print(f"Nombre: {i[0]}, telefono: {i[1]}")
       
         
# Create and append tests:
a = nueva_agenda()
add_entry(a, "juan", "91886777")
add_entry(a, "pepe", "91555555")
add_entry(a, "ana", "914444444")
ok = add_entry(a, "ana", "999999", False)
if not ok:
 print("Error adding entry.")
ok = add_entry(a, "ana", "999999", True)
if not ok:
 print("Error adding entry.")
print_agenda(a)
# Contains and find tests:
print(contains(a, "juan"), contains(a, "antonio"))
print(find(a, "ana"), find(a, "antonio"))
print(encontar_telefono(a, "ana"), encontar_telefono(a, "antonio"))
# Delete testing:
delete_entry(a, "ana")
delete_entry(a, "antonio")
print(encontar_telefono(a, "ana"))


#arreglarlos index anidados