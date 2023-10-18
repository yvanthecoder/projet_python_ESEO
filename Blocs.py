from affichage_jeu import *
from pièces import *
from gameplay import *
setPieces = creerppieces()
class joueur:
    def __init__(self):
        self.couleur = ""
        self.pieces = setPieces
        self.piecesposées = []
        self.piecesjouée = []
    def posabilité (self,Plan,coordX,coordY,couleurAutreJoueur):
        if spotlesdiez(Plan, self.piecesjouée, self.couleur, coordX,coordY) and spotlesdiez(Plan, self.piecesjouée, couleurAutreJoueur , coordX,coordY) and PasDePieceCollées(Plan,self.piecesjouée,self.couleur,coordX,coordY) and PieceEnDiagonale(Plan,self.piecesposées,self.piecesjouée,self.couleur,coordX,coordY):
            return True
        return False
    def poserpiece(self,numeropiece,plan,couleurAutreJoueur,coordonnées_X,coordonnées_Y):
            self.piecesjouée = self.pieces[numeropiece-1]
            self.pieces.remove(self.piecesjouée)    
            self.piecesposées.append(self.piecesjouée)
            for i in range(len(self.piecesjouée)):
                for j in range(len(self.piecesjouée[i])):
                        if self.piecesjouée[i][j] == "#":
                            plan[coordonnées_Y+i][coordonnées_X+j] = self.couleur+"#"
   
    
#  "\033[1;36m" = Bleu
#  "\033[1;31m" = rouge
""" Jeu entre ligne 1 et colone 1 jusqu'à ligne 21 colonne 21"""
effaceEcran()

""" plateau = creerMatrice()
joueur1 = joueur()
joueur2 = joueur()
joueur1.couleur = "\033[1;36m"
joueur2.couleur = "\033[1;31m"

    
joueur1.poserpiece(9,plateau,joueur2.couleur,15,14)
joueur1.poserpiece(1,plateau,joueur2.couleur,14,13)
joueur1.poserpiece(1,plateau,joueur2.couleur,13,11)
affichegrille(plateau)
 """
 
affichagepiecesrestantes(setPieces)