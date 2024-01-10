import requests
from bs4 import BeautifulSoup
import re

def extract_links(url):
    """
    Cette fonction extrait tous les liens d'une URL donnée.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    return links

def validate_link(url, base_url):

      if url is None:
            return False
      elif url.startswith('http://') or url.startswith('https://'):
            return url
      elif url.startswith('www'):
            return True
      elif url.startswith(r"/[a-zA-Z0-9]+"):
            return base_url + url
      else:
            return None

def remove_special_chars(text):
    """
    Cette fonction supprime les caractères spéciaux inutiles d'une chaîne de caractères.
    """
    text = re.sub(r'\s*', ' ', text) # Remove duplicate spaces
    return text.strip()

def extract_data(url):
    """
    Cette fonction récupère les données (titre, paragraphe, div) d'une URL donnée.
    """
    response = requests.get(url)
    response.encoding = 'utf-8'  # Ajoutez cette ligne
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {}
    
    data['title'] = remove_special_chars(soup.title.string.encode('utf-8').decode('utf-8')) if soup.title else None
    data['h1'] = ' '.join([remove_special_chars(h1.text.encode('utf-8').decode('utf-8')) for h1 in soup.find_all('h1')]) if soup.find_all('h1') else None
    data['p'] = ' '.join([remove_special_chars(p.text.encode('utf-8').decode('utf-8')) for p in soup.find_all('p')]) if soup.find_all('p') else None
    data['div'] = ' '.join([remove_special_chars(div.text.encode('utf-8').decode('utf-8')) for div in soup.find_all('div')]) if soup.find_all('div') else None

    return data


def scrape_site(url):
    """
    Cette fonction récupère tous les liens d'une URL donnée, les valide, extrait les données et les écrit dans un fichier texte.
    """
    links = extract_links(url)
    base_url = url
    valid_links = [link for link in links if validate_link(link, base_url) and link is not None]
    
    with open('blog-weproc.txt', 'w', encoding="utf-8") as f:
        for link in valid_links:
            try:
                 data = extract_data(link)
                 f.write(f"On scrape l'URL: {link}\n\n")
                 try:
                      f.write(f"Title: {data['title'].strip()}\n\n")
                 except AttributeError:
                      return None
                 try:
                      f.write(f"H1: {data['h1'].strip()}\n\n")
                 except AttributeError:
                      return None
                 try:
                      f.write(f"P: {data['p'].strip()}\n\n")
                 except AttributeError:
                      return None
                 try:
                      f.write(f"Div: {data['div'].strip()}\n\n")
                 except AttributeError:
                      return None
                 f.write("\n\n")
                 print("Scraping réussi") # Ajout d'un message de réussite
            except AttributeError:
                print("Scrapping échoué") # Ajout d'un message d'échec

scrape_site('https://blog.weproc.com/')