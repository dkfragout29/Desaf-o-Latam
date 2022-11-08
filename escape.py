import math
"""
La velocidad de escape de un planeta se define como la mínima velocidad necesaria para
salir de un planeta venciendo la gravedad.
La velocidad de escape se calcula mediante la siguiente fórmula:
𝑉𝑒= 2𝑔𝑟
Ve: corresponde a la Velocidad de Escape en [m/s].
g: corresponde a la constante gravitacional en [m/s2].
r: Corresponde al radio del planeta en [m].

1. Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().

2. El programa debe especificar claramente el formato en el que se deben entregar los
datos de entrada con instrucciones apropiadas.
(5 Puntos)
Ej:
“Ingrese el radio en Kilómetros:”, --> 6371 km
“Ingrese la constante g: ” 9.8 [m/s2]
La respuesta del programa también debe mostrarse con un texto apropiado:
Ej:
“La velocidad de Escape es 11174.6 [m/s]”

"""
gravedad=float(input("Ingrese la constante gravitacional: "))
radio_planeta=int(input("Ingrese el radio del planeta en kilómetros: "))
velocidad_escape=math.sqrt(2*gravedad*radio_planeta*1000) #velocidad_escape=(2*gravedad*radio_planeta*1000)**(1/2)
print(f"La velocidad de Escape es {velocidad_escape:.1f} [m/s]")