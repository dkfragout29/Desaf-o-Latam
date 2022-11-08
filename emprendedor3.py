""""
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇
Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
original de utilidades donde el usuario ingrese el precio de suscripción P, el número
de usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del
año anterior Uanterior
, todo esto mediante input(). El programa debe calcular las
utilidades actuales y mostrar la razón entre las utilidades actuales y las del año
anterior con dos decimales.
(2 Puntos)
"""
número_usuarios=int(input("usuarios: "))
precio_suscripción=int(input("precio: "))
gastos_totales=int(input("gastos: "))
utilidades=precio_suscripción*número_usuarios-gastos_totales
utilidades_año_anterior=int(input("Utilidades antiguas: "))
razón=utilidades/utilidades_año_anterior
print(f"La razón entre las utilidades actuales y las utilidades del año anterior es de {razón:.2f}")