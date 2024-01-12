def counter_vowels (word):
      
      voyelles = 'aeiouyAEIOUY'
      counter = 0
      
      for letter in word: 
            if letter in voyelles:
                  counter += 1
                  print(f'Les voyelles contenue dans le mot {word} sont: {letter}')
      return counter
                  
def main():
    word = input("Entrez votre mot : ")
    count = counter_vowels(word)
    print(f"Le nombre de voyelles dans le mot {word} est: {count}")
                  
if __name__ == "__main__":
      main()  
      