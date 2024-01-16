import re
import requests
from bs4 import BeautifulSoup

urls = []
baseUrl = "https://www.ooinvestir.fr/"
def extractUrlsData():
      try:
            request = requests.get(baseUrl)
            request.raise_for_status() 
      except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
      except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
      except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
      except requests.exceptions.RequestException as err:
            print(f"OOps: Something Else {err}")

      if request.status_code == 200:
            soup = BeautifulSoup(request.content, "html.parser")
      
            dataText = soup.find_all("a", href=True)
      
            for tempLink in dataText:
                 url = tempLink['href']
                 if url.startswith("https://") or url.startswith("http://"):
                        if not url in urls:
                              urls.append(url)
                 elif url.startswith(r"/[w]+"):
                        urLink = f"{baseUrl.lstrip('/')}{url}"
                        if not url in urls:
                              urls.append(urLink)
                 elif url.startswith('www'):
                      urLink = 'https://' + url
                      if not url in urls:
                              urls.append(urLink)
                 elif url.startswith("#"):
                        pass
            return urls  

extractData = extractUrlsData()

def getAllPagesScraping(link):
      try:
            requete = requests.get(link)
            requete.raise_for_status() 
      except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
      except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
      except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
      except requests.exceptions.RequestException as err:
            print(f"OOps: Something Else {err}")

      if requete.status_code == 200:
            soup = BeautifulSoup(requete.content, features="xml")

            texte = soup.get_text()
            finalText = re.sub(r"\s+", " ", texte)

            with open('data.txt', "a", encoding="utf-8") as f :
                 f.write(f"Lien: {link}\n") 
                 f.write(f"Text sur la page: {finalText}\n\n")


def getAllDataPages() :
      pages = extractData
      for page in pages:
            getAllPagesScraping(link=page)
            print(f"On scrappe : {page} ")             
getAllDataPages()