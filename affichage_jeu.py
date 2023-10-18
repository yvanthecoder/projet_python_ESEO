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
        
 
def affichegrille(grille):
    print(f"\033[1;37m")
    print(*grille[0])
    print(*grille[1])
    for i in range(2,len(grille)-1):
            print(f"\033[1;37m ".join(grille[i]), end = " ")
            print(i-1)
    print(*grille[-1])

lettres = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
effaceEcran()
affichegrille(creerMatrice())
print(creerMatrice())
for i in range(len(creerMatrice())):
    print(len(creerMatrice()[i][0]))