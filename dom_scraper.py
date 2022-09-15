import requests
import re
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup

# Names of divs we should discard
bad_divs = {"Songwriter(s):", "Producer(s):", "Imprint/Promotion Label:", "Follow Us", "The Daily", "Have a Tip?", "Gains in Weekly Performance", "Additional Awards"}

# Regular expression for class selectors for chart items
regex = re.compile('.*o-chart-results-list__item.*')

with open("dates.txt","r") as f:
    for date in f:
        url = "https://www.billboard.com/charts/hot-100/" + date.strip()
        page = requests.get(url, timeout=10)

        soup = BeautifulSoup(page.content, "html.parser")

        # Get each chart item with title and artist
        results = soup.find_all("li", {"class" : regex})

        textStringArray = []

        for result in results:
            # Get titles
            title_string = ""
            title_children = result.findChildren("h3", recursive=False)
            for title_child in title_children:
                title_string = title_child.text.strip()

            # Get artists
            artist_string = ""
            artist_children = result.findChildren("span", recursive=False)
            for artist_child in artist_children:
                artist_string = artist_child.text.strip()
            
            # Combine into text string
            title_string_array = title_string.split()
            artist_string_array = artist_string.split()

            total_string = ""
            for artist_word in artist_string_array:
                if artist_word == "&":
                    artist_word = "and"
                if artist_word == "Featuring":
                    break
                total_string += artist_word + "-"
            for title_word in title_string_array:
                total_string += title_word + "-"
            total_string += "lyrics"

            if (len(total_string) > 10) and (total_string != "RE--ENTRY-lyrics"):
                print("https://genius.com/" + total_string)

