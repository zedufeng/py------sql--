import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
frand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in frand:
    print(line.decode().strip())