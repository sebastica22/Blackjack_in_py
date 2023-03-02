from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#pregunta_1 = input("Quieres jugar Blackjack responde 'si' o 'no' ? \n ")
mano = []
mano_de1 = []

def activacionJuego(mano_de, final_deljuego):

    print(logo)
    mano_uno = random.sample(cards, 2)
    mano = mano_uno 
    suma = 0
    for carta in mano:
        suma += carta
    mano_de1.append(mano_de)
    print(f"Tus cartas: {mano} Tu puntaje: {suma}\n Primera carta del dealer {mano_de1}")

    while True:
        pregunta_2 = input("Quieres otra carta responde 'si' o 'no'\n\n").lower()
        if pregunta_2 == "no":
            han = mano_de
            mano_de1.append(han)
            resul_dealer = sum(mano_de1)
            if sum(mano) > resul_dealer:
                 print(f"\n\n GANASTE !!!\n\nTus cartas: {mano} Tu puntaje: {suma}\n\nSegunda mano del dealer {han} Puntaje del dealer: {resul_dealer}\n\n")
            elif sum(mano) < resul_dealer:
                 print(f"\n\n Perdiste !!!\n\nTus cartas: {mano} Tu puntaje: {suma}\n\nSegunda mano del dealer {han} Puntaje del dealer: {resul_dealer}\n\n")
            else:
                print(f"\n\nEmpate !!!\n\nTus cartas: {mano} Tu puntaje: {suma}\nSegunda mano del dealer {han} Puntaje del dealer: {resul_dealer}\n")
            break
        
        elif pregunta_2 == "si":
               mano_ju = mano_de
               mano.append(mano_ju)
               suma = sum(mano)
               print(f"Tu carta es {mano_ju}, tu puntaje es {suma}")
               if suma > 21:
                    print(f"Tu carta es {mano_ju} Perdiste, te has pasado del limite, tu puntaje es {suma}")
                    break
               



mano_de = random.choice(cards)
final_juego = False
activacionJuego(mano_de, final_juego)