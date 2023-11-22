from affichage_jeu import *
from pièces import *
from Blocs import *
from gameplay import *

#test Dédié à la création de cases interdites et autorisées
#test de camouflage de ces dernières lors de l'impression

#creation du joueur
joueurtest = joueur()
joueurtest.couleur = "\033[1;36m"
#creation du plateau
plandejeu = creerMatrice()
#creationde la liste des cases posées
Coordposées = []

effaceEcran()
joueurtest.poserpiece(15,plandejeu,12,12)
(joueurtest.piecesposées[-1])
NouvellesCasesPosées(Coordposées,joueurtest.piecesposées)
affichegrille(plandejeu,Coordposées)
print(joueurtest.casesINTERDITES)
print(joueurtest.casesELIGIBLES)

