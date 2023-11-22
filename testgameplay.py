def spotlesdiez(plateau, piece, couleur ,coordonnee_X,coordonnee_Y):
#good
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if plateau[coordonnee_Y+i][coordonnee_X+j] == couleur+piece[i][j]:
                return False
    return True
    
def findemap(plateau,piece,coordX,coordY):
    if coordY+len(piece)>=len(plateau):
            return False
    for i in range(len(piece)):
        if coordX+len(piece[i]) >= len(plateau):
            return False
    return True

def casesInterdites():
    
def casesEligibles(PlateauDeJeu,piece,couleur,coordonnee_X,coordonnee_Y,casesELIGIBLES,casesINTERDITES):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if PlateauDeJeu[coordonnee_Y][coordonnee_X] == couleur+"#":
                for q in range(-1,2):
                        for p in range(-1,2):
                            if abs(q) == abs(p):
                                if PlateauDeJeu[coordonnee_Y+i+p][coordonnee_X+j+q] == "-" and [coordonnee_Y+i+p,coordonnee_X+j+q] not in casesINTERDITES:
                                    PlateauDeJeu[coordonnee_Y+i+p][coordonnee_X+j+q] = couleur+"-"
                                    casesELIGIBLES.append([coordonnee_Y+i+p,coordonnee_X+j+q])