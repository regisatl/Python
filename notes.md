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

## Les expressions régulières

Les expressions régulières (ou RegEx) sont des séquences de caractères qui définissent un motif de recherche. En Python, les expressions régulières sont implémentées dans le module re. Voici quelques méthodes et actions courantes que l'on peut effectuer avec les expressions régulières en Python :

`Recherche de motifs : `On peut rechercher des motifs dans une chaîne de caractères en utilisant la méthode search() ou match().
`Recherche de toutes les occurrences :` On peut rechercher toutes les occurrences d'un motif dans une chaîne de caractères en utilisant la méthode findall().
`Remplacement de motifs `: On peut remplacer des motifs dans une chaîne de caractères en utilisant la méthode sub().
`Utilisation de caractères spéciaux :` Les expressions régulières en Python utilisent des caractères spéciaux pour définir des motifs, tels que . pour n'importe quel caractère, * pour zéro ou plusieurs occurrences, + pour une ou plusieurs occurrences, ? pour zéro ou une occurrence, ^ pour le début de la chaîne, $ pour la fin de la chaîne, etc.
`Utilisation de classes de caractères :` Les classes de caractères permettent de définir un ensemble de caractères possibles pour un motif, tels que [a-z] pour toutes les lettres minuscules, [1][2][3][4][5] pour tous les chiffres, etc.
`Utilisation de groupes de capture :` Les groupes de capture permettent de capturer des parties spécifiques d'un motif en utilisant des parenthèses.

Voici quelques exemples d'utilisation de ces méthodes et actions :

```py
import re

# Recherche de motifs
texte = "Bonjour tout le monde"
motif = "tout"
resultat = re.search(motif, texte)
print(resultat.group())

# Recherche de toutes les occurrences
texte = "Bonjour tout le monde"
motif = "o"
resultat = re.findall(motif, texte)
print(resultat)

# Remplacement de motifs
texte = "Bonjour tout le monde"
motif = "tout"
remplacement = "rien"
resultat = re.sub(motif, remplacement, texte)
print(resultat)

# Utilisation de caractères spéciaux
texte = "Bonjour tout le monde"
motif = "^Bonjour"
resultat = re.search(motif, texte)
print(resultat.group())

# Utilisation de classes de caractères
texte = "Bonjour tout le monde"
motif = "[a-z]+"
resultat = re.findall(motif, texte)
print(resultat)

# Utilisation de groupes de capture
texte = "Bonjour tout le monde"
motif = "(Bonjour) (tout)"
resultat = re.search(motif, texte)
print(resultat.group(1))
print(resultat.group(2))

```
## Listes des commandes dans un projet python

Voici une liste de commandes Python utiles pour un projet Python :

1. Exécuter un fichier Python : `python <nom_du_fichier.py>`
2. Exécuter du code Python sans ouvrir un fichier : `python -c "print('Hello, World!')"`
3. Exécuter un module Python en tant que script : `python -m <module_name>`
4. Installer un paquet Python avec pip : `pip install <package>`
5. Lister les paquets Python installés : `pip list` ou `pip freeze`
6. Importer un paquet Python dans un script : `import <package>`
7. Vérifier la version de Python que vous exécutez : `python -V`
8. Utiliser l'interpréteur Python dans un terminal : `python -i`
9. Exécuter des commandes Python depuis l'entrée standard : `python -c "print('Hello, World!')"`
10. Exécuter du code Python contenu dans un fichier .py : `python <nom_du_fichier.py>`
11. Exécuter du code Python contenu dans un script .pyo : `python <nom_du_fichier.pyo>`
12. Exécuter du code Python contenu dans un script .pyc : `python <nom_du_fichier.pyc>`
13. Exécuter du code Python contenu dans un script .pycu : `python <nom_du_fichier.pycu>`
14. Exécuter du code Python contenu dans un script .pyd : `python <nom_du_fichier.pyd>`
15. Exécuter du code Python contenu dans un script .pyz : `python <nom_du_fichier.pyz>`

N'oubliez pas que vous pouvez utiliser la documentation de Python pour obtenir des informations supplémentaires sur les commandes et les options disponibles[2].

