def creerppieces():
    Listepieces = [ [[" " for j in range(5)] for i in range(5)] for i in range(21)]

    #carré
    Listepieces[0][0][0] = "#"
    #ligne de 2
    Listepieces[1][0][0] = "#"
    Listepieces[1][1][0] = "#"
    #ligne de 3
    Listepieces[2][0][0] = "#"
    Listepieces[2][1][0] = "#"
    Listepieces[2][2][0] = "#"
    #coin de 3
    Listepieces[3][0][0] = "#"
    Listepieces[3][1][0] = "#"
    Listepieces[3][1][1] = "#"
    #ligne de 4
    Listepieces[4][0][0] = "#"
    Listepieces[4][1][0] = "#"
    Listepieces[4][2][0] = "#"
    Listepieces[4][3][0] = "#"
    #L inversé
    Listepieces[5][0][0] = "#"
    Listepieces[5][1][0] = "#"
    Listepieces[5][2][0] = "#"
    Listepieces[5][2][1] = "#"

    #T de 4 cases (petit)
    Listepieces[6][0][0] = "#"
    Listepieces[6][0][1] = "#"
    Listepieces[6][0][2] = "#"
    Listepieces[6][1][1] = "#"
    #carré de 4 cases
    Listepieces[7][0][0] = "#"
    Listepieces[7][0][1] = "#"
    Listepieces[7][1][0] = "#"
    Listepieces[7][1][1] = "#"
    #zigzag de 4
    Listepieces[8][0][0] = "#"
    Listepieces[8][0][1] = "#"
    Listepieces[8][1][1] = "#"
    Listepieces[8][1][2] = "#"
    #ligne de 5
    Listepieces[9][0][0] = "#"
    Listepieces[9][1][0] = "#"
    Listepieces[9][2][0] = "#"
    Listepieces[9][3][0] = "#"
    Listepieces[9][4][0] = "#"

    #grand L
    Listepieces[10][0][0] = "#"
    Listepieces[10][0][1] = "#"
    Listepieces[10][1][0] = "#"
    Listepieces[10][2][0] = "#"
    Listepieces[10][3][0] = "#"
    #2-3 cases
    Listepieces[11][0][0] = "#"
    Listepieces[11][1][0] = "#"
    Listepieces[11][1][1] = "#"
    Listepieces[11][2][1] = "#"
    Listepieces[11][3][1] = "#"
    #carré+1
    Listepieces[12][0][0] = "#"
    Listepieces[12][0][1] = "#"
    Listepieces[12][1][0] = "#"
    Listepieces[12][1][1] = "#"
    Listepieces[12][2][1] = "#"
    #U
    Listepieces[13][0][0] = "#"
    Listepieces[13][0][1] = "#"
    Listepieces[13][1][1] = "#"
    Listepieces[13][2][1] = "#"
    Listepieces[13][2][0] = "#"
    #4+1 
    Listepieces[14][0][0] = "#"
    Listepieces[14][1][0] = "#"
    Listepieces[14][1][1] = "#"
    Listepieces[14][2][0] = "#"
    Listepieces[14][3][0] = "#"

    #grand T 5 cases
    Listepieces[15][0][0] = "#"
    Listepieces[15][0][1] = "#"
    Listepieces[15][0][2] = "#"
    Listepieces[15][1][1] = "#"
    Listepieces[15][2][1] = "#"
    #Grand coin
    Listepieces[16][0][0] = "#"
    Listepieces[16][1][0] = "#"
    Listepieces[16][2][0] = "#"
    Listepieces[16][2][1] = "#"
    Listepieces[16][2][2] = "#"
    #W
    Listepieces[17][0][0] = "#"
    Listepieces[17][0][1] = "#"
    Listepieces[17][1][1] = "#"
    Listepieces[17][1][2] = "#"
    Listepieces[17][2][2] = "#"
    #electricité
    Listepieces[18][0][0] = "#"
    Listepieces[18][1][0] = "#"
    Listepieces[18][1][1] = "#"
    Listepieces[18][1][2] = "#"
    Listepieces[18][2][2] = "#"

    #petit T +1   
    Listepieces[19][0][0] = "#"
    Listepieces[19][1][0] = "#"
    Listepieces[19][1][1] = "#"
    Listepieces[19][1][2] = "#"
    Listepieces[19][2][1] = "#"
    #croix
    Listepieces[20][0][1] = "#"
    Listepieces[20][1][1] = "#"
    Listepieces[20][2][1] = "#"
    Listepieces[20][1][0] = "#"
    Listepieces[20][1][2] = "#" 
    return Listepieces


 

def affichagepiecesrestantes(Liste):
    for i in range(len(Liste)):
        print(f"{i+1}/")
        for j in range(len(Liste[i])):
            print(" ".join(Liste[i][j]))
        print(" \n")


