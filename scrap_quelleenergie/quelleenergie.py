import requests
from bs4 import BeautifulSoup
import re

urls = []

def extractUrlsData():
      request = requests.get("https://app.assurup.com/")
      soup = BeautifulSoup(request.content, "html.parser")
      
      dataText = soup.find_all("a", href=True)
      
      for tempLink in dataText:
            baseUrl = "https://app.assurup.com"
            url = tempLink['href']
            if url.startswith("https://") or url.startswith("http://"):
                  if not url in urls:
                        urls.append(url)
            elif url.startswith(r"/[w]+"):
                  urLink = f"{baseUrl}{url}"
                  if not url in urls:
                        urls.append(urLink)
            elif url.startswith("#"):
                  pass
      return urls  

extractData = extractUrlsData()

def getAllPagesScraping(link):
      requete = requests.get(link)
      soup = BeautifulSoup(requete.content, "html.parser")
      text = soup.get_text()
      finalText = re.sub(r"\s+", " ", text)

      with open('assurup.txt', "a", encoding="utf-8") as f :
            f.write(f"{link}\n") 
            f.write(f"{finalText}\n\n")


def getAllDataPages() :
      pages = extractData
      for page in pages:
            getAllPagesScraping(link=page)
            print(f"On scrappe : {page} ")             
getAllDataPages()

