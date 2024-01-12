def year():
      print('Nous somme en 2024')

year()

years = 2024
def next_year():
      global years
      years += 1
      print(f'Nous sommes maintenant en {years} ')

next_year()