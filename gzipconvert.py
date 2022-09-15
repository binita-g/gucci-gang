import gzip
import sys
import requests
import gzip

file_in = sys.argv[1]
file_out = file_in + ".gz"

# The argument here should be the output from scraper.py, i.e. python3 gzipconvert.py output.txt
f_in = open(file_in, 'rb')
f_out = gzip.open(file_out, 'wb')
f_out.writelines(f_in)
f_out.close()