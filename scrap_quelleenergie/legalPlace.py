import requests
from bs4 import BeautifulSoup
import re

urls = []

def extractUrlsData():
      request = requests.get("https://www.legalplace.fr/")
      soup = BeautifulSoup(request.content, "html.parser")
      
      dataText = soup.find_all("a", href=True)
      
      # Afficher les liens href             
      for link in dataText:
            baseUrl ="https://www.legalplace.fr"
            urlsInit = []
            urlsInit.append(link['href'])
            for url in urlsInit:
                  if url.startswith("https://"):
                       print(url)
                  elif url.startswith("/"):
                        urLink = f"{baseUrl}" + url
                        print(urLink)
                  elif url.startswith("#"):
                        pass

extractUrlsData()

# def getAllPagesScraping(link):
#       requete = requests.get(link)
#       soup = BeautifulSoup(requete.content, "html.parser")
#       text = soup.get_text()
#       finalText = re.sub(r"\s*", " ", text)
      
#       wayStockData = r"C:\Users\Régis.Attolou\Documents\Github\Python\scrap_quelleenergie/flora.txt"
#       with open(wayStockData, "a", encoding="utf-8") as f :
#             f.write(f"{link}\n") 
#             f.write(f"{finalText}\n\n")


# def getAllDataPages() :
#       pages = extractUrlsData()
#       for page in pages:
#             getAllPagesScraping(link=page)
#             print(f"On scrappe : {page} ")             
# getAllDataPages()

