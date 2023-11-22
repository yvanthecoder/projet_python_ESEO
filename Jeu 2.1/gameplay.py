def findemap(plateau,piece,coordX,coordY):
    if coordY+len(piece)>=len(plateau):
            return False
    for i in range(len(piece)):
        if coordX+len(piece[i]) >= len(plateau):
            return False
    return True

def spotlesdiez(plateau, piece, couleur ,coordonnee_X,coordonnee_Y):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if plateau[coordonnee_Y+i][coordonnee_X+j] == couleur+piece[i][j]:
                return False
    return True

def NouvellesCasesPosées(ListeTotale,pieceposée):
    for i in range(len(pieceposée)):
        ListeTotale.append(pieceposée[i])
