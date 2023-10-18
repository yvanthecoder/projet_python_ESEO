def spotlesdiez(plateau, piece, couleur ,coordonnee_X,coordonnee_Y):
    for i in range(5):
        for j in range(5):
            if plateau[coordonnee_Y+i][coordonnee_X+j] == couleur+piece[i][j]:
                return False
    return True

def PasDePieceCollées(plateau, piece, couleur,coordonnee_X,coordonnee_Y):
    for i in range(len(piece)):
        for j in range(len(piece)):
            if piece[i][j] == "#":
                if plateau[coordonnee_Y+i-1][coordonnee_X+j] == couleur+"#" or plateau[coordonnee_Y+i+1][coordonnee_X+j] == couleur+"#" or plateau[coordonnee_Y+i][coordonnee_X+j-1] == couleur+"#" or plateau[coordonnee_Y+i][coordonnee_X+j+1] == couleur+"#" :

                    return False
    return True 

def PieceEnDiagonale(plateau,piecesposees, piece, couleur,coordonnee_X,coordonnee_Y):
    if len(piecesposees) == 0:
        return True
    else :
        for i in range(len(piece)):
            for j in range(len(piece)):
                if piece[i][j] == "#":
                    if plateau[coordonnee_Y+i-1][coordonnee_X+j-1] == couleur+"#" or plateau[coordonnee_Y+i+1][coordonnee_X+j-1] == couleur+"#" or plateau[coordonnee_Y+i-1][coordonnee_X+j+1] == couleur+"#" or plateau[coordonnee_Y+i+1][coordonnee_X+j+1] == couleur+"#" :       
                        return True
        return False
