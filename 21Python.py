from random import *


def generar_mazo():
    return sample([(x, y) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] for y in ['p', 't', 'd', 'c']], 52)


def valor_mano(mano):
    if mano[0][0] == 'J':
        if mano[1][0] == 'J':
            return 20
        elif mano[1][0] == 'Q':
            return 20
        elif mano[1][0] == 'K':
            return 20
        return 10 + mano[1][0]
    elif mano[0][0] == 'Q':
        if mano[1][0] == 'J':
            return 20
        elif mano[1][0] == 'Q':
            return 20
        elif mano[1][0] == 'K':
            return 20
        return 10 + mano[1][0]
    elif mano[0][0] == 'K':
        if mano[1][0] == 'J':
            return 20
        elif mano[1][0] == 'Q':
            return 20
        elif mano[1][0] == 'K':
            return 20
        return 10 + mano[1][0]

    if mano[1][0] == 'J':
        if mano[0][0] == 'J':
            return 20
        elif mano[0][0] == 'Q':
            return 20
        elif mano[0][0] == 'K':
            return 20
        return 10 + mano[0][0]
    elif mano[1][0] == 'Q':
        if mano[0][0] == 'J':
            return 20
        elif mano[0][0] == 'Q':
            return 20
        elif mano[0][0] == 'K':
            return 20
        return 10 + mano[0][0]
    elif mano[1][0] == 'K':
        if mano[0][0] == 'J':
            return 20
        elif mano[0][0] == 'Q':
            return 20
        elif mano[0][0] == 'K':
            return 20
        return 10 + mano[0][0]

    else:
        return mano[0][0] + mano[1][0]


def jugar(mazo, casa, jugador):
    print casa
    print jugador
    if mazo != []:
        if casa == []:
            return jugar(mazo[4:], casa + mazo[:2], jugador + mazo[2:4])
        if valor_mano(casa) < 21 and valor_mano(jugador) < 21:
            print valor_mano(casa)
            print valor_mano(jugador)
            return jugar(mazo[2:], casa + [mazo[0]], jugador + [mazo[1]])


jugar(generar_mazo(), [], [])
