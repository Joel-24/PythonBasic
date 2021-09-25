#PRIMERA PRUEBA
# print("Mensaje especial")
# print("¡Estoy aprendiendo a usar funciones!")
# print("Mensaje especial")
# print("¡Estoy aprendiendo a usar funciones!")
# print("Mensaje especial")
# print("¡Estoy aprendiendo a usar funciones!")

#SEGUNDA PRUEBA USANDO FUNCIONES PARA NO REPETIR
# def imprimir_mensaje():
#     print("Mensaje especial")
#     print("¡Estoy aprendiendo a usar funciones!")    

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

#TERCERA PRUEBA (FUNCIONES)

# def conversacion(mensaje):
#     print("Hola")
#     print("como estas")
#     print(mensaje)
#     print("adios")    


# opcion = int(input("Elige una opción (1, 2, 3): "))
# if opcion == 1:
#     conversacion("Elegiste la opción 1")
# elif opcion == 2:
#     conversacion("Elegiste la opción 2")
# elif opcion == 3:
#     conversacion("Elegiste la opción 3")
# else:
#     print("Escribe la opción correcta")

# ADIONAL USANDO  "RETURN"
def suma(a,b):
    print("Se suman dos númemros")
    resultado = a + b
    return resultado
sumatoria = suma(1,4)

print(sumatoria)


#EJERCICIO N° #1

# def area_rectangulo(area):
#     print(f"El area del triangulo es {area}")

# base = int(input("Ingrese la base: "))
# altura = int(input("Ingrese la altura: "))

# area = base * altura

# area_rectangulo(area)

#EJERCICIO N° #2

# def area_circulo(area):
#     print(f"- {area}")


# from typing import Match


# radio = int(input("Ingrese el radio: "))

# pi = 3.14159

# area = (radio ** 2) * pi

# area = round(area,3)
# area_circulo(area)

#EJERCICIO N° #3


# a = int(input("Ingrese el primer numero: "))
# b = int(input("Ingrese el segundo numero: "))

# if a > b:
#     print("1")
# elif a < b:
#     print("-1")
# elif a == b:
#     print("0")
