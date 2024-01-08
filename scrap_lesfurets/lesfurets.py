import requests
from bs4 import BeautifulSoup
import re

verifyGetRequest = requests.get("https://www.lesfurets.com/")
print(verifyGetRequest.status_code)