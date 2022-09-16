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
brands_dict = {'gucci': 0, 
                'rolex': 0, 
                'rollie': 0, 
                'louis': 0, 
                'dior': 0, 
                'cartier': 0, 
                'chanel': 0, 
                'louboutin': 0, 
                'prada': 0, 
                'fendi': 0, 
                'balenciaga': 0, 
                'tiffany': 0, 
                'versace': 0, 
                'hermes': 0, 
                'ysl': 0}

# Take input .txt file from first argument (i.e. python3 scraper.py songs_list_2015_summer.txt)
in_file = sys.argv[1]

# Iterate through list of URLs
with open(in_file, 'r') as f:
    # Set output file to output folder with input file name + scraped (i.e. "scraped_output/scraped_songs_list_2015_summer.txt")
    out_file = "scraped_output/scraped_" + (sys.argv[1]).split("songs_lists/",1)[1]
    print(out_file)

    sys.stdout = open(out_file, 'w+')

    # Set up frequency distribution.
    fdist = FreqDist()
    
    # Keep track of all the text in one string (do not print).
    totalTextString = ""
    
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
                
                        # Update total text string
                        totalTextString += textString
                
                # Print lyrics
                print(textString)
        # If the automatic lyric generator did not work, output which song it did not work for.
        except:
            print('Could not get song', line.strip())

    # Print all frequency analyses in freqdist folder.
    out_file = "freqdist_results/freqdist_" + (sys.argv[1]).split("songs_lists/",1)[1]
    sys.stdout = open(out_file, 'w')
    
    print(brands_dict)
    print(repr(fdist))
