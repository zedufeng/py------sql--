import urllib.error
import urllib.parse
import urllib.request
import re
from bs4 import BeautifulSoup

try:
    url=input('Please enter your URL')
    html=urllib.request.urlopen(url).read().decode()
except urllib.error.URLError:
    print('url is error,Please enter right url')
    quit()

soup=BeautifulSoup(html,'html.parser')
title_tag=soup.find('title')
tags=soup.find_all('a')
a=len(tags)
relative_url=0
full_url=0
valid_url=0
other_url =0
for tag in tags:
    href=tag.get('href')
    if href is None:
        continue
    valid_url=valid_url+1
    if href.startswith('http'):
        full_url=full_url+1
    elif href.startswith('/'):
        relative_url=relative_url+1
    else:
        other_url = other_url + 1
    
all_url=other_url+relative_url
print('Title',title_tag.text)
print('Total <a> tags',a)
print('valid href links',valid_url)
print('Full links',full_url)
print('Relative links',all_url)
print('Result saved to report.txt')


with open('report.txt', 'w', encoding='utf-8') as f:
    f.write('Title: ' + title_tag + '\n')
    f.write('Total <a> tags: ' + str(a) + '\n')
    f.write('valid href links: ' + str(valid_url) + '\n')
    f.write('Full links: ' + str(full_url) + '\n')
    f.write('Relative links: ' + str(relative_url) + '\n')
    f.write('Other links: ' + str(other_url) + '\n')