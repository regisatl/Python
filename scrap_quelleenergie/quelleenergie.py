import requests
from bs4 import BeautifulSoup
import re

def extractData():
      
      request = requests.get("https://www.quelleenergie.fr/")
      soup = BeautifulSoup(request.content, "html.parser")
      
      test = soup.find_all("a")
      
      for i in test:
            print("https://www.quelleenergie.fr" + i["href"])
      
      

extractData()