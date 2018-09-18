def carre(n)
return n*n

##########

def fonction1(n):
# retourne la somme 1+2+...+n
    s = 0
    for i in range(n):
        s = s + i
    return s

##########

def premiers_carres(k):
# affiche les k premiers carrés : 1^2, 2^2, ..., k^2
    for i in range(k):
        print carre(i)

def premiers_carres(k):
# idem
    i=0
while i < k:
        print carre(i)
        i=i+1

# les deux lignes suivantes doivent permettre d'afficher les carrés jusqu'au
# rang choisi par l'utilisateur
k = input("Entrez un nombre : ")
print(premiers_carres (k))

##########

# retourne si le nombre est pair ou non
def est_pair(n):
    if n % 2 = 0
        return True

##########


# prend en entrée une chaîne de caractères et renvoie le nombre de voyelles
def nb_voyelles(u):
    for c in u:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            voyelles = voyelles + 1
            return voyelles

def nb_voyelles(u):
# idem
    voyelles = 0
    i=1
    while i < len(u):
        c = u(i)
    if ('a' or 'e' or 'i' or 'o' or 'u')==c:
        voyelles = voyelles + 1
        i = i+1
    return voyelles


def nb_voyelles(u):
# idem
    voyelles = 0
    for c in u:
        if c in 'aeiou':
            voyelles += 1
            return voyelles

##########

def convert_g_kg(l):
    # prend une liste de masses en grammes et renvoie la liste en kg
    return l * 1000

##########

def add_liste(l1, l2):
    # prend deux listes de même taille en entrée et renvoie la liste contenant
    # les sommes des éléments de même rang dans l1 et l2
    return l1 + l2

##########

def pile_face():
    # effectue un tirage de pile ou face
    if rand()<0,5:
        print("Pile")
    else:
        print("Face")

##########

def count_distance(pos, n)
# déplacement aléatoire dans Z, évalue la distance entre la position initiale et
# la position d'arrivée au bout de n pas
    new_pos = pos
    for i in range(n):
        new_pos = new_pos + random.choice([-1, 1])
    return abs(new_pos - pos)

##########

print ("Ce script recherche le plus grand de trois nombres")
print ('Veuillez entrer trois nombres séparés par des virgules : ')

3nombres = input()
max, index = 3nombres[0], 'premier'
if 3nombres[1] > max:
    max = 3nombres[1]
    index = 'second'
if 3nombres[2] > max:
    max = 3nombres[2]
    index = 'troisième'
print ("Le plus grand de ces nombres est" max)
print ("Ce nombre est le" index "de votre liste.")

##########




# Ecrire une fonction qui prend en entrée deux points du plan et renvoie
# l'équation de la droite passant par ces points



# Ecrire une fonction qui renvoie l'impot sur le revenu en fonction du
# salaire net imposable
