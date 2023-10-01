"""Cuando construyamos programas para su comercialización mimaremos el
aspecto de la entrada y la salida (lo que en conjunto se llama interfaz de
usuario). Posiblemente pondremos al principio un rótulo, indicando al
usuario qué aplicación está usando, rótulo que irá centrado en la pantalla y
subrayado, dejando una línea en blanco por encima y otra por debajo. Así:
Aplicación de combinatoria
=================
 Escribe el siguiente subprograma:
def centrarRotulo (rotulo):
 string--> None
 OBJ: centra rótulo, subrayado con signos =, +línea encima y debajo
 
 tam=len(rotulo)
 lado=((72-tam)//2)-1 # 72 columnas suele ser ancho de la pantalla
 print()
 print(' '*lado,rotulo)
 print(' '*lado , '='*tam , end='\n')
#Probador
frase = 'Don Quijote de la Mancha'
centrarRotulo(frase) # distinto nombre
centrarRotulo('Cervantes') # constante
rotulo = 'El famoso hidalgo don Quijote de la Mancha' # mismo nombre
centrarRotulo(rotulo)
Ejecútalo en Pythontutor (http://www.pythontutor.com/visualize.html)
Nota: Este ejercicio pretende que visualices:
▪ Que la declaración de un subprograma no es ejecutable
▪ Que los argumentos reales no tienen por qué llamarse igual, ni diferente
que los argumentos formales.
▪ De hecho, los argumentos reales de entrada pueden ser una constante
▪ Aprecia que cada pieza de código tiene su propia tabla de símbolos (frames
en Python tutor). En un momento de la ejecución hay dos variables con el
mismo nombre y distinto contenido."""