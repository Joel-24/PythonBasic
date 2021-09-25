def run():
    caballeros_dorados = {
        'aries': 'mu',
        'tauro': 'aldebaran',
        'cancer': 'deadmask',
        'geminis': 'saga',
        'leo': 'aioria',
        'virgo': 'shaka',
        'libra': 'dohko',
        'sagitario': 'aioros',
        'escorpion': 'milo',
        'capricornio': 'shura',
        'acuario': 'camus',
        'piscis': 'afrodita',
    }
    # for signo_zodiacal in caballeros_dorados.keys():
    #     print(signo_zodiacal)
    # for nombre_caballero in caballeros_dorados.values():
    #     print(nombre_caballero)
    # for signo_zodiacal, nombre_caballero in caballeros_dorados.items():
    #     print(str(signo_zodiacal).capitalize() + ': ' + str(nombre_caballero).capitalize())
    seguir = 's'
    while seguir.lower() == 's':
        llave = input('Escribe tu signo zodical: ').lower()
        print (f'El caballero que representa tu signo es: {str(caballeros_dorados[llave]).capitalize()}')
        seguir = input('Desea continuar S/N:')
if __name__ == "__main__":
    run()