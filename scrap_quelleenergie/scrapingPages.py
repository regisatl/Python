import requests
from bs4 import BeautifulSoup
import re

verifyStatutsCode = requests.get("https://www.latribune.fr/")
print(verifyStatutsCode.status_code)