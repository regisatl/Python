# Importer les modules nécessaires
import requests
from bs4 import BeautifulSoup
import re

def extract_links(url):
    # Effectuer une requête GET pour récupérer le contenu HTML de la page
    response = requests.get(url)
    
    # Analyser le contenu HTML pour créer un objet BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Utiliser la méthode find_all pour extraire tous les éléments <a>
    # Utiliser la méthode get pour extraire l'attribut href de chaque élément <a>
    links = [link.get('href') for link in soup.find_all('a')]
    
    # Retourner la liste des liens
    return links

def extract_data(url):
    # Effectuer une requête GET pour récupérer le contenu HTML de la page
    response = requests.get(url)
    
    # Analyser le contenu HTML pour créer un objet BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraire le titre de la page à partir de l'élément <title>
    data = {}
    data['title'] = soup.title.string
    
    # Extraire le contenu du paragraphe à partir de l'élément <p>
    data['body'] = ' '.join([p.text for p in soup.find_all('p')])
    
    # Retourner le dictionnaire contenant les données
    return data

def scrape_site(url):
    # Extraire tous les liens du site en utilisant la fonction extract_links
    links = extract_links(url)
    
    # Chemin vers l'emplacement du fichier .txt
    wayStockData = r"C:\Users\Régis.Attolou\Documents\Github\Python\scrap_quelleenergie/wizishop.txt"
    
    # Ouvrir un fichier en mode écriture pour stocker les données
    with open(wayStockData, 'w', encoding="utf-8") as f:
        # Parcourir tous les liens extraits
        for link in links:
            # Vérifier si le lien commence par "http"
            if link.startswith('http'):
                # Extraire les données du lien en utilisant la fonction extract_data
                data = extract_data(link)
                
                # Écrire les données dans le fichier, y compris l'URL, le titre et le contenu du paragraphe
                f.write(f"URL: {link}\n")
                f.write(f"Title: {data['title']}\n")
                f.write(f"Body: {data['body']}\n")
                f.write("\n")

# Utiliser la fonction scrape_site pour scraper un site spécifique
scrape_site('https://www.wizishop.fr/')