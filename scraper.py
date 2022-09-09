import requests
from bs4 import BeautifulSoup

# Scrape lyrics from the lyrics container on Genius page
URL = "https://genius.com/Lil-pump-gucci-gang-lyrics"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("div", "data-lyrics-container"=="true")

print(results.text)
