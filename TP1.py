def carre(n)
    """
    Parameter
    ---------
    n : nombre entier

    Return
    ------
    le carré de n
    """
return n*n


def fonction1(n):
    """
    Parameter
    ---------
    n : nombre entier positif

    Return
    ------
    la somme des entiers de 1 à n
    """
    s = 0
    for i in range(n):
        s = s + i
    return s



def premiers_carres(k):
    """
    Parameter
    ---------
    k : nombre entier positif

    Return
    ------
    Affiche les k premiers carrés de nombres
    """
    for i in range(k):
        print carre(i)

def premiers_carres(k):
    """
    Parameter
    ---------
    k : nombre entier positif

    Return
    ------
    Affiche les k premiers carrés de nombres
    """
    i=0
while i < k:
        print carre(i)
        i=i+1


def est_pair(n):
    """
    Parameter
    ---------
    n : nombre entier positif

    Return
    ------
    Boolean : True si n est pair, False sinon
    """
    if n % 2 = 0
        return True


def nb_voyelles(u):
    """
    Parameter
    ---------
    u : une chaîne de caractères

    Return
    ------
    Nombre de voyelles contenues dans u
    """
    for c in u:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            voyelles = voyelles + 1
            return voyelles


def nb_voyelles(u):
    """
    Parameter
    ---------
    u : une chaîne de caractères

    Return
    ------
    Nombre de voyelles contenues dans u
    """
    voyelles = 0
    for c in u:
        if c in 'aeiou':
            voyelles += 1
            return voyelles


def convert_g_kg(l):
    """
    Parameter
    ---------
    l : une liste de masses (en grammes)

    Return
    ------
    Une liste des masses converties en kilogrammes
    """
    return l * 1000


def add_liste(l1, l2):
    """
    Parameter
    ---------
    l1 : une liste
    l2 : une liste de même taille que l1

    Return
    ------
    Une liste contenant la somme des deux listes : L[i] = l1[i] + l2[i]
    """
    return l1 + l2


def pile_face():
    """
    Parameter
    ---------
    aucun

    Return
    ------
    Pile ou Face
    """
    if rand()<0,5:
        print("Pile")
    else:
        print("Face")


def count_distance(pos, n)
    """
    Parameter
    ---------
    pos : un nombre entier
    n : un nombre entier positif

    Return
    ------
    Calcule la distance entre la position initiale pos et la position finale
    après une marche aléatoire de n pas sur les entiers relatifs
    """
    new_pos = pos
    for i in range(n):
        new_pos = new_pos + random.choice([-1, 1])
    return abs(new_pos - pos)
