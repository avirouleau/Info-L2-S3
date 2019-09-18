# Consignes TP 2

Ce TP a pour but de vous faire manipuler les listes (ou tableaux).

La structure de liste apparaît naturellement lorsque l'on stocke des données:

- Stockage d'une liste de notes
- Stockage de données de localisation
- En santé : lorsque vous utilisez votre carte vitale, les données sont enregistrées dans une liste, qui résume votre parcours de soin (consultation médicale, médicaments achetés, opérations,...)

## Types de données dans une liste

Les listes que l'on rencontre le plus souvent sont :
- Les listes de nombres (des notes par exemple)
- Les listes de chaînes de caractères (par exemple, la liste des médicaments que vous avez acheté à la pharmacie durant votre vie, ou bien une liste de course)
- Les listes de... listes !

Les exemples de listes de listes sont nombreux:
- Plusieurs listes de notes que l'on souhaite stocker dans une liste (la première liste de la liste contiendra les notes d'un premier étudiant, la deuxième liste de la liste contiendra les notes d'un deuxième étudiant, etc...
- Une liste de points du plans : chaque élément de la liste est alors une liste de deux éléments (abscisse et ordonnée)
- Une liste de coordonnées GPS (typiquement ce qu'enregistre votre téléphone lorsque les données de localisation sont activées)
- Une liste de courses un peu évoluée, dans laquelle chaque élément est une liste de deux éléments (nom du produit et quantité)


## Les commandes de base sur une liste
- On peut créer une liste en écrivant `l = [1, 2]`. Souvent on crée d'abord une liste
vide avec `l=[]` pour pouvoir la remplir ensuite.
- La longueur d'une liste `l`s'obtient en écrivant `len(l)`
- Les éléments d'une liste ont un rang (ou indice), allant de **0** à `len(l)`.
On accède à l'élément de rang **i** grâce à `l[i]`.
- On peut concaténer (coller deux listes en une seule) deux listes `l1`et `l2`grâce à l'opération `l1+l2`
- On peut ajouter un élément `x`à une liste `l`en écrivant `l.append(x)`. `x`est alors ajouté en dernière position.
- On peut enlever le dernier élément d'une liste `l`en effectuant `l.pop()` (qui affiche aussi l'élément ainsi enlevé)
- On peut transformer un texte `t` en la liste des mots le composant grâce à `t.split()`.

## Des commandes que l'on va coder soi-même pour s'entraîner !


### Recherche d'un élément dans une liste

Coder une fonction `recherche` prenant en argument une liste `l` et un élément `x`, et renvoyant le nombre de fois où l'élément `x` apparaît dans la liste. On pourra également retourner la liste des positions de cet élément.

Vous pourrez tester votre fonction sur les listes du fichier `TP2.py`:
- `liste_etudiants` pour vérifier que vous êtes bien dans la liste des étudiants de L2 !
- `liste_etudiants_best`, qui contient les noms des étudiant.e.s ayant obtenu le plus haut taux de bonne réponse lors de chaque épreuve wooclap l'année dernière (cette liste est bien sûr fictive :) )

Cela peut s'appliquer dans toute sorte de liste bien concrète, par exemple pour savoir si une personne est présente sur les listes électorales, ou encore si un patient a été exposé (et combien de fois) à un médicament qui serait en fait nocif.


### Liste de nombres : moyenne, minimum et maximum

Coder les fonctions `moyenne`, `mini` et `maxi` qui prennent en argument une liste de nombres et retournent respectivement la moyenne, le minimum et le maximum des nombres dans la liste.

Vous pourrez tester vos fonctions sur la liste du fichier `TP2.py`:
- `Liste_wooclap`, qui recense les pourcentages de réussite de chacun de vous aux questions wooclap de l'année dernière (liste fictive :) )


**Extension:** Ecrire une fonction prenant en entrée une liste de listes (toutes de même taille) ainsi qu'un entier `n`, et renvoie le maximum parmi les éléments de la colonne
`n` et la liste dans laquelle se trouve ce maximum.

Créer une liste de listes et tester votre fonction dessus !


## Trier une liste

Lorsqu'on a une liste de nombres, on peut avoir envie de faire mieux que sortir le maximum et le minimum : on peut vouloir trier la liste !

On s'intéressera à cela ainsi qu'à quelques applications du tri dans le prochain TP.

En attendant, vous pouvez vous rendre [ici](https://plm.telecomnancy.univ-lorraine.fr/#/ui/lessons/sort.pancake/) pour trier une pile de pancakes à l'aide d'une spatule sans salir une assiette, ni la table, ni vos mains ! (sélectionner Python en haut à droite et cliquer sur Aide pour voir les fonctions dont vous disposez)
