# Consignes TP3

Ce TP aborde de nouveau les listes, que nous avons manipulé dans le TP précédent.


Les questions naturelles lorsqu'on a une liste est :
- Peut-on la trier ?
- Comment la trier ?
- Comment la trier assez rapidement ?

Trier une liste c'est la ranger dans un ordre donnée (ordre alphabétique pour des mots, ordre croissant ou décroissant pour des nombres,...)
Du tri on en a tous déjà fait ! Du tri de cartes, notamment. Et si vous jouez au tarot vous devez déjà avoir vu des différences de stratégie et de rapidité pour trier les cartes.

Avant de lire la suite, essayez de vous imaginer en train de trier une liste de nombres ou de cartes.

Quelle stratégie adopteriez-vous ?

Essayer de décrire de manière claire votre méthode.

C'est fait ?

\_

(Vous êtes sûrs ?)

\_

Alors avec un peu de chance votre méthode est l'une des deux décrites dans les deux premiers exercices ci-dessous, il ne reste qu'à la coder ! (Si ce n'est pas le cas, n'hésitez pas à coder votre propre méthode !!)

**Remarque:** si vous voulez trier une liste sans modifier la liste initiale, la commande `l[:]` permet de créer une copie de la liste `l`. Ainsi `l2 = l[:]` crée une liste `l2` qui est une copie de la liste `l`, que l'on peut modifier sans affecter `l`.


## Exercice 1 : Stratégie "du minimum"

Il s'agit ici de trier notre liste en ordre croissant (on pourrait facilement adapter pour l'ordre décroissant !)

La stratégie est la suivante : on a notre liste, celui qu'on doit mettre en premier c'est clair c'est le minimum de la liste ! On peut donc:
- Echanger le premier élément de la liste avec le minimum de la liste

Maintenant que le premier élément est le bon, qui est le deuxième ? C'est le minimum de tout le reste, et donc rebelote !

Il vous reste à coder tout cela :smile: (par exemple dans une fonction que vous pouvez appeler `tri_croissant` et qui prendra en entrée une liste à trier). Vous pouvez :
- Réutiliser ou s'inspirer de la fonction du TP précédent qui permet de trouver le minimum d'une liste
- Définir une fonction prenant en entrée une liste ainsi que deux positions *i*  et *j* et renvoie la liste avec les éléments des positions *i* et *j* échangés
- Tester votre code sur une liste d'un TP précédent ou bien sur une liste que vous créez vous-même.

**Remarque :** Les commandes suivantes peuvent être ou ne pas être utiles:
- `l[:i]` permet d'extraire la liste des *i* premiers éléments de la liste `l`
- `l[i:]` permet d'extraire la liste des éléments de `l` en partant du rang *i* (c'est donc la liste `l` à laquelle on a enlevé les *i* premiers éléments)


## Exercice 2 : Stratégie du "C'est où que je le mets celui-là ?"

Restons toujours sur l'idée de trier par ordre croissant.

Pourquoi se casser la tête à chercher le minimum ? Au lieu de cela, une autre stratégie possible est de prendre les nombres (ou les cartes) commes elles viennent et de placer chaque nouvelle carte au bon endroit. Par exemple, le premier nombre de la liste je le mets en première position puisque pour l'instant c'est le seul que j'ai vu ! Le deuxième, je dois le comparer au premier pour savoir si j ele mets avant ou après, etc... Cela signifie qu'il va falloir créer un décalage pour insérer l'élément !

Coder ainsi une fonction `tri_ouquilva` prenant en entrée une liste à trier. Pour chaque élément à ranger vous devez penser à :
- Trouver l'endroit où il doit s'insérer
- Créer le décalage nécessaire à l'insertion de l'élément
- Insérer l'élément

N'oubliez pas de tester votre fonction sur une liste d'un TP précédent ou bien sur une liste que vous créez vous-même.


## Exercice 3 : Trier une liste de listes

**Remarque:** une liste de listes peut être visualisée comme une matrice. Pourquoi, comment ?
- On sait que `l[i]` donne accès à l'élément de rang `i` de la liste `l`. Si `l` est une liste de listes, `l[i]` est donc une liste !
- `l[i][j]` permet donc d'accéder à l'élément de rang `j` de la liste de rang `i` !
- Il est donc "naturel" de voir la liste de liste comme une matrice dont les lignes sont les listes de la liste.

Mais du coup trier une liste de listes ça veut dire quoi ? Il s'agit de trier selon une colonne :
- On réarrange la liste de liste, de sorte que la première liste devient celle contenant le premier élément de la colonne ordonnée, la deuxième liste est celle du deuxième élément de la colonne ordonnée, etc...
- On peut s'inspirer de la stratégie du minimum, mais au lieu d'échanger deux nombres on échange deux listes !

## Exercice 4 : Application à l'analyse de fréquences

Dans le fichier `TP3.py` vous trouverez un texte relativement long. Le but est de calculer les fréquences d'apparition de chaque lettre de l'alphabet dans ce texte. Pour vous aider:
- `for c in texte` fait parcourir à la variable `c` tous les caractères de la chaîne de caractère `texte`
- Pour chaque lettre de l'alphabet, il faut compter combien de fois elle apparaît dans le texte.
- La commande `texte.lower()` permet de transformer tous les caractères de la chaîne `texte` en minuscules.
- La commande `list(texte)` permet de transformer un texte en une liste de caractères (découpage lettre par lettre du texte)

Afficher ensuite la liste des lettres par ordre croissant (ou décroissant) de fréquence d'apparition.

## Pour aller plus loin : Diviser pour régner et récursivité.

Quelques questions exploratoires pour vous permettre de coder un nouvel algorithme de tri :
- Qu'est-ce qu'une fonction récursive ?
- Est-il facile de fusionner deux listes triées en une liste triée ?
- En déduire un algorithme récursif de tri et comparer sa rapidité face aux deux tris précédents
