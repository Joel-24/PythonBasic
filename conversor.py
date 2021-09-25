#PRIMERA PRUEBA 
# menu = """
# Bienvenido al conversor de monedas 🧡


# 1 - Nuevos soles
# 2 - Pesos argentinos
# 3 - Pesos mexicanos

# Elige una opcion:
# """
# opcion = int(input(menu))

# if opcion == 1:
#     pesos = input("¿Cuántos nuevos soles tienes?:  ")
#     pesos = float(pesos)
#     valor_dolar = 4.01
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares")

# elif opcion == 2:
#     pesos = input("¿Cuántos pesos argentinos tienes?:  ")
#     pesos = float(pesos)
#     valor_dolar = 5.7
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares")

# elif opcion == 3:
#     pesos = input("¿Cuántos pesos mexicanos tienes?:  ")
#     pesos = float(pesos)
#     valor_dolar = 7.1
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares")

# else:
#     print("Ingresa una opcion correcta")

#SEGUNDA PRUEBA USANDO FUNCIONES (Modulando nuestro conversor)
def conversor(moneda,valor_dolar):
    pesos = input("¿Cuántos " + moneda + " tienes?:  ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 🧡


1 - Nuevos soles
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion:
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("nuevos soles", 4.01)
elif opcion == 2:
    conversor("pesos argentinos", 5.9)
elif opcion == 3:
    conversor("pesos mexicanos", 7.8)

else:
    print("Ingresa una opcion correcta")







# dolares = input("¿Cuántos dolares tienes: ")
# dolares = float(dolares)
# valor_dolar = 4.1
# nuevo_sol = dolares * valor_dolar
# nuevo_sol =round(nuevo_sol, 2)
# nuevo_sol = str(nuevo_sol)
# print("Tienes S/." + nuevo_sol + " nuevos soles")
