# Exercice :
# 1- Créez une liste de dictionnaire, où chaque dictionnaire représente un livre avec des propriétés telles que le titre, l'auteur, et le genre.
# 2- Utilisez une boucle pour afficher les livres de chaque genre.
# 3- Créez une liste pour suivre les livres empruntés par les étudiants. Chaque élément de la liste peut être un tuple avec le titre du livre et le nom de l'emprunteur.
# 4- Utilisez une condition pour vérifier si un livre est disponible avant de l'emprunter.
# 5- Créez une fonction pour permettre aux utilisateurs de retourner un livre
# Liste des livres
livres = [
    {"titre": "The Catcher in the Rye", "auteur": "J.D. Salinger", "genre": "fiction"},
    {"titre": "1984", "auteur": "George Orwell", "genre": "fiction"},
    {"titre": "Pride and Prejudice", "auteur": "Jane Austen", "genre": "fiction"},
    {"titre": "Outliers", "auteur": "Malcolm Gladwell", "genre": "non-fiction"},
    {"titre": "The Selfish Gene", "auteur": "Richard Dawkins", "genre": "non-fiction"},
]

# Créer un dictionnaire pour organiser les livres par genre
GENRES = {}

for livre in livres:
    if livre["genre"] not in GENRES:
        GENRES[livre["genre"]] = []
    GENRES[livre["genre"]].append(livre)

for genre, livres in GENRES.items():
    print(f"{genre} livres:")
    for livre in livres:
        print(f" Titre: {livre['titre']}, Auteur: {livre['auteur']}")

# Liste des livres empruntés
livres_empruntes = []

def emprunter_livre(titre, emprunteur):
    global livres, livres_empruntes
    for livre in livres:
        if livre["titre"] == titre:
            livres_empruntes.append((titre, emprunteur))
            print(f"Livre '{titre}' emprunté avec succès par {emprunteur}.")
            return
    print(f"Livre '{titre}' n'est pas disponible.")

def retourner_livre(titre):
    global livres_empruntes
    for livre in livres_empruntes:
        if livre[0] == titre:
            livres_empruntes.remove(livre)
            print(f"Livre '{titre}' retourné avec succès.")
            return
    print(f"Livre '{titre}' n'est pas actuellement emprunté.")

# Exemple d'utilisation des fonctions
emprunter_livre("The Catcher in the Rye", "Alice")
emprunter_livre("1984", "Bob")
emprunter_livre("Pride and Prejudice", "Charlie")
emprunter_livre("Outliers", "David")

print("\nLivres empruntés:")
for livre in livres_empruntes:
    print(f" Titre: {livre['titre']}, Emprunteur: {livre['emprunteur']}")

retourner_livre("The Catcher in the Rye")
retourner_livre("1984")