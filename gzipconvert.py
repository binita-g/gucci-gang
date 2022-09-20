import gzip
import sys
import requests
import gzip
import os

directory = 'scraped_output'

# file_in = sys.argv[1]

# The argument here should be the output from scraper.py, i.e. python3 gzipconvert.py output.txt
for file_in in os.listdir(directory):
    f_name = os.path.join(directory, file_in)
    if (".gz" not in f_name):
        f_in = open(f_name, 'rb')
        file_out = f_name + ".gz"
        f_out = gzip.open(file_out, 'wb')
        f_out.writelines(f_in)
        f_out.close()