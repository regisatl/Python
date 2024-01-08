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
      
      request = requests.get(url)
      soup = BeautifulSoup(request.content, "html.parser")

      attorneys = soup.find_all("div", class_ ="callout secondary annuaire-single")
      
      for attorney in attorneys :
            try :
                  nameAttorney = attorney.find('h3').text.strip()
            except : 
                  pass
            adressAttorney = attorney.find('span', class_ = 'adresse').text.strip()
            try :    
                  adressFinalAttorney = re.sub(r"\s*", " ", adressAttorney)
            except :
                  pass
            telAttorney = attorney.find('span', class_ = 'telephone').text.strip()
            try:
                telFinalAttorney = re.sub(r"\s*", " ", telAttorney)
            except :
                pass 
            try:
                  emailAttorney = attorney.find('span', class_ = 'email').a.text.strip()
            except:
                    pass
      
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