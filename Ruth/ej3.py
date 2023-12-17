"""Ejercicio 3. Creación y Análisis de Actas de notas. Crea un programa en Python que conste de
dos funciones:
• Creación de Actas: Escribe una función llamada crear_actas que no acepte
argumentos. Esta función solicitará al usuario que ingrese nombres de estudiantes
de uno en uno. Después de ingresar cada nombre, el usuario deberá introducir 3
notas (del 1 al 10) para ese estudiante. El proceso de introducir nombres y notas
continuará hasta que el usuario escriba "STOP" como nombre de un estudiante. La
función debe devolver un diccionario con los nombres de los estudiantes como
claves y sus listas de notas como valores.
• Análisis de Puntuaciones: Escribe una función llamada analizar_puntuaciones que
realice las siguientes tareas. La función debe aceptar como argumento un
diccionario donde las claves son los nombres de los estudiantes y los valores son
listas de puntuaciones (números) obtenidas por cada estudiante. Se debe calcular
la puntuación promedio para cada estudiante y devolver los resultados en un
nuevo diccionario, donde las claves son los nombres de los estudiantes y los valores
son sus puntuaciones promedio."""

def crear_actas()->dict:
    actas={}
    nombre=input("Introduce el nombre del alumno: ")
    notas=[]
    while nombre != "STOP":
        for i in range(3):
            nota=float(input("Introduce la nota: "))
            if nota<0 or nota>10:
                print("Nota no válida")
                nota=float(input("Introduce la nota: "))
            notas.append(nota)
        actas.update({nombre:[notas[0],notas[1],notas[2]]})
        nombre=input("Introduce el nombre del alumno: ")
    return actas

def analizar_puntuaciones(actas:dict)->dict:
    analisis={}
    for nombre,notas in actas.items():
        suma=0
        for nota in notas:
            suma+=nota
        analisis.update({nombre:suma/len(notas)})
    return analisis


actas=crear_actas()
analisis=analizar_puntuaciones(actas)
print(analisis)


