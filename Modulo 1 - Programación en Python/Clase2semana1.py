#import sys
#estructura de datos
#Listas
#a=[1,2,3,"hola",8]
#indice      0     ,   1    ,    2
#print(type(Alumnos))
#indice... 0 - n-1 ej: Angelina sería el 1 -> por lo tanto es de índice 0(posición en que se encuentra el elemento)
#print(Alumnos[0]) singifica que se asocia al índice 0 Angelina
#print(type(Alumnos[0])) el type asume el elemento que contiene la lista, es decir, en este caso str.
#print(Alumnos[-1]) comienza desde el final de los elementos de la lista
#print(a[a[0]]) = 2  Se resuelve de dentro hacia fuera es decir a[0]=1 y el a[1]=2
#print(a[4])
#lista ARGV
#print(a)
#print(sys.argv) #en terminal escribir comando "dir"
#para inseretar elementos a las variables
#a.append("marco")
#a.append("marco")
#print(a)
#a.insert(2,"Mauri")
#print(a)
#eliminar elementos
#a.pop() #elimina siempre el último elemento (es decir el -1), pero queda como un elemento individual
#print(a)
#a(0)=11 #actualizar
#print(a)
#print(len(a)) numero de elementos de una lista
notas={"Mauricio":7,"Antonia":6}
print(notas)
notas["Ignacio"]=5
#print(type(notas))
#para borrar se ocupa del