import requests
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup

tokenizer = RegexpTokenizer(r'\w+')
wordnet_lemmatizer= WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Words of interest
brands_dict = {'gucci': 0, 'louis': 0, 'rolex': 0, 'ysl': 0}

# Iterate through list of URLs
with open("songs_list_generated.txt","r") as f:
    # Set up frequency distribution.
    fdist = FreqDist()
    
    for line in f:
        # Scrape lyrics from the lyrics container on Genius page
        try:
            page = requests.get(line.strip(), timeout=10)

            soup = BeautifulSoup(page.content, "html.parser")

            # Scrape only from the divs that contain lyrics.
            results = soup.find_all(attrs={"data-lyrics-container": "true"})

            for result in results:
                # Create an empty string to print out all the word tokens to.
                textString = ""

                # Replace <br> tags with a space to avoid word concatenation bug.
                result = result.get_text(separator=" ").strip()
                word_tokens = tokenizer.tokenize(result)

                # Lemmatize word tokens.
                for w in word_tokens:
                    if w not in stop_words:
                        lemmatized = wordnet_lemmatizer.lemmatize(w).strip('[]').lower()
                        fdist[lemmatized.strip('[]').lower()]+= 1

                        # Update dictionary of brands with frequencies of words
                        if lemmatized in brands_dict:
                            brands_dict[lemmatized] += 1
                        textString += str(lemmatized).strip('[]')
                        textString += " "
                
                print(textString)
        except:
            print('Could not get song', line.strip())

    # Print the brands and the number of times they appear
    print(brands_dict)

    # Print the frequency distribution
    print(repr(fdist))

    # Print all the text
    # print(textString)
