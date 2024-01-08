import requests
from bs4 import BeautifulSoup

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

def parseAttorney() :
      request = requests.get("https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=1")
      soup = BeautifulSoup(request.content, "html.parser")

      attorneys = soup.find_all("div", class_ ="callout secondary annuaire-single")
      
      for attorney in attorneys :
            name = attorney.find('h3').text.strip()
            adressAttorney = attorney.find('span', class_ = 'adresse').text.strip()
            print(adressAttorney)
      
parseAttorney()