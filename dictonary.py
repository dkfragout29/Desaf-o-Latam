elficio={
    "clase":"Mago",
    "tipo":"Hielo",
"raza":"Elfo de sangre",
"nivel":39}
print(elficio["nivel"])
elficio["nivel"]=49
print(elficio["nivel"])
print(elficio.keys())
print(elficio.values())

#convertir un diccionario en una lista. funcion .items()
print(list({"k1":5, "k2":7}.items()))
#convertir lista en diccionario
print(dict([('k1', 5), ('k2', 7)]))