"""Explica lo más brevemente posible qué hace la expresión: a=a==False,
sabiendo que la variable a está inicializada a un valor bool (sea cual sea).
Explica también qué pasaría si a no hubiera sido previamente inicializado."""

a=False

a=a==False
print(a)

"""Compara el valor de a respecto a de False. Si son el mismo, dará como resultado true y en el caso contrario false"""

a=True

a=a==False
print(a)

"""Si no inicializamos previamente "a"  nos dara un error----> NameError: name 'a' is not defined"""
