import sys
type(sys.argv)
nombre=sys.argv[1]
apellido=sys.argv[2]

print(f"Mi nombre es {nombre}")
print(f"Mi apellido es {apellido}")
print(f"El nombre de este archivo es {sys.argv[0]}")
#se ingresa en terminal: python argumentos.py(nombre del archivo) Mauricio(argumento1) Lecaros(argumento2)