import requests
from bs4 import BeautifulSoup
import re

urls = []
def extractUrlsData():
      request = requests.get("https://flora.insure/fr")
      soup = BeautifulSoup(request.content, "html.parser")
      dataText = soup.find_all("a", href=True)
    
    # Récupérer les liens href
      for link in dataText:
           urLink = link['href']
           if not urLink in urls:
                  urls.append(urLink)
      return urls           

# Appel de la fonction et affichage des URLs
extracted_urls = extractUrlsData()

def getAllPagesScraping(link):
      requete = requests.get(link)
      soup = BeautifulSoup(requete.content, "html.parser")
      text = soup.get_text()
      finalText = re.sub(r"\s*", " ", text)
      
      wayStockData = r"C:\Users\Régis.Attolou\Documents\Github\Python\scrap_quelleenergie/floraInsure.txt"
      with open(wayStockData, "a", encoding="utf-8") as f :
            f.write(f"{link}\n") 
            f.write(f"{finalText}\n\n")


def getAllDataPages() :
      pages = extracted_urls
      for page in pages:
            getAllPagesScraping(link=page)
            print(f"On scrappe : {page} ")             
getAllDataPages()

