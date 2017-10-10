from random import *


def generar_mazo():
    return sample([(x, y) for x in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] for y in ['p', 't', 'd', 'c']], 52)


def valor_carta(carta):
    if str(carta[0]) in "JQK":
        return 10
    if str(carta[0]) == "A":
        return 1
    return carta[0]


def valor_mano(mano):
    if mano == []:
        return 0
    else:
        return valor_carta(mano[0]) + valor_mano(mano[1:])


def hay_aces(mano):
    if mano == []:
        return False
    else:
        if str(mano[0][0]) == "A":
            return True
        else:
            return hay_aces(mano[1:])


def valor_aces(mano):
    if mano == []:
        return 0
    else:
        if hay_aces(mano) and valor_mano(mano) <= 10:
            return 10 + valor_mano(mano)
        else:
            return valor_mano(mano)

def verificar_mano(mano):
        if  valor_mano(mano) <= 21:
            return True
        else:
            
            return False


def jugar(mazo, casa, jugador):
  

    if (jugador==[] and casa==[]):

        return jugar(mazo[4:], casa + mazo[:2], jugador + mazo[2:4])

    print str(casa[1:])+"[(*, *)]"
    print jugador
    print "--------------------------------------------"

    
    if verificar_mano(jugador) == False:
        print "Perdio ome"
        return exit

    if verificar_mano(casa) == False:
        print "Ganaste ome"
        return exit

    if (input( "Desea otra carta?:  s = 1/ no = 0:   ") == 1):
        if mazo != []:
            if jugador == []:
                return jugar(mazo[4:],casa, jugador + mazo[2:4])
            if valor_aces(jugador) < 21:
                return jugar(mazo[2:], casa, jugador + [mazo[1]])
    else:
        if mazo != []:
            if casa == []:
                return jugar(mazo[4:], casa + mazo[:2], jugador)
            if valor_aces(casa) < 21 :
                return jugar(mazo[2:], casa + [mazo[0]], jugador)


jugar(generar_mazo(), [], [])
