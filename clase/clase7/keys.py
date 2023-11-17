d= {"a_key":42,22:"hello","another_key":[1,2,3]}

print(d)
print(d["a_key"],d[22])
d[34.5] = "a float number"
print(len(d))
print(list(d)) #si la "operas" como lista te da las keys


"""Si buscas una el valor asociado auna key y esta no existe te devuelve
KeyError, para evitarlo utilzar en vez de print(grades["Ana"]), 
utilizas grades.get(("Ana",None), si no encientra Ana te devuelve None"""

"""lo mismo con del grades["Ana"], grades.pop("Ana",None)"""

"""grades.uppdate(other_grades)
grades.clear
"""

"""e = diccioanrio 
e.key te da sus keys 
e.values te da el valor asociado a la llave
e.items te da una tupla formada por los valores
"""

def histogram(students_marks):
    hist= dict.fromkeys(range(11),)
    for mark in students_marks:
        hist[mark[1]] += 1
    return hist

def print_histogram(hist):
    for mark in hist:
        print(f"{mark}: {'*'*hist[mark]}")
