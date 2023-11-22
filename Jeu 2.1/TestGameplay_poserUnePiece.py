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
    X = 0
    Y = 0
    # Regroupe l'ensemble des cases posées et inutilisables dans la partie
    Cases_Totales_Posées = []
    
    while not fin:
        effaceEcran()
        #Début du tour  :
        chiffrejoueur = tour%nombre_de_joueurs
        
        ##création des listes de cases jouées : liste tridimensionnel avec une liste de coordonnées pour chaque joueur
        Scores_Par_Cases = [[] for i in range(nombre_de_joueurs)]
        joueuractuel = players[chiffrejoueur]
        
        ##affichage du tour et de la grille:
        affichegrille(grille,Cases_Totales_Posées)
        print(f"\033[1;37mTour n°{tour+1}")
        print(f"{joueuractuel.couleur}Joueur n°{(chiffrejoueur)+1}")
        
        ##affichage des options du joueur actuel:
        print(f"\033[1;37m")
        affichagepiecesrestantes(joueuractuel.pieces)
        
        ##Interface de choix du joueur:
        ###première pièce :
        if tour < nombre_de_joueurs:
            print("Cette pièce étant votre première vous ne pouvez la mettre que dans l'un des coins (1,1) (1,20) (20,1) (20,20)")
            numéroPièce = int(input("Quel numéro de pièce voulez-vous poser ?\n"))
            joueuractuel.piecesjouée = joueuractuel.pieces[numéroPièce-1]
            X = int(input("X = "))
            Y = int(input("Y = "))
            while  (X,Y)!=(1,1) and (X,Y)!=(1,20) and (X,Y)!=(20,1) and (X,Y)!=(20,20):
                print("Cette pièce étant votre première vous ne pouvez la mettre que dans l'un des coins (1,1) (1,20) (20,1) (20,20)")
                numéroPièce = int(input("Quel numéro de pièce voulez-vous poser ?\n"))
                joueuractuel.piecesjouée = joueuractuel.pieces[numéroPièce-1]
                X = int(input("X = "))
                Y = int(input("Y = "))
                
        ### poser une pièce normalement :
        else :
            numéroPièce = int(input("Quel numéro de pièce voulez-vous poser ?\n"))
            joueuractuel.piecesjouée = joueuractuel.pieces[numéroPièce-1]
            print("En quel point ?")
            X = int(input("X = "))
            Y = int(input("Y = "))
        #### vérification de la posabilité
        while not joueuractuel.posabilité():
            print("Impossible de poser la pièce de cette manière, réessayez")
            numéroPièce = int(input("Quel numéro de pièce voulez-vous poser ?\n"))
            joueuractuel.piecesjouée = joueuractuel.pieces[numéroPièce-1]
            print("En quel point ?")
            X = int(input("X = "))
            Y = int(input("Y = "))
        ####action finale pose la pièce quand tout est ok:
        joueuractuel.poserpiece(numéroPièce,grille,X,Y+1)
        
        ##Fin du tour :
        tour+=1
        if len(joueuractuel.pieces) == 0:
            fin = True   
            

plandeTest = creerMatrice()
jeu(plandeTest,2)