Citations:

[1] https://kinsta.com/fr/blog/commandes-python/
[2] https://docs.python.org/fr/3/using/cmdline.html
[3] https://python.developpez.com/exercices/?page=Les-chaines-de-caracteres
[4] https://www.math.univ-toulouse.fr/~pmaillar/cours/modelisation2020/liste%20de%20commandes%20Python.pdf
[5] https://openclassrooms.com/fr/courses/6951236-mettez-en-place-votre-environnement-python/7013523-gerez-des-paquets-python

La gestion des dépendances dans un projet Python est essentielle pour assurer la cohérence et la reproductibilité du code. Voici quelques commandes et outils couramment utilisés pour gérer les dépendances dans un projet Python :

1. **pip** : Pip est le gestionnaire de paquets par défaut pour Python. Il est utilisé pour installer et gérer les dépendances d'un projet. Quelques commandes utiles :
   - `pip install <package>` : Installe un paquet Python.
   - `pip uninstall <package>` : Désinstalle un paquet Python.
   - `pip list` : Liste les paquets installés.
   - `pip freeze` : Génère une liste des paquets installés avec les versions, utile pour la reproductibilité du projet.

2. **Pipenv** : Pipenv est un outil de gestion d'environnements virtuels et de dépendances. Il combine pip et virtualenv dans un seul outil. Quelques commandes utiles :
   - `pipenv install <package>` : Installe un paquet et le rajoute à Pipfile.
   - `pipenv uninstall <package>` : Désinstalle un paquet et le retire de Pipfile.
   - `pipenv lock` : Génère un fichier Pipfile.lock basé sur les dépendances actuelles et leurs versions.

3. **Poetry** : Poetry est un outil de gestion de dépendances et de packaging pour Python. Il permet de déclarer les dépendances d'un projet dans un fichier pyproject.toml.

4. **pip-tools** : L'outil pip-tools est utilisé pour construire des fichiers de dépendances cohérents. Quelques commandes utiles :
   - `pip-compile` : Génère un fichier requirements.txt basé sur les dépendances déclarées dans un fichier.in.
   - `pip-sync` : Installe les paquets spécifiés dans un fichier requirements.txt, en supprimant les paquets non spécifiés.

Ces outils et commandes sont largement utilisés dans la communauté Python pour gérer les dépendances des projets. Il est recommandé de choisir l'outil qui convient le mieux à vos besoins et à la structure de votre projet.

Citations:
[1] https://www.docstring.fr/blog/gerer-efficacement-les-dependances-de-vos-projets/
[2] https://blog.stephane-robert.info/post/python-pipx-piptools-pipdeptree/
[3] https://moisio.fr/2022/05/09/python-gestion-des-packages-et-des-dependances/
[4] https://makina-corpus.com/python/gerer-ses-dependances-de-paquets-python
[5] https://www.math.univ-toulouse.fr/~pmaillar/cours/modelisation2020/liste%20de%20commandes%20Python.pdf

`python.exe -m pip install --upgrade pip`

## Les fonctions en python

1. Définitions de fonction en python
   Les fonctions en Python sont des blocs de code réutilisables qui peuvent être définis pour effectuer une tâche spécifique. Les fonctions sont définies en utilisant le mot-clé def suivi du nom de la fonction et de la liste des paramètres entre parenthèses. Le bloc de code de la fonction est indenté sous la déclaration de la fonction.

- Exemple:
```py
  def greet(name):
    print(f"Hello, {name}!")
```
2. Paramètres et arguments
    Les paramètres sont des variables déclarées dans la définition de la fonction qui représentent les entrées de la fonction. Les arguments sont les valeurs réelles fournies pour les paramètres lors de l'appel de la fonction.

- Exemple :
```py
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30) # name="Alice", age=30
```
3. Fonctions sans paramètres
    Les fonctions peuvent être définies sans paramètres.

- Exemple :
```py
def say_hello():
    print("Hello!")

say_hello() # "Hello!"
```
4. Fonctions avec des paramètres par défaut
    Les paramètres de fonction peuvent avoir des valeurs par défaut qui seront utilisées si aucune valeur n'est fournie lors de l'appel de la fonction.

