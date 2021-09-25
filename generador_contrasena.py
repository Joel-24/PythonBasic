import random


def generar_contrasena():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    minusculas = ["a", "b", "c", "d", "e", "f", "h", "i"]
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []
#random.choice(listas) - te devuelve las listas mezcladas aletorio.
    for i in range(15):
        caracter_random = random.choice(caracteres)
        #.append(variable) - agrega a la variable "contrasena" que fue creado antes lin 12
        #el cual es una lista.
        contrasena.append(caracter_random)
#.join(lista o variable) - quita todo caracter innecesario para que se forme en texto
#de corrido.
    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print(f"Tu nueva contraseña es: {contrasena}")


if __name__ == "__main__":
    run()


# .join(lista) -  pone en formato texto de corrido y nos permite juntar las letras
# sin espacio y comas u otro caracter.
   
# contrasena = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

# contrasena = "".join(contrasena)

# print(contrasena)