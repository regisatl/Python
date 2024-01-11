import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_links(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    with open(output_file, 'w', encoding='utf-8') as file:
        for link in links:
            href = link.get('href')
            if href:
                # Nettoyage des liens
                href = href.strip()
                if href.startswith('http://') or href.startswith('https://'):
                    pass
                elif href.startswith('www'):
                    href = 'https://' + href
                elif href.startswith('/') and href.count('/') == 1:
                    href = urllib.parse.urljoin(url, href)
                    href = href.replace(url + '/', '')

                # Ecriture dans le fichier
                file.write(f'{href} {link.text}\n')

if __name__ == '__main__':
    url = 'https://www.01net.com/'
    output_file = '01net.txt'
    scrape_links(url, output_file)