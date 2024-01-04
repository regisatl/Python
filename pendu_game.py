import random # Importe le module random pour générer des nombres aléatoires

dictionnaire = [ # Définit une liste de mots
    "test",
    "vie",
    "aimer",
    "secret",
    "mystere",
    "cacher"
]

# Cette ligne est commentée, donc elle n'est pas exécutée. Si décommentée, elle mélangerait la liste 'dictionnaire'
#word = random.shuffle(dictionnaire) 

# Sélectionne le quatrième mot de la liste 'dictionnaire' (l'indexation commence à 0 en Python)
word = dictionnaire[3]

# Calcule la longueur du mot sélectionné
word_len = len(word)

# Initialise une chaîne vide pour stocker le mot mystère
wordMystere = ""

# Initialise une variable booléenne pour contrôler la boucle while
loop = True

# Parcourt chaque caractère du mot sélectionné
for i in range(word_len):

      if i%2 == 0 : # Si l'index du caractère est pair,
            wordMystere += word[i] # ajoute le caractère à 'wordMystere'
      else : 
            wordMystere += "*" # Sinon, ajoute un astérisque à 'wordMystere'

while loop : # Tant que 'loop' est vrai,

      print(wordMystere) # imprime 'wordMystere'

      wordUser = input(f"Quel est le mot caché: ") # Demande à l'utilisateur de deviner le mot caché

      if not len(wordUser) == word_len : # Si la longueur du mot entré par l'utilisateur n'est pas égale à la longueur du mot caché,
            print(f"Désolé vous devez entrer un mot contenant {word_len} caractère !") # imprime un message d'erreur
      else : 
            if  wordUser != word : # Si le mot entré par l'utilisateur n'est pas égal au mot caché,
                  wordMystereBackup = wordMystere # sauvegarde 'wordMystere' dans 'wordMystereBackup'
                  wordMystere = "" # réinitialise 'wordMystere'
                  for i in range(word_len) : # Parcourt chaque caractère du mot entré par l'utilisateur
                        if wordUser[i] == word[i] : # Si le caractère correspond au caractère du mot caché,
                              wordMystere += word[i] # ajoute le caractère à 'wordMystere'
                        else :
                              wordMystere += wordMystereBackup[i] # Sinon, ajoute le caractère correspondant de 'wordMystereBackup' à 'wordMystere'
                              wordMystere = "" # réinitialise 'wordMystere'
                  print(f"Désolé le entré ne correspond pas !")  # Imprime un message indiquant que le mot entré par l'utilisateur ne correspond pas
            else : 
                  print(f"Félécitations vous avez trouvé le mot caché : {word}") # Si le mot entré par l'utilisateur correspond au mot caché, félicite l'utilisateur
                  loop = False # Met fin à la boucle while