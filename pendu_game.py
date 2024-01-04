dictionnaire = [
    "test",
    "vie",
    "aimer",
    "secret",
    "mystere",
    "cacher"
]

word = dictionnaire[3]

word_len = len(word)

wordMystere = ""

loop = True


while loop :
      for i in range(word_len):
            if i%2 == 0 :
                  wordMystere += word[i]
            else : 
                  wordMystere += "***"

      print(word)

      wordUser = input(f"Quel est le mot caché")

      if wordUser != word :
            print(f"Désolé le entré ne correspond pas !")
      else : 
            print(f"Félécitations vous avez trouvé le mot caché : {word}")