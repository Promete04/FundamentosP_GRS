"""El Barn es una unidad de superficie muy utilizada en la física de partículas,
que equivale a 10-28 m². Para ilustrar su tamaño, ten en cuenta que un Barn
es, aproximadamente, el área de la sección transversal del núcleo de un
átomo de uranio. Programa dos funciones, una que permita convertir
unidades en m² a Barns, y su inversa."""

b=float(input("Barns\n"))
m=float(input("Metros cuadrados\n"))
q=10^28
p=1/q


def f(m:float,p:float): #p es la proporcion de barns por metro
    return(m*p)

def g(b:float,q:float): #q es la proporcion de metros por barns
    return(b*p)

print(str(g(b,p))+" metros cuadrados")
print(str(f(m,q))+" barns")



