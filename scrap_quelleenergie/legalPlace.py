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
             print(link['href'])
      
      # for i in dataText:
      #       base_url = "https://www.legalplace.fr/"
      #       if i['href'] == " ":
      #            pass
      #       else:
      #             link_suffixe = i['href']
      #       final_url = ""
      #       if link_suffixe.startswith("https://"):
      #             final_url = link_suffixe
      #       elif link_suffixe.startswith("/"):
      #             final_url = base_url + link_suffixe
      #             if not final_url in urls:
      #                   urls.append(final_url)

      # for url in urls:
      #       print(url)

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

