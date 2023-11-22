from testgameplay import *
from affichage_jeu import *
from pièces import *
from gameplay import *


class joueur:
    def __init__(self):
        self.couleur = ""
        self.pieces = creerppieces()
        self.piecesposées = []
        self.piecesjouée = []
        self.casesELIGIBLES = []
        self.casesINTERDITES = []
    def posabilité (self,Plan,coordX,coordY,couleurAutreJoueur):
        if findemap(Plan,self.piecesposées,coordX,coordY):
            print("\033[1;37maucun souci de barrière")
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
            casesEligiblesInterdites(plan,self.piecesjouée,self.couleur,coordonnées_X,coordonnées_Y,self.casesELIGIBLES,self.casesINTERDITES)


effaceEcran()
plateux = creerMatrice()

joueurtest = joueur()
joueurtest.couleur = "\033[1;36m"

joueurtest.poserpiece(6,plateux,"\033[1;36m",10,10)
affichegrille(plateux)