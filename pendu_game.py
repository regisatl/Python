import random

dictionnaire = [
    "test",
    "vie",
    "aimer",
    "secret",
    "mystere",
    "cacher"
]

#word = random.shuffle(dictionnaire)

word = dictionnaire[3]

word_len = len(word)

wordMystere = ""

loop = True

for i in range(word_len):
      if i%2 == 0 :
            wordMystere += word[i]
      else : 
            wordMystere += "*"

while loop :

      print(wordMystere)

      wordUser = input(f"Quel est le mot caché: ")

      if not len(wordUser) == word_len :
            print(f"Désolé vous devez entrer un mot contenant {word_len} caractère !")
      else : 
            if  wordUser != word :
                  print(f"Désolé le entré ne correspond pas !")
            else : 
                  print(f"Félécitations vous avez trouvé le mot caché : {word}")
                  loop = False