import codecs
import sys
import requests
import nltk
import gensim
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import gutenberg
from nltk import FreqDist
from gensim.models import Word2Vec
import numpy as np
import gzip
import logging
import importlib
from operator import itemgetter


# To run, run "python3 most_similar.py output.txt.gz"
# Must be gzip file
in_file = sys.argv[1]

# Set output file to output folder
file_name = ((sys.argv[1]).split("scraped_output/",1)[1]).split(".gz",1)[0]
file_name_with_folder = "scraped_output/" + file_name
out_file = "vector_results/" + file_name + "_results"
print(out_file)
sys.stdout = open(out_file, 'w')

# Read gzip file
def read_input(input_file):
    logging.info("reading file {0}...this may take a while.",
        format(input_file))
    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):
            # Preprocess the text.
            yield gensim.utils.simple_preprocess(line)

# Frequency analysis
def get_freq():
    brands_dict = ['gucci', 
                    'rolex', 
                    'rollie',
                    'louis',
                    'goyard',
                    'saint laurent',
                    'dolce',
                    'celine',
                    'canada goose',
                    'moncler',
                    'bottega',
                    'burberry',
                    'loewe', 
                    'dior', 
                    'cartier', 
                    'chanel', 
                    'louboutin', 
                    'prada', 
                    'fendi', 
                    'balenciaga', 
                    'tiffany', 
                    'versace', 
                    'hermes', 
                    'ysl']
        
    articles_dict = ['t-shirt',
                    'shirt',
                    'jeans',
                    'sweater',
                    'daisy dukes',
                    'bikini',
                    'black dress',
                    'red dress',
                    'dress',
                    'shades',
                    'sunglasses',
                    'sneakers',
                    'sneaks',
                    'boots',
                    'bag',
                    'bags',
                    'hat',
                    'cap',
                    'jacket',
                    'cardigan',
                    'suit',
                    'tie',
                    'pajamas',
                    'trousers',
                    'coat',
                    'overalls',
                    'skirt'
    ]

    textiles_dict = ['denim',
                    'silk',
                    'wool',
                    'cotton',
                    'velvet',
                    'chiffon',
                    'satin',
                    'velour',
                    'moleskin',
                    'flannel',
                    'corduroy',
                    'fleece',
                    'lace'
    ]

    print("Frequency Analysis")

    with open (file_name_with_folder, "r") as text_file:
        data = text_file.read().replace('\n', ' ')
    
    data = data.split(' ')
    freqDist = FreqDist(data)

    # Freq count for brands
    print(" \nBrands")
    for brand in brands_dict:
        print_stmt = brand + ":" + str(freqDist[brand])
        print(print_stmt)
    
    # Freq count for articles of clothing
    print("\nArticles")
    for article in articles_dict:
        print_stmt = article + ":" + str(freqDist[article])
        print(print_stmt)
    
    # Freq count for textiles
    print("\nTextiles")
    for textile in textiles_dict:
        print_stmt = textile + ":" + str(freqDist[textile])
        print(print_stmt)
    
    print('\n')

# Find most similar words to another word.
def find_most_similar(*w_group):
    for w in w_group:
        ms_set = model.wv.most_similar(w, topn=100)
        for ms_word in ms_set:
            print(ms_word)
            print('\n')

# Train model.
documents = list(read_input(in_file))
model = gensim.models.Word2Vec(
    documents,
    vector_size=100,
    window=5,
    min_count=1,
    workers=1
)

model.train(documents, total_examples=len(documents), epochs=10)
model.save('brand-vectors.w2v')

# Frequency analysis
get_freq()

# Words Associations
# Gucci
w_gucci = [[u'gucci']]
print("gucci: ")
find_most_similar(*w_gucci)

# Rolex
# w_rolex = [[u'rolex'], [u'rollie']]
# print("rolex: ")
# find_most_similar(*w_rolex)

# Louis
# w_louis = [[u'louis'], [u'vuitton']]
# print("louis: ")
# find_most_similar(*w_louis)

# Dior
# w_dior = [[u'dior']]
# print("dior: ")
# find_most_similar(*w_dior)

# Cartier
w_cartier = [[u'cartier']]
print("cartier: ")
find_most_similar(*w_cartier)

# Chanel
# w_chanel = [[u'chanel']]
# print("chanel: ")
# find_most_similar(*w_chanel)

# Louboutin
# w_louboutin = [[u'louboutin']]
# print("louboutin: ")
# find_most_similar(*w_louboutin)

# Prada
# w_prada = [[u'prada']]
# print("prada: ")
# find_most_similar(*w_prada)

# Fendi
w_fendi = [[u'fendi']]
print("fendi: ")
find_most_similar(*w_fendi)

# Find similarity between TWO words
w1 = 'gucci'
w2 = 'louis'
sim = model.wv.similarity(w1, w2)
print(f"Similarity between {w1} and {w2}:")
print(sim)

# Find relationship between Drake and his brand sponsorships
# w1 = 'drake'
# w2 = 'nike'
# sim = model.wv.similarity(w1, w2)
# print(f"Similarity between {w1} and {w2}:")
# print(sim)

# w2 = 'ovo'
# sim = model.wv.similarity(w1, w2)
# print(f"Similarity between {w1} and {w2}:")
# print(sim)

# w2 = 'louis'
# sim = model.wv.similarity(w1, w2)
# print(f"Similarity between {w1} and {w2}:")
# print(sim)

# w1 = 'migos'
# w2 = 'louis'
# sim = model.wv.similarity(w1, w2)
# print(f"Similarity between {w1} and {w2}:")
# print(sim)

# w2 = 'prada'
# sim = model.wv.similarity(w1, w2)
# print(f"Similarity between {w1} and {w2}:")
# print(sim)

# w2 = 'valentino'
# sim = model.wv.similarity(w1, w2)
# print(f"Similarity between {w1} and {w2}:")
# print(sim)
