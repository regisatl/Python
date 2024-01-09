import requests
from bs4 import BeautifulSoup
import re

def extractUrlsData():
      urls = []
      request = requests.get("https://www.legalplace.fr/")
      soup = BeautifulSoup(request.content, "html.parser")
      dataText = soup.find_all("a", href=True)
    
    # Récupérer les liens href
      for link in dataText:
            baseUrl = "https://www.legalplace.fr"
            url = link['href']
            if url.startswith("https://"):
                  urls.append(url)
            elif url.startswith("/"):
                  urLink = f"{baseUrl}{url}"
                  urls.append(urLink)
            elif url.startswith("#"):
                  pass
      return urls

# Appel de la fonction et affichage des URLs
extracted_urls = extractUrlsData()


def getAllPagesScraping(link):
      requete = requests.get(link)
      soup = BeautifulSoup(requete.content, "html.parser")
      text = soup.get_text()
      finalText = re.sub(r"\s*", " ", text)
      
      wayStockData = r"C:\Users\Régis.Attolou\Documents\Github\Python\scrap_quelleenergie/legalPlace.txt"
      with open(wayStockData, "a", encoding="utf-8") as f :
            f.write(f"{link}\n") 
            f.write(f"{finalText}\n\n")


def getAllDataPages() :
      pages = extracted_urls
      for page in pages:
            getAllPagesScraping(link=page)
            print(f"On scrappe : {page} ")             
getAllDataPages()

