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
    def posabilité(plan,coordonnées_X,coordonnées_Y):
        Au_Moins_Une_Case_Posable = False
        for ligne in range(self.piecesjouée):
            for colonne in range(self.piecesjouée[ligne]):
                if [coordonnées_Y+ligne,coordonnées_X+colonne] in self.casesINTERDITES:
                    return False
                elif [coordonnées_Y+ligne,coordonnées_X+colonne] in self.casesELIGIBLES:
                    Au_Moins_Une_Case_Posable = True
            
    def poserpiece(self,numeropiece,plan,coordonnées_X,coordonnées_Y):
            #met a 0 piecesposées qui sert a avoir les coordonées ajoutées ce tour:
            self.piecesposées = []
            self.piecesjouée = self.pieces[numeropiece-1]
            self.pieces.remove(self.piecesjouée)
            #place les # dans le "plan":
            for i in range(len(self.piecesjouée)):
                for j in range(len(self.piecesjouée[i])):
                        if self.piecesjouée[i][j] == "#":
                            plan[coordonnées_Y+i][coordonnées_X+j] = self.couleur+"#"
                            #actualise les coordonées dans piecesposées:
                            self.piecesposées.append([coordonnées_Y+i,coordonnées_X+j])
            self.SpotCasesInterdites(plan,coordonnées_X,coordonnées_Y)
            self.SpotCasesEligibles(plan,coordonnées_X,coordonnées_Y)
    


