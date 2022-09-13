import requests
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup

tokenizer = RegexpTokenizer(r'\w+')
wordnet_lemmatizer= WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Iterate through list of URLs
with open("songs_list.txt","r") as f:
    for line in f:
        # Scrape lyrics from the lyrics container on Genius page
        page = requests.get(line.strip(), timeout=10)

        soup = BeautifulSoup(page.content, "html.parser")

        # Scrape only from the divs that contain lyrics.
        results = soup.find_all(attrs={"data-lyrics-container": "true"})

        textString = ""

        for result in results:
            # Replace <br> tags with a space to avoid word concatenation bug.
            result = result.get_text(separator=" ").strip()
            word_tokens = tokenizer.tokenize(result)

            # Lemmatize word tokens.
            for w in word_tokens:
                if w not in stop_words:
                    lemmatized = wordnet_lemmatizer.lemmatize(w)
                    textString += str(lemmatized).strip('[]')
                    textString += " "
        
        print(textString)
