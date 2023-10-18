from Blocs import *
from gameplay import *
from affichage_jeu import *
from pièces import *



def jeu():
    PlateauDeJeu = creerMatrice()
    joueur1 = joueur()
    joueur2 = joueur()
    joueur1.couleur = "\033[1;36m"
    joueur2.couleur = "\033[1;31m"
    joueurs = [joueur1,joueur2]
    PartieFinie = False 
    tour = 0
    while not PartieFinie :
        effaceEcran()
        tour += 1
        affichegrille(PlateauDeJeu)
        if tour%2 == 0 :
            JoueurDuTour = joueurs[0]
            CouleurAdverse = joueurs[1].couleur
        else :
            JoueurDuTour = joueurs[1]
            CouleurAdverse = joueurs[0].couleur
        print(f"{JoueurDuTour.couleur}Joueur n°{joueurs.index(JoueurDuTour)}")
        #poser la première case :
        affichagepiecesrestantes(JoueurDuTour.pieces)
        X = 0
        Y = 0
        if tour == 1 or tour == 2:
            while  (X,Y)!=(1,1) and (X,Y)!=(1,20) and (X,Y)!=(20,1) and (X,Y)!=(20,20):
                numéroPièce = int(input("Quel numéro de pièce voulez-vous poser ?\n"))
                JoueurDuTour.piecesjouée = JoueurDuTour.pieces[numéroPièce-1]
                print("Cette pièce étant votre prmeière vous ne pouvez la mettre que dans l'un des coins (1,1) (1,20) (20,1) (20,20)")
                X = int(input("X = "))
                Y = int(input("Y = "))
        #poser une case : 
        else :
            numéroPièce = int(input("Quel numéro de pièce voulez-vous poser ?\n"))
            JoueurDuTour.piecesjouée = JoueurDuTour.pieces[numéroPièce-1]
            print("En quel point ?")
            X = int(input("X = "))
            Y = int(input("Y = "))
        while not JoueurDuTour.posabilité(PlateauDeJeu,X,Y,CouleurAdverse):
            print("Impossible de poser la pièce de cette manière, réessayez")
            numéroPièce = int(input("Quel numéro de pièce voulez-vous poser ?\n"))
            JoueurDuTour.piecesjouée = JoueurDuTour.pieces[numéroPièce-1]
            print("En quel point ?")
            X = int(input("X = "))
            Y = int(input("Y = "))
            
        JoueurDuTour.poserpiece(numéroPièce,PlateauDeJeu,CouleurAdverse,X,Y+1)
        
jeu()