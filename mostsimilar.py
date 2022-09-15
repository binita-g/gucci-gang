import codecs
import sys
import requests
import nltk
import gensim
from nltk.corpus import sentiwordnet as swn
from gensim.models import Word2Vec
import numpy as np
import gzip
import logging
import importlib
from operator import itemgetter

# To run, run "python3 mostsimilar.py output.txt.gz output_model.txt"
# Must be gzip file
in_file = sys.argv[1]

out_file = sys.argv[2]

sys.stdout = open(out_file, 'w')

# Read gzip file
def read_input(input_file):
    logging.info("reading file {0}...this may take a while.",
        format(input_file))
    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):
            # Preprocess the text.
            yield gensim.utils.simple_preprocess(line)

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

# Words Associations
# Gucci
w_gucci = [[u'gucci']]
print("gucci: ")
find_most_similar(*w_gucci)

# Rolex
w_rolex = [[u'rolex'], [u'rollie']]
print("rolex: ")
find_most_similar(*w_rolex)

# Louis
w_louis = [[u'louis'], [u'vuitton']]
print("louis: ")
find_most_similar(*w_louis)

# Dior
w_dior = [[u'dior']]
print("dior: ")
find_most_similar(*w_dior)

# Cartier
w_cartier = [[u'cartier']]
print("cartier: ")
find_most_similar(*w_cartier)

# Chanel
w_chanel = [[u'chanel']]
print("chanel: ")
find_most_similar(*w_chanel)

# Louboutin
w_louboutin = [[u'louboutin']]
print("louboutin: ")
find_most_similar(*w_louboutin)

# Prada
w_prada = [[u'prada']]
print("prada: ")
find_most_similar(*w_prada)

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

w1 = 'beyonce'
w2 = 'adidas'
sim = model.wv.similarity(w1, w2)
print(f"Similarity between {w1} and {w2}:")
print(sim)

w1 = 'beyonce'
w2 = 'balenciaga'
sim = model.wv.similarity(w1, w2)
print(f"Similarity between {w1} and {w2}:")
print(sim)