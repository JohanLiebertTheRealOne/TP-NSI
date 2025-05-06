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

# def correspond(mot,mot_a_trous):
    # if len(mot) != len(mot_a_trous):
        # return False
    # liste_index = []
    # i =  0
    # for lettre in mot_a_trous:
        # if lettre == "*":
            # liste_index.append(i)
            # i += 1
        # elif lettre != "*":
            # i += 1
    # print(liste_index)
    # chaine = []
    # for lettre in mot:
        # chaine.append(lettre)
    # for index in liste_index:
        # chaine[index] = "*"
    # print(chaine)
    # return ''.join(chaine)==mot_a_trous

# adj = [[1, 2], [2], [0], [0]]

def voisins_entrants(adj:list, x):
    voisin_liste = []
    index = 0
    for g in adj:
        if x in g:
            voisin_liste.append(index)
        index += 1
    return voisin_liste


assert voisins_entrants([[1, 2], [2], [0], [0]], 0)==[2, 3]

def max_et_indice(tab:list)->tuple:
    max = 0
    indice_max = 0
    for nombre in tab:
        if nombre > max:
            max = nombre
            indice_max += 1
    indice_max -= 1
    return max,indice_max

assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])==(9, 3)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

assert fibonacci(25)==75025

def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []
    for i in range(len(eleves)):
        if notes[i] == ...:
            meilleurs_eleves.append(...)
        elif notes[i] > note_maxi:
            note_maxi = ...
            meilleurs_eleves = [...]
    return (note_maxi, meilleurs_eleves)

def recherche(tab:list,n:int):
    index = 0
    for valeur in tab:
        if valeur==n:
            return index
        index += 1
    return None

assert recherche([2,4],2)==0

def distance_carre(point1, point2):
    """ Calcule et renvoie la distance au carre entre
    deux points."""
    return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2

def point_le_plus_proche(depart, tab):
    """ Renvoie les coordonnées du premier point du tableau tab se
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = distance_carre(min_point,depart)
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < min_dist:
            min_point = tab[i]
            min_dist = distance_carre(min_point,depart)
    return min_point

assert distance_carre((1, 0), (5, 3))==25
assert point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)])==(5, 2)

def moyenne(notes:list)->float:
    somme = 0
    n = len(notes)
    for note in notes:
        somme += note[0]*note[1]
    return somme/n

class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None),
Noeud(0, None,
Noeud(7, None, None)))

def taille(arb:Noeud):
    if arb==None:
        return 0
    return 1 + taille(arb.gauche) + taille(arb.droit)

def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = element
        tab_ins[...] = ...
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = ...
    return tab_ins