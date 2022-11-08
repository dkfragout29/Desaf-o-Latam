import math
#proteinas y carbohidratos aportan 4 calorias/gramo, mientras que las grasas aportan 9 calorias/gramo
proteina=float(input("Ingrese los gramos de proteina: "))
carbohidratos=float(input("Ingrese los gramos de carbohidratos: "))
grasas=float(input("Ingrese los gramos de grasas: "))

"""
Fórmula para calcular la cantidad de calorias
calorias totales= proteina*4+carbohidratos*4+grasas*9
"""
calorias=(proteina+carbohidratos)*4+grasas*9
print(f"Las calorias totales del producto son: {math.ceil(calorias)}")