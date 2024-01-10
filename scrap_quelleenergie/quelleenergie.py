import requests
from bs4 import BeautifulSoup
import re

urls = []

def extractUrlsData():
      request = requests.get("https://www.latribune.fr/")
      soup = BeautifulSoup(request.content, "html.parser")
      
      dataText = soup.find_all("a")
      
      for i in dataText:
            if 'href' in i.attrs:  # Vérifiez si l'attribut 'href' existe
                  base_url = "https://www.latribune.fr"
                  link_suffixe = i["href"]
                  final_url = ""
                  if link_suffixe.startswith("http://") or link_suffixe.startswith("https://"):
                        final_url = link_suffixe
                  elif link_suffixe.startswith("www"):
                        final_url = "https://" + link_suffixe
                  elif link_suffixe.startswith(r"/[a-zA-Z0-9]+"):
                        final_url = base_url + link_suffixe
                        if not final_url in urls:
                              urls.append(final_url)
      return urls

def getAllPagesScraping(link):
      requete = requests.get(link)
      soup = BeautifulSoup(requete.content, "html.parser")
      text = soup.get_text()
      finalText = re.sub(r"\s*", " ", text)

      with open('latribune.txt', "a", encoding="utf-8") as f :
            f.write(f"{link}\n") 
            f.write(f"{finalText}\n\n")


def getAllDataPages() :
      pages = extractUrlsData()
      for page in pages:
            getAllPagesScraping(link=page)
            print(f"On scrappe : {page} ")             
getAllDataPages()