- Exemple :
```py
def greet(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice") # name="Alice", age=30
greet("Bob", 25) # name="Bob", age=25
```
5. Arguments variadiques
    Les fonctions peuvent accepter un nombre variable d'arguments en utilisant le signe * dans la définition de la fonction.

- Exemple :
```py
def print_all(*args):
    for arg in args:
        print(arg)

print_all("Hello", "world!") # "Hello", "world!"
```
6. Fonctions à renvoi
    Les fonctions peuvent renvoyer une valeur en utilisant le mot-clé return. Une fois que return est exécuté, la fonction se termine et la valeur renvoyée est utilisée comme résultat de la fonction.

Exemple :
```py
def add(a, b):
    return a + b

result = add(3, 4) # result=7
```

7. Fonctions en tant qu'objets
    En Python, les fonctions sont des objets de première classe, ce qui signifie qu'elles peuvent être utilisées comme des variables, affectées à d'autres variables, passées en argument à d'autres fonctions et renvoyées en tant que résultat de fonction.

Exemple :
```py
def add(a, b):
    return a + b

def apply(func, a, b):
    return func(a, b)

result = apply(add, 3, 4) # result=7
```
8. Utilisation de fonctions anonymes (lambda)
     Python, les fonctions anonymes peuvent être définies en utilisant la syntaxe lambda. Les fonctions lambda sont généralement plus courtes et moins complexes que les fonctions régulières.

Exemple :
```py
greet = lambda name: print(f"Hello, {name}!")

greet("Alice") # "Hello, Alice!"
```
## Les classes 

1. Introduction
    Dans ce guide, nous aborderons les bases des classes et des objets en Python. Les classes sont des modèles ou des blueprints pour la création d'objets, tandis que les objets sont des instances de classes qui représentent des entités spécifiques dans un programme.

Response: 
2. Classes
    Une classe est un modèle ou un blueprint pour la création d'objets. En Python, une classe est définie à l'aide du mot-clé class, suivi du nom de la classe et de deux points. Voici un exemple de définition de classe:
    ```py
        class MonAnimal:
        pass
    ```
Dans cet exemple, la classe MonAnimal est définie sans `attributs` ni `méthodes`.

Response: 
3. Attributs
    Les attributs sont des variables associées à une instance de classe. En Python, les attributs peuvent être définis à l'intérieur ou à l'extérieur d'une méthode (comme __init__ pour l'initialisation). Voici un exemple de définition d'attributs:
    ```py
    class MonAnimal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    ```
Dans cet exemple, la classe ``MonAnimal`` possède deux attributs: `nom` et `age`.

Response: 
4. Méthodes
    Les méthodes sont des fonctions associées à une instance de classe. En Python, les méthodes sont définies à l'intérieur d'une classe. Voici un exemple de définition d'une méthode:
    ```py
    class MonAnimal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def manger(self):
        print(f"{self.nom} mange.")
    ```
Dans cet exemple, la classe MonAnimal possède une méthode appelée `manger`.

Response: 
5. Objets
    Un objet est une instance de classe qui représente une entité spécifique dans un programme. En Python, un objet est créé en appelant une classe avec les arguments nécessaires pour l'initialisation des attributs. Voici un exemple de création d'un objet:
    ```py
    mon_animal = MonAnimal("Chat", 5)
    ```

Dans cet exemple, la variable mon_animal est un objet de la classe `MonAnimal`.

Response: 
6. Utilisation des objets
    Les objets peuvent être utilisés pour accéder et manipuler leurs attributs et méthodes. Voici un exemple d'utilisation d'un objet:
    ```py
    mon_animal.manger()
    print(mon_animal.nom)
    print(mon_animal.age)
    ```
Dans cet exemple, la méthode manger de l'objet `mon_animal` est appelée pour afficher un message. Les attributs nom et age de l'objet `mon_animal` sont également accédés et affichés.

En conclusion, les classes et les objets en Python sont des éléments essentiels pour la programmation orientée objet. Les classes sont des modèles ou des blueprints pour la création d'objets, tandis que les objets sont des instances de classes qui représentent des entités spécifiques dans un programme.








