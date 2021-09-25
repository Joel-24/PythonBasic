
# contador = 0
# print(f"2 elevado a {contador} es igual a: {2**contador}")

# contador = 1
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 2
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 3
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 4
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 5
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

from typing import Container


def run():
    LIMITE = 100000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print(F"2 elevado a {contador} es igual a: {potencia_2}")
        contador += 1
        potencia_2 = 2**contador

if __name__ == "__main__":
    run()