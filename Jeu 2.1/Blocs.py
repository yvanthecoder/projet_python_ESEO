from affichage_jeu import *
from pièces import *

class joueur:
    def __init__(self):
        self.couleur = ""
        self.pieces = creerppieces()
        self.piecesposées = []
        self.piecesjouée = []
        self.casesELIGIBLES = []
        self.casesINTERDITES= []
    def SpotCasesInterdites(self,plan,coordonnées_X,coordonnées_Y):
        for LinePiece in range(len(self.piecesjouée)):
            for ColPiece in range(len(self.piecesjouée[LinePiece])):
                if plan[coordonnées_Y+LinePiece][coordonnées_X+ColPiece] == self.couleur+"#":
                    for absc in range(-1,2):
                        for ordo in range(-1,2):
                            if abs(absc) != abs(ordo) and plan[coordonnées_Y+LinePiece+absc][coordonnées_X+ColPiece+ordo] == "-":
                                self.casesINTERDITES.append([coordonnées_Y+LinePiece+absc,coordonnées_X+ColPiece+ordo]) 
                                plan[coordonnées_Y+LinePiece+absc][coordonnées_X+ColPiece+ordo] = self.couleur+"0"
    def SpotCasesEligibles(self,plan,coordonnées_X,coordonnées_Y):
        for LinePiece in range(len(self.piecesjouée)):
            for ColPiece in range(len(self.piecesjouée[LinePiece])):
                if plan[coordonnées_Y+LinePiece][coordonnées_X+ColPiece] == self.couleur+"#":
                    for absc in range(-1,2,2):
                        for ordo in range(-1,2,2):
                            if plan[coordonnées_Y+LinePiece+absc][coordonnées_X+ColPiece+ordo] == "-" and [coordonnées_Y+LinePiece+absc,coordonnées_X+ColPiece+ordo] not in self.casesINTERDITES:
                                plan[coordonnées_Y+LinePiece+absc][coordonnées_X+ColPiece+ordo] = self.couleur+"1"
                                self.casesELIGIBLES.append([coordonnées_Y+LinePiece+absc,coordonnées_X+ColPiece+ordo])
    """ def posabilité(plan,coordonnées_X,coordonnées_Y):
        if findemap(plan,self.piecesjouée,coordonnées_X,coordonnées_Y): """
            
    def poserpiece(self,numeropiece,plan,coordonnées_X,coordonnées_Y):
            self.piecesposées = []
            self.piecesjouée = self.pieces[numeropiece-1]
            self.pieces.remove(self.piecesjouée)    
            self.piecesposées.append(self.piecesjouée)
            for i in range(len(self.piecesjouée)):
                for j in range(len(self.piecesjouée[i])):
                        if self.piecesjouée[i][j] == "#":
                            plan[coordonnées_Y+i][coordonnées_X+j] = self.couleur+"#"
                            self.piecesposées.append([coordonnées_Y+i,coordonnées_X+j])
            self.SpotCasesInterdites(plan,coordonnées_X,coordonnées_Y)
            self.SpotCasesEligibles(plan,coordonnées_X,coordonnées_Y)
    
#  "\033[1;36m" = Bleu
#  "\033[1;31m" = rouge

