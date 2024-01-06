## Règles de nommage des variables

1. le nom d'une variable doit être de letttre de majuscule et de minuscule, de chiffre et du symbole underscore
2. Les accents, les espaces et les caractère spéciaux sont interdit sauf le souligné
3. Le nom d'une variable ne doit jamais commencé par un chiffre
4. Python est sensible à la casse, les majuscule et les minuscule
5. On peut nommer les variables en camelCase, le PascalCase et en kebab_case

En résumé nous avons quatre grandes méthodes de formatage de texte:

- le formatage avec la méthode d'addition ou encore appellé concaténation
- le formtage avec la méthode format avec les variables nommées
- le formatage avec les méthodes de pourcentage `%s` et` %d` `%`
- le formatage avec la méthode `f` qui consiste à mettre f au début de la chaîne avec les variables entre accolades

## Une séquences

Les données dans un tuples peut être uniquement lu, elles ne peuvent pas être modifiées ni supprimées

**\*\*\*\***\*\***\*\*\*\***COURS PYTHON**\*\*\*\***\*\***\*\*\*\***

## les listes

En Python, une liste est une structure de données qui permet de stocker une collection ordonnée d'éléments. Les listes sont des objets mutables, ce qui signifie qu'elles peuvent être modifiées après leur création.

Voici quelques-unes des méthodes et actions courantes que vous pouvez effectuer sur les listes en Python :

`append():` Ajoute un élément à la fin de la liste.
`extend():` Ajoute les éléments d'une liste (ou de tout autre itérable) à la fin de la liste courante.
`insert():` Insère un élément à une position donnée dans la liste.
`remove():` Supprime la première occurrence d'un élément donné dans la liste.
`pop():` Supprime l'élément à une position donnée dans la liste et le renvoie.
`index():` Renvoie la position de la première occurrence d'un élément donné dans la liste.
`count():` Renvoie le nombre d'occurrences d'un élément donné dans la liste.
`sort():` Trie les éléments de la liste dans l'ordre croissant.
`reverse():` Inverse l'ordre des éléments dans la liste.

Voici un exemple d'utilisation de ces méthodes :

```py
# Créer une liste
ma_liste = [1, 2, 3, 4, 5]

# Ajouter un élément à la fin de la liste
ma_liste.append(6)

# Ajouter les éléments d'une autre liste à la fin de la liste courante
ma_liste.extend([7, 8, 9])

# Insérer un élément à une position donnée dans la liste
ma_liste.insert(3, 10)

# Supprimer la première occurrence d'un élément donné dans la liste
ma_liste.remove(5)

# Supprimer l'élément à une position donnée dans la liste et le renvoyer
element_supprime = ma_liste.pop(2)

# Renvoyer la position de la première occurrence d'un élément donné dans la liste
position = ma_liste.index(4)

# Renvoyer le nombre d'occurrences d'un élément donné dans la liste
nombre_occurrences = ma_liste.count(2)

# Trier les éléments de la liste dans l'ordre croissant
ma_liste.sort()

# Inverser l'ordre des éléments dans la liste
ma_liste.reverse()

```

## Les tuples

En Python, un tuple est une autre structure de données qui permet de stocker une collection ordonnée d'éléments. Les tuples, comme les listes, sont des objets mutables, ce qui signifie qu'ils peuvent être modifiés après leur création.

Voici quelques-unes des méthodes et actions courantes que vous pouvez effectuer sur les tuples en Python :
`index(): `Renvoie le plus petit numéro d'index correspondant à l'élément donné dans le tuple.
`count(): `Renvoie le nombre de fois où l'élément donné est présent dans le tuple.

`- et \*: `Les opérateurs de concaténation et de répétition pour les tuples.
  `tuple(): `Convertit une liste en tuple.
  Voici un exemple d'utilisation de ces méthodes et actions :

```py
# Créer un tuple
ma_tuple = (1, 2, 3, 4, 5)

# Accéder à un élément d'un tuple
ma_tuple_element = ma_tuple[2]

# Compter l'occurrence d'un élément dans un tuple
occurrence = ma_tuple.count(3)

# Concaténation de tuples
ma_tuple_concatene = ma_tuple + (6, 7, 8)

# Répétition de tuple
ma_tuple_repe = ma_tuple * 2

# Convertir une liste en tuple
ma_liste = [1, 2, 3, 4, 5]
ma_tuple_liste_to_tuple = tuple(ma_liste)


```

