import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

try:
    url=input('Please enter example url')
    html=urllib.request.urlopen(url)
except urllib.error.URLError as e:
    print('Please enter right url')
    quit()
html=html.read().decode()
soup=BeautifulSoup(html,"html.parser")
title_tag=soup.find('title')
tags=soup.find_all('a')
for tag in tags:
    link=tag.get('href')

