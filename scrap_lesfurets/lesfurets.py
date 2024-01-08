import requests
from bs4 import BeautifulSoup
import re

verifyGetRequest = requests.get("https://www.quelleenergie.fr/")
print(verifyGetRequest.status_code)

def parseAttorney(url):
      
      request = requests.get(url)
      soup = BeautifulSoup(request.content, "html.parser")

      attorneys = soup.find_all("div", class_ ="callout secondary annuaire-single")
      
      for attorney in attorneys:
            try:
                  nameAttorney = attorney.find('h3').text.strip()
            except AttributeError:
                  nameAttorney = "N/A"
            try:
                  adressAttorney = attorney.find('span', class_ = 'adresse').text.strip()
                  adressFinalAttorney = re.sub(r"\s*", " ", adressAttorney)
            except AttributeError:
                  adressFinalAttorney = "N/A"
            try:
                  telAttorney = attorney.find('span', class_ = 'telephone').text.strip()
                  telFinalAttorney = re.sub(r"\s*", " ", telAttorney)
            except AttributeError:
                  telFinalAttorney = "N/A"
            try:
                  emailAttorney = attorney.find('span', class_ = 'email').a.text.strip()
            except AttributeError:
                  emailAttorney = "N/A"

      
            wayStockData = r"C:\Users\Régis.Attolou\Documents\Github\Python\scrap_annuaire\quelleenergie.txt"
            with open(wayStockData, "a") as f :
                  f.write(f"{nameAttorney}\n")
                  f.write(f"{adressFinalAttorney}\n")
                  f.write(f"{telAttorney}\n")
                  f.write(f"{emailAttorney}\n\n")