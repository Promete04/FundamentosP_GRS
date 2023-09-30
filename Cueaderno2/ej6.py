"""El antiguo sistema anglosajón de unidades sigue en vigor en muchos lugares
y su uso es frecuente en algunos contextos. Programa una función que
determine el número de pintas que contiene una cierta cantidad de líquido
expresada en mililitros, sabiendo que 1 pinta (pt) = 473,176473 ml."""

ml= float(input("Cuantos mililitros tienes?\n"))

def f(ml:float):
    return(ml/473.176473)
print(str(f(ml))+" pintas")