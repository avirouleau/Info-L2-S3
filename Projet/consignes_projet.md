# Consignes Projet

Le projet se fait par groupe de deux ou trois personnes

Ce fichier décrit rapidement en quoi consistent les données du projet. Vous les trouverez dans un fichier .csv nommé `donnees_projet`.

Vous disposez par ailleurs d'une grille critériée (envoyée par mail !) qui vous permettra de comprendre nos attentes quant au compte-rendu du projet.

## Les données

Elles contiennent des points d'XP pour 100 étudiants de l'Institut dans 4 thèmes différents d'une UE de mathématiques.

Les données dans le fichier .csv sont de la forme suivante :
- La première ligne contient Les plafonds d'XP pour chaque thème, ainsi que l'entête de la dernière colonne ('Validation').
- Chacune des 100 lignes suivantes représente les données d'un étudiant, c'est-à-dire les XP obtenus dans chaque thème ainsi que le nombre `1` ou `0` qui correspond au fait que l'étudiant a validé ou non l'UE.

## Pour bien démarrer

- Il est crucial de démarrer en définissant des problématiques, c'est-à-dire les questions auxquelles vous voulez répondre en analysant ces données.
- Il est non moins crucial de pouvoir lire ces données en Python ! Vous pouvez exécuter le code ci-dessous pour importer les données sous forme de liste :

```python
import csv

with open('donnees_projet', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
```

Attention à placer le fichier au bon endroit. Par exemple dans Spyder vous devez placer le fichier de données dans le même dossier que votre script pour que les lignes ci-dessus s'exécutent correctement !

- L'esprit d'un projet d'analyse de données n'est pas forcément de tout coder soi-même. Plein de fonctions existent déjà, servez-vous en !

- Une structure de données qui pourra vous intéresser sont les numpy array. Cela se manipule grosso modo comme des listes, avec quelques commandes supplémentaires et en particulier un bon nombre de fonctions déjà existantes. Une liste `L` contenant des nombres se transforme en un tableau numpy array (une matrice), grâce à la commande `numpy.array(L).astype(np.float)`
