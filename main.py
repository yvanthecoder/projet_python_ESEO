from affichage_jeu import *
from pièces import *

class joueur:
    def __init__(self):
        self.couleur = ""
        self.pieces = setPieces
        self.piecesposées = []
       
    def poserpiece(self,numeropiece,plan,coordonnées_X,coordonnées_Y):
        piecesjouée = self.pieces[numeropiece-1]
        if self.superposition_debordement(plan,piecesjouée,coordonnées_X,coordonnées_Y) is True:
            self.pieces.remove(piecesjouée)
            self.piecesposées.append(piecesjouée)
            #coordonnées dans la pièce qui est traitée
            coordonnées_piece_X = 0
            coordonnées_piece_Y = 0
            for i in range(len(piecesjouée)):
                for j in range(len(piecesjouée[i])):
                    if piecesjouée[i][j] == "#":
                        plan[coordonnées_Y+coordonnées_piece_Y][coordonnées_X+coordonnées_piece_X] = "\033[1;36m#"
                        coordonnées_piece_X += 1
                coordonnées_piece_X = 0
                coordonnées_piece_Y +=1
        else :
            print("il y a chevauchement")
           
    def superposition_debordement(self,tableau, piece, coordonnee_X,coordonnee_Y):
        limite = len(tableau[0])
        coordonnées_piece_X = 0
        coordonnées_piece_Y = 0
       
        for i in range(0, len(piece[0])):
            for j in range(0, len(piece[0])):
                if ((tableau[coordonnee_Y+coordonnées_piece_Y][coordonnee_X+coordonnées_piece_X] == "#" and piece[coordonnées_piece_Y][coordonnées_piece_X] == "#")) :
                    return (False)
                elif (tableau[coordonnee_Y+coordonnées_piece_Y][coordonnee_X+coordonnées_piece_X] == "*" and piece[coordonnées_piece_Y][coordonnées_piece_X] == "#"):
                    return (False)
                coordonnées_piece_X +=1
            coordonnées_piece_X = 0
            coordonnées_piece_Y += 1
        return (True)
                   
           
       
       
   
       







#  "\033[1;36m" = Bleu
#  "\033[1;31m" = rouge
""" Jeu entre ligne 1 et colone 1 jusqu'à ligne 21 colonne 21"""

setPieces = creerppieces()
plateau = creerMatrice()
joueur1 = joueur()
joueur1.poserpiece(9,plateau,15,14)
joueur1.poserpiece(18,plateau,15,14)


effaceEcran()
affichegrille(plateau)