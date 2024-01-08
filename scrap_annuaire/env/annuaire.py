from bs4 import BeautifulSoup
import requests
import re

verifyGetRequest = requests.get("https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=1")
print(verifyGetRequest.status_code)

def getAllPagesScraping() :
      
      urls = []
      pageNumber = 1
      
      for i in range (107) : 
            i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={pageNumber} "
            pageNumber += 1
            urls.append(i)      
            return urls
      
getAllPagesScraping()

def parseAttorney(url) :
      request = requests.get("https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=1")
      soup = BeautifulSoup(request.content, "html.parser")

      attorneys = soup.find_all("div", class_ ="callout secondary annuaire-single")
      
      for attorney in attorneys :
            nameAttorney = attorney.find('h3').text.strip()
            adressAttorney = attorney.find('span', class_ = 'adresse').text.strip()
            adressFinalAttorney = re.sub(r"\s*", " ", adressAttorney)
            telAttorney = attorney.find('span', class_ = 'telephone').text.strip()
            emailAttorney = attorney.find('span', class_ = 'email').a.text.strip()
            
            wayStockData = r"C:\Users\Régis.Attolou\Documents\Github\Python\scrap_annuaire\annuaire_attorney.txt"
            with open(wayStockData, "a") as f :
                  f.write(f" {nameAttorney}\n")
                  f.write(f" {adressFinalAttorney}\n")
                  f.write(f" {telAttorney}\n")
                  f.write(f" {emailAttorney}\n\n")
            

def parseAllAttorneys() :
      pages = getAllPagesScraping()
      for page in pages :
            parseAttorney(url = page)
            print(f"On scrape {page} ")
            
parseAllAttorneys()