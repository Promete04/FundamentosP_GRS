""". Los profesores solemos utilizar dos decimales cuando trabajamos con las
notas parciales de un alumno, pero en las actas se desea calificar con puntos
enteros o medios (es decir: 0 / 0.5 / 1 / 1.5 /… / 9.5 /10). Combinando
operaciones y funciones enteras y en coma flotante, encuentra una fórmula
general que convierta una nota con dos decimales a la calificación
correspondiente en el acta e implementa una función que la utilice para convertir cualquier nota. Pista (aunque te parezca obvio, esta es la pista): 0.5
(que es lo que quiero conseguir) es la mitad de 1.
Tu propuesta debe funcionar para todos los casos de prueba que adjuntamos.
Nota original En acta
8,89 9,0
8,50 8,5
8,45 8,5
8,24 8,0
Error frecuente: considerar que necesitas una instrucción if. No es necesario
utilizarlo y te pedimos de hecho que no lo utilices."""

num=float(input("Número a redondear?\n"))

def f(num):
    return(round(num*2)/2)
print(f(num))

print(f(8.89))
print(f(8.50))
print(f(8.45))
print(f(8.24))