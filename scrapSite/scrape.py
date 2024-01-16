import re
import requests
from bs4 import BeautifulSoup

urls = []
baseUrl = "https://www.nexity.fr/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}

def extractUrlsData():
      try:
            request = requests.get(baseUrl, headers=headers, timeout=10)
            request.raise_for_status() 
      except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
      except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
      except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
      except requests.exceptions.RequestException as err:
            print(f"Oups: Something Else {err}")

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
      else :
            print(f"Impossible de scrapper cette page car son status code est : {request.status_code} ") 

extractData = extractUrlsData()

def getAllPagesScraping(link):
      requete = None  # Initialize requete to None
      try:
            requete = requests.get(link, headers=headers, timeout=10)
            requete.raise_for_status() 
      except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
      except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
      except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
      except requests.exceptions.RequestException as err:
            print(f"Oups: Something Else {err}")

      if requete and requete.status_code == 200:

            textSoup = BeautifulSoup(requete.content, 'html.parser')
            text_content = textSoup.get_text()
            cleaned_text = re.sub(r'\s+', ' ', text_content)

            with open('nexity.txt', "a", encoding="utf-8") as file :
                  file.write(f"Lien de la page: {link}\n\n") 
                  file.write(f"Contenu de la page: {cleaned_text}\n\n")
      elif requete is not None:
            print(f"Impossible de scrapper cette page car son status code est : {requete.status_code} ")
  
def getAllDataPages() :
      pages = extractData
      for page in pages:
            getAllPagesScraping(link=page)
            print(f"On scrappe : {page} ")             

if __name__ == '__main__':
      getAllDataPages()
      print("Le contenu de toutes les pages a été enregistré avec succès")
else:
      print("Impossible de récupérer le contenu de toutes les pages")