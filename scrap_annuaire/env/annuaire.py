import requests
from bs4 import BeautifulSoup

verifyGetRequest = requests.get("https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=1")
print(verifyGetRequest.status_code)

def getAllPagesScraping():
      
      urls = []
      
      pageNumber = 1
      
      for i in range (107) : 
            i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={pageNumber} "
            pageNumber += 1
            urls.append(i)      

            return urls
      
getAllPagesScraping()