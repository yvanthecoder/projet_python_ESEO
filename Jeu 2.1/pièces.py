def creerppieces():
    Listepieces = [ [[" " for j in range(5)] for i in range(5)] for i in range(21)]

    #carré
    Listepieces[0]= [['#']]
    #ligne de 2
    Listepieces[1]=  [['#'], ['#']]
    #ligne de 3
    Listepieces[2]= [['#'], ['#'], ['#']]
    #coin de 3
    Listepieces[3]= [['#'], ['#', '#']]

    #ligne de 4
    Listepieces[4]= [['#'], ['#'], ['#'], ['#']]

    #L inversé
    Listepieces[5]=[['#'], ['#'], ['#', '#']]


    #T de 4 cases (petit)
    Listepieces[6]=[['#', '#', '#'], [' ', '#']]

    #carré de 4 cases
    Listepieces[7]= [['#', '#'], ['#', '#']]
    #zigzag de 4
    Listepieces[8]=[['#', '#'], [' ', '#', '#']]
    #ligne de 5
    Listepieces[9]=[['#'], ['#'], ['#'], ['#'], ['#']]

    #grand L
    Listepieces[10]=[['#', '#'], ['#'], ['#'], ['#']]
    #2-3 cases
    Listepieces[11]=[['#'], ['#', '#'], [' ', '#'], [' ', '#']]
    #carré+1
    Listepieces[12]=[['#', '#'], ['#', '#'], [' ', '#']]
    #U
    Listepieces[13]=[['#', '#'], [' ', '#'], ['#', '#']]

    #4+1 
    Listepieces[14]=[['#'], ['#', '#'], ['#'], ['#']]

    #grand T 5 cases=
    Listepieces[15]= [['#', '#', '#'], [' ', '#'], [' ', '#']]
    #Grand coin
    Listepieces[16]=[['#'], ['#'], ['#', '#', '#']]
    #W
    Listepieces[17]=[['#', '#'], [' ', '#', '#'], [' ', ' ', '#']]
    #electricité
    Listepieces[18]=[['#'], ['#', '#', '#'], [' ', ' ', '#']]

    #petit T +1   
    Listepieces[19]= [['#'], ['#', '#', '#'], [' ', '#']]
    #croix
    Listepieces[20]=[[' ', '#'], ['#', '#', '#'], [' ', '#']]
    return Listepieces


 

def affichagepiecesrestantes(Liste):
    for i in range(len(Liste)):
        print(f"{i+1}/")
        for j in range(len(Liste[i])):
            print(" ".join(Liste[i][j]))
        print(" \n")


