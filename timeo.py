def taille(arbre:dict,lettre)->int:
    if lettre=='':
        return 0
    gauche = arbre[lettre][0]
    droite = arbre[lettre][1]
    return 1+taille(arbre,gauche) + taille(arbre,droite)

a = {
    'F': ['B', 'G'],
    'B': ['A', 'D'],
    'A': ['', ''],
    'D': ['C', 'E'],
    'C': ['', ''],
    'E': ['', ''],
    'G': ['', 'I'],
    'I': ['', 'H'],
    'H': ['', '']
}

assert taille(a,'F')==9
assert taille(a,'B')==5
assert taille(a,'I')==2