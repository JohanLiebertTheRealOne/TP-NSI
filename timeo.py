def taille(arbre:dict,lettre)->int:
    if lettre=='':
        return 0
    gauche = arbre[lettre][0]
    droite = arbre[lettre][1]
    return 1+taille(arbre,gauche) + taille(arbre,droite)