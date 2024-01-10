import requests
from bs4 import BeautifulSoup
import re

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    return links

def extract_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {}
    data['title'] = soup.title.string
    data['body'] = ' '.join([p.text for p in soup.find_all('p')])
    return data

def scrape_site(url):
    links = extract_links(url)
    with open('data.txt', 'w') as f:
        for link in links:
            if link.startswith('http'):
                data = extract_data(link)
                f.write(f"URL: {link}\n")
                f.write(f"Title: {data['title']}\n")
                f.write(f"Body: {data['body']}\n")
                f.write("\n")

scrape_site('https://www.example.com')