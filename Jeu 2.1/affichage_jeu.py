def creerMatrice():
    matrice = [["-" for i in range(20)] for j in range(20)]
    Barrierehorizontale = ["*" for i in range(20)]
    lignelettres = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    matrice.append(Barrierehorizontale)
    matrice.insert(0,Barrierehorizontale)
    matrice.insert(0,lignelettres)
    for i in range(1,len(matrice)-1):
            matrice[i].insert(0,"*")
            matrice[i].append("*")
    return matrice

def effaceEcran ():
    for i in range (1,100) :
        print("\n")
        
 
def affichegrille(grille,listejouée):
    #création d'une pseudo liste afin de ne pas impacter la grille originale
    Liste = grille
    
    #camouflage des 1 et des 0
    for i in range(2,len(grille)-1):
        for j in range(2,len(grille)-2):
            if Liste[i][j] != "-" and [i,j] not in listejouée:
                Liste[i][j] = "-"
    #impression du plateau
    print(f"\033[1;37m")
    print(*Liste[0])
    print(*Liste[1])
    for i in range(2,len(grille)-1):
            print(f"\033[1;37m ".join(Liste[i]), end = " ")
            print(i-1)
    print(*Liste[-1])


lettres = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
