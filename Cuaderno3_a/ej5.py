"""Una universidad acaba de modificar su sistema de representación de la calificación
de los alumnos. A partir de ahora, se calificarán como “A” las notas mayores o
iguales a 8,5, “B” las mayores o iguales a 6,5, “C” las calificaciones mayores o
iguales a 5, “D” las calificaciones mayores o iguales a 3,5, y “F” todas las demás.
Programa una función que reciba una calificación numérica y retorne la letra con la
nueva calificación, luego pruébala con valores introducidos por el usuario. Tal vez
sea buena idea basarte en el ejercicio resuelto número 1 pero, a diferencia de lo
que se hace allí (se controla la validez con una precondición), asegúrate de que la
calificación introducida es válida."""

 
x= float(input("Introduzca una nota: "))

def clasificar(x:float)-> str:
    if 0<x<=10:
        if x >= 8.5:
            y = "A"
        elif 6.5<=x<8.5:
            y= "B"
        elif 5<= x < 6.5:
            y= "C"
        elif 3.5 <= x < 5:
            y = "D"
        else: 
            y = "F"
    else:
        y= "Valor no valido"
    return y

print (clasificar(x))