import sys
sys.argv
sol=float(sys.argv[1])
peso_argentino=float(sys.argv[2])
dolar_americano=float(sys.argv[3])
peso_chileno=float(sys.argv[4])
conversion_sol_chileno=sol*peso_chileno
conversion_argentino_chileno=peso_argentino*peso_chileno
conversion_dolar_chileno=dolar_americano*peso_chileno
print(f"Los {peso_chileno} pesos chilenos equivalen a:\n{conversion_sol_chileno} soles\n{conversion_argentino_chileno} pesos argentinos\n{conversion_dolar_chileno} dólares")

"""
IMPORTANTE:para correr lista sys.argv, se agrega en la terminal los siguientes argumentos en el siguiente orden:
python conversiones.py 0.0046 0.093 0.0013 10000

"""