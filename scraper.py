import requests
from bs4 import BeautifulSoup

# Iterate through list of URLs
with open("songs_list.txt","r") as f:
    for line in f:
        # Scrape lyrics from the lyrics container on Genius page
        page = requests.get(line.strip(), timeout=10)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find_all(attrs={"data-lyrics-container": "true"})
        for result in results:
            print(result.text)
