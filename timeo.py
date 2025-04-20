# def taille(arbre:dict,lettre)->int:
#     if lettre=='':
#         return 0
#     gauche = arbre[lettre][0]
#     droite = arbre[lettre][1]
#     return 1+taille(arbre,gauche) + taille(arbre,droite)

# a = {
#     'F': ['B', 'G'],
#     'B': ['A', 'D'],
#     'A': ['', ''],
#     'D': ['C', 'E'],
#     'C': ['', ''],
#     'E': ['', ''],
#     'G': ['', 'I'],
#     'I': ['', 'H'],
#     'H': ['', '']
# }

# def echange(tab, i, j):
#     temp = tab[i]
#     tab[i] = tab[j]
#     tab[j] = temp

# def tri_selection(tab):
#     N = len(tab)
#     for k in range(N):
#         imin = k
#         for i in range(k + 1, N):
#             if tab[i] < tab[imin]:
#                 imin = i
#         echange(tab, k, imin)

def correspond(mot,mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    liste_index = []
    i =  0
    for lettre in mot_a_trous:
        if lettre == "*":
            liste_index.append(i)
            i += 1
        elif lettre != "*":
            i += 1
    print(liste_index)
    chaine = []
    for lettre in mot:
        chaine.append(lettre)
    for index in liste_index:
        chaine[index] = "*"
    print(chaine)
    return ''.join(chaine)==mot_a_trous

test = correspond("test","t*s*")
print(test)