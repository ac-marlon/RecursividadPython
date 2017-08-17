from random import *


def generar_mazo():
    return sample([(x, y) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] for y in ['p', 't', 'd', 'c']], 52)


def verificar_veintiuna(mano):
    if mano[0][0] + mano[1][0]<21:
        print 'Holiiiiiiii!!!'


def jugar(mazo):
    if mazo != []:
        print mazo[0:2]
        verificar_veintiuna(mazo[0:2])
        # verificar_veintiuna(mazo[1:2])
        return jugar(mazo[50:])
        

jugar(generar_mazo())


def pedir_carta(mazo):
    print mazo[:3]
    return jugar(mazo[49:])
    

# pedir_carta(generar_mazo())