## Les dictionnaires

Un dictionnaire en Python est une structure de données qui permet de stocker des paires clé-valeur. Voici un aperçu des méthodes et actions courantes que l'on peut effectuer sur les dictionnaires en Python :
`Création d'un dictionnaire :` On peut créer un dictionnaire en Python en plaçant les items entre accolades, séparés par des virgules. Chaque item est entré en plaçant `successivement :` la clé, le séparateur deux-points, la valeur de la clé.
`Accès aux éléments :` On peut accéder aux éléments d'un dictionnaire en utilisant la clé comme indice.
`Ajout et modification d'éléments : `On peut ajouter de nouveaux éléments à un dictionnaire ou modifier les éléments existants en utilisant la notation d'indexation.
`Suppression d'éléments :` On peut supprimer des éléments d'un dictionnaire en utilisant l'instruction del ou la méthode pop().
`Méthodes de dictionnaire :` Les dictionnaires en Python disposent de plusieurs méthodes intégrées telles que keys(), values(), items(), get(), update(), pop(), popitem(), clear(), etc.
`Itération sur un dictionnaire :` On peut itérer sur les clés, les valeurs ou les paires clé-valeur d'un dictionnaire en utilisant des boucles for et les méthodes keys(), values() et items().
`Copie de dictionnaire : `On peut créer une copie indépendante d'un dictionnaire en utilisant la méthode copy().
`Fusion de dictionnaires :` La méthode update() permet de fusionner deux dictionnaires.
Les dictionnaires en Python sont des structures de données très flexibles et polyvalentes, et ils sont largement utilisés pour stocker et manipuler des données de manière efficace.

```py
# Créer un dictionnaire
mon_dictionnaire = {"voiture": "véhicule à quatre roues", "vélo": "véhicule à deux roues"}

# Accéder à un élément d'un dictionnaire
mon_dictionnaire_element = mon_dictionnaire["voiture"]

# Ajouter un élément à un dictionnaire
mon_dictionnaire["moto"] = "véhicule à deux roues"

# Modifier un élément d'un dictionnaire
mon_dictionnaire["voiture"] = "véhicule à moteur"

# Supprimer un élément d'un dictionnaire
del mon_dictionnaire["vélo"]

# Itérer sur les clés d'un dictionnaire
for cle in mon_dictionnaire.keys():
    print(cle)

# Itérer sur les valeurs d'un dictionnaire
for valeur in mon_dictionnaire.values():
    print(valeur)

# Itérer sur les paires clé-valeur d'un dictionnaire
for cle, valeur in mon_dictionnaire.items():
    print(cle, valeur)

# Copier un dictionnaire
mon_dictionnaire_copie = mon_dictionnaire.copy()

# Fusionner deux dictionnaires
mon_dictionnaire_fusionne = {"moto": "véhicule à deux roues", "camion": "véhicule à quatre roues"}
mon_dictionnaire.update(mon_dictionnaire_fusionne)


```

## les sets

Un set en Python est une collection d'éléments non ordonnés, où chaque élément est unique (pas de doublons) et doit être immuable (ne peut pas être modifié) 
1
. Voici un aperçu des méthodes et actions courantes que l'on peut effectuer sur les sets en Python :

`Création d'un set`
`Ajout d'un élément à un set`
`Suppression d'un élément d'un set`
`Vérifier si un élément existe dans un set`
`Itération sur un set`

Voici des exemples d'utilisation de ces méthodes et actions :
```py
# Créer un set
mon_set = {"A", "B", "C"}

# Ajouter un élément à un set
mon_set.add("D")

# Supprimer un élément d'un set
mon_set.remove("B")

# Vérifier si un élément existe dans un set
if "A" in mon_set:
    print("A est présent dans le set")

# Itérer sur un set
for élément in mon_set:
    print(élément)

```
Les sets en Python permettent également d'effectuer des opérations mathématiques sur les ensembles, telles que l'union (|), l'intersection (&) et la différence symétrique (^) 
2
. Chacune de ces opérations a une méthode correspondante pour effectuer l'opération sur un set :
`Union : `mon_set1 | mon_set2
`Intersection :` mon_set1 & mon_set2
`Difference symétrique :` mon_set1 ^ mon_set2
Enfin, vous pouvez convertir un set en une liste ou un tuple pour effectuer des opérations qui ne sont pas définies sur les sets, puis convertir à nouveau le set si nécessaire
5