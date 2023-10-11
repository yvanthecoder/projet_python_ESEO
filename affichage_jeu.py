def creerMatrice():
    matrice = [["-" for i in range(20)] for j in range(20)]
    Barrierehorizontale = ["*" for i in range(22)]
    matrice.append(Barrierehorizontale)
    matrice.insert(0,Barrierehorizontale)
    for i in range(1,len(matrice)-1):
            matrice[i].insert(0,"*")
            matrice[i].append("*")
    return matrice

def effaceEcran ():
    for i in range (1,100) :
        print("\n")
       
from random import *    
def affichegrille(grille):
    print("\033[1;30m")
    print(*grille[0])
    for i in range(1,len(grille)-1):
        for j in range(len(grille)):
            if grille[i][j] != "*":
                print(f"\033[1;37m{grille[i][j]}",end = " ")
            elif grille[i][j] == "*" and j == 0:
                print(f"\033[1;30m{grille[i][j]}", end = " ")
            else:
                print(f"\033[1;30m{grille[i][j]}")  
    print(*grille[-1])            


affichegrille(creerMatrice())