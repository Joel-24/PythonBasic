def run():
    mi_diccionario = {
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])
    
    poblacion_paises = {
        "Argentina" :  44938712,
        "Brasil" :  210213231323,
        "Colombia" :  500330293,

    }
    #imprime la poblacion de cada pais, en caso no se encuentre el pais genera error
    # print(poblacion_paises["Bolivia"])

    #imprime los paises en orden con el metodo "KEYS()" que es propio del diccionario
    # for pais in poblacion_paises.keys():
    #     print(pais)

    #imprime la poblacion "valores" con el metodo "values()" propio del diccionario
    # for pais in poblacion_paises.values():
    #     print(pais)

    #imprime los dos datos "valores" con el metodo "values()" propio del diccionario
    for pais, poblacion in poblacion_paises.items():
        print(f"{pais} tiene {poblacion} habitantes")

if __name__ == "__main__":
    run()