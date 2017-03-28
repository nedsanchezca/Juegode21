#Programa que sirve como juego de 21, cuya principal caracteristica es que no tiene asignaciones
import random

""""Funcion que permite dar carta apartir de un mazo"""
def darMazo():
    return [['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]

""""Funcion que permite asignar un valor a la carta si no tiene un valor numerico"""""
def analizarCarta(card):
    if (card == 'K' or card == 'Q' or card == 'J'):
        return 10
    elif (card == 'A'):
        return 1 or 11
    else:
        return int(card)

"""""Funcion que anade a la baraja de juego las cartas en forma de una lista"""""
def repartirCartas(mazo):
    mazo[0].insert(len(mazo[0]), analizarCarta(darMazo()[0][random.randint(0, 12)]))
    mazo[1].insert(len(mazo[1]), analizarCarta(darMazo()[0][random.randint(0, 12)]))
    return mazo

""""Funcion que permite obtener el puntaje con respecto a los ases"""
def obtenerMPuntaje(cartas, nu):
    if (nu == 0):
        return sum(cartas)
    elif (sum(cartas) + 10 * nu <= 21):
        return sum(cartas) + 10 * nu;
    else:
        return obtenerMPuntaje(cartas, nu - 1)

def obtenerPuntaje(cartas):
    return obtenerMPuntaje(cartas, cartas.count(1))

"""""Funcion que desarrolla el juego de la persona"""""
def turnoJugador(cartas):
    print ("Su turno: ")
    print ("Su puntaje es: "), obtenerPuntaje(cartas[0])
    if (obtenerPuntaje(cartas[0]) == 21):
        print("Ha ganado")
    elif (obtenerPuntaje(cartas[0]) < 21):
        print ("Sus cartas son:"), cartas[0]
        print ("si quiere coger otra carta oprima cualquier letra, si quiere plantarse oprima (0)")
        if (raw_input() != "0"):
            cartas[0].insert(len(cartas[0]), analizarCarta(darMazo()[0][random.randint(0, 12)]))
            return Juego(cartas, 'J')
        else:
            print("Maquina")
            return Juego(cartas, 'M')
    elif (obtenerPuntaje(cartas[0]) > 21):
        print("ha perdido el juego")
        print cartas

"""""Parte que desarrolla el juego de la maquina"""
def turnoMaquina(cartas):
    if (obtenerPuntaje(cartas[1]) > 21):
        print ("Jugador ha ganado")
        print cartas
    if (obtenerPuntaje(cartas[1]) < 21 and (obtenerPuntaje(cartas[1]) > obtenerPuntaje(cartas[0]))):
        print("Maquina gana")
        print cartas
    if (obtenerPuntaje(cartas[1]) < 21 and (obtenerPuntaje(cartas[1]) <= obtenerPuntaje(cartas[0]))):
        if (obtenerPuntaje(cartas[1]) == obtenerPuntaje(cartas[0])):
            print ("empate")
            print cartas
        else:
            print ("maquina ha sacado una carta")
            cartas[1].insert(len(cartas[1]), analizarCarta(darMazo()[0][random.randint(0, 12)]))
            return Juego(cartas, 'R')

"""""Parte del juego donde se asignan las cartas a jugar y cuando juega la maquina"""
def Juego(cartas, jug):
    #print cartas
    if (cartas[0] == []):
        print ("Reparte cartas al jugador y al repartidor")
        return Juego(repartirCartas(cartas), 'J')
    elif (len(cartas[0]) == 1):
        print ("Reparte cartas jugador y al repartidor")
        return Juego(repartirCartas(cartas), 'J')
    if (jug == "M"):
        turnoMaquina(cartas)
    elif (len(cartas[0]) >= 2 and (jug == "J")):
        turnoJugador(cartas)

Juego([[], []], 'J')