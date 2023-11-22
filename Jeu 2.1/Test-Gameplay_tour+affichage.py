from affichage_jeu import *
from Blocs import *
from pièces import *


def NouvellesCasesPosées(ListeTotale,pieceposée):
    for i in range(len(pieceposée)):
        ListeTotale.append(pieceposée[i])


#  "\033[1;36m" = Bleu
#  "\033[1;31m" = rouge
#  "\033[1;32m" = vert
#  "\033[1;33m" = jaune
#  "\033[1;37m" = blanc

def jeu(grille,nombre_de_joueurs):
    # création des joueurs selon le nombre indiqué
    couleurs = ["\033[1;36m","\033[1;31m","\033[1;32m","\033[1;33m"]
    players = []
    for i in range(nombre_de_joueurs):
        players.append(joueur())
        players[i].couleur = couleurs[i]
    
    #Début du jeu :
    fin = False
    tour = 0
    while not fin:
        effaceEcran()
        #Début du tour  :
        chiffrejoueur = tour%nombre_de_joueurs
        
        ##création des listes de cases jouées : liste tridimensionnel avec une liste de coordonnées pour chaque joueur
        Scores_Par_Cases = [[] for i in range(nombre_de_joueurs)]
        joueuractuel = players[chiffrejoueur]
        
        ##affichage du tour et de la grille
        affichegrille(grille,Scores_Par_Cases[chiffrejoueur])
        print(f"\033[1;37mTour n°{tour+1}")
        print(f"{joueuractuel.couleur}Joueur n°{(chiffrejoueur)+1}")
        
        ##affichage des options du joueur actuel
        print(f"\033[1;37m")
        affichagepiecesrestantes(joueuractuel.pieces)
        
        #Fin du tour :
        tour+=1
        if len(joueuractuel.pieces) == 0:
            fin = True
            


plandeTest = creerMatrice()
jeu(plandeTest,2)