import requests
from bs4 import BeautifulSoup
import re

urls = []

def extractUrlsData():
      requete = requests.get("https://www.wizishop.fr/")
      soup = BeautifulSoup(requete.content, "html.parser")
      
      dataLink = soup.find_all("a", href=True)
      
      for link in dataLink:
            baseUrl = "https://www.wizishop.fr"
            linkSuffixe = link['href']
            tempUrl = ""
            if linkSuffixe.startswith("https://"):
                  tempUrl = linkSuffixe
                  print(tempUrl)
            elif linkSuffixe.startswith(r'/[a-zA-Z0-9]+'):
                  tempUrl = baseUrl + linkSuffixe
                  print(tempUrl)
            elif linkSuffixe.startswith("#"):
                  return None
            if not tempUrl in urls:
                  urls.append(tempUrl)
      return urls

extractData = extractUrlsData()
for data in extractData:
      print(data)

# def getAllPagesScraping(link):
#       requete = requests.get(link)
#       soup = BeautifulSoup(requete.content, "html.parser")
#       text = soup.get_text()
#       finalText = re.sub(r"\s*", " ", text)
      
#       wayStockData = r"C:\Users\Régis.Attolou\Documents\Github\Python\scrap_quelleenergie/latribune.txt"
#       with open(wayStockData, "a", encoding="utf-8") as f :
#             f.write(f"{link}\n") 
#             f.write(f"{finalText}\n\n")


# def getAllDataPages() :
#       pages = extractUrlsData()
#       for page in pages:
#             getAllPagesScraping(link=page)
#             print(f"On scrappe : {page} ")             
# getAllDataPages()

