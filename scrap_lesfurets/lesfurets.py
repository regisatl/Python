import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def is_valid_url(url, base_url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ("http", "https"):
            return False
        if not parsed_url.netloc:
            return False
        if not parsed_url.path.startswith("/"):
            return False
        return True
    except Exception as e:
        print(f"Error checking validity of URL {url}: {e}")
        return False


def scrape_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            content = ""
            for tag_name in ["h1", "p", "span", "div", "article", "section"]:
                elements = soup.find_all(tag_name)
                for element in elements:
                    content += element.get_text(strip=True) + "\n"
            return content
        else:
            print(f"Failed to fetch URL {url}. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error scraping URL {url}: {e}")
        return None


def main(start_url):
    try:
        base_url = urlparse(start_url).scheme + "://" + urlparse(start_url).netloc

        # Scraping links
        response = requests.get(start_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = [link.get("href") for link in soup.find_all("a", href=True)]

            # Filtering and validating URLs
            valid_urls = [
                urljoin(base_url, link)
                for link in links
                if is_valid_url(urljoin(base_url, link), base_url)
            ]

            # Scraping content for each valid URL
            for url in valid_urls:
                content = scrape_url(url)
                if content:
                    with open("output.txt", "w", encoding="utf-8") as file:
                        file.write(content + "\n\n")

    except Exception as e:
        print(f"Error in main function: {e}")


if __name__ == "__main__":
    main("https://www.journaldugeek.com/")
