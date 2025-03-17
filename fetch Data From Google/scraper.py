import requests
from bs4 import BeautifulSoup
import urllib.parse

class GoogleScraper:
    def __init__(self, num_results=10, num_pages=3):
        self.num_results = num_results
        self.num_pages = num_pages
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

    def google_search(self, query):
        results = []
        for page in range(self.num_pages):
            start = page * self.num_results
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&num={self.num_results}&start={start}"
            headers = {"User-Agent": self.user_agent}
            
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"Error: Received status code {response.status_code}")
                continue
            
            soup = BeautifulSoup(response.text, 'html.parser')
            for g in soup.find_all('div', class_='g'):
                title = g.find('h3')
                link = g.find('a', href=True)
                if title and link:
                    results.append({
                        'title': title.text,
                        'link': link['href']
                    })
        
        return results 