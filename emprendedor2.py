""""
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇
Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto.Para ello utiliza input() para solicitar
como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
(5 Puntos)

import math
#print(math.sqrt(5))
9**(1/2) = 9 elevado a 1/2 (igual a raiz cuadrada)

Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de
utilidades en la cual se solicite mediante input() los parámetros de entrada precios
de suscripción P, así como el número de usuarios U normal y U premium y el gasto total GT.
(3 Puntos)

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = (𝑃 * 𝑈)+(𝑃*UP) − 𝐺𝑇

"""
precio_suscripción=int(input("precio: "))
número_usuarios=int(input("usuarios: "))
número_usuariospremium=int(input("usuariopremium: "))
gasto_total=int(input("gasto: "))
utilidades=precio_suscripción*número_usuarios-gasto_total+número_usuariospremium
print(utilidades)