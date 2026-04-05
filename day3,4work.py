from bs4 import BeautifulSoup
import urllib.error
import urllib.request
import urllib.parse

url="https://books.toscrape.com/"

def get_html(url):
    try:
        with url.urllib.request.urlopen(url):
            html=url.decode()
    except urllib.error.URLError as e:
        print('URL错误',e)
    except Exception as e:
        print('未知错误',e)
        return html



def get_soup(html):
    html=get_html(url)
    soup=html.BeautifulSoup(html,html.parser)
    return soup

def get_book_tag(book_tag):
    html=get_html(url)
    soup=get_soup(html)
    tags={}
    book_tag=soup.findall('<div class="tags">')
    for tag in book_tag:
        tags[tag]=tag.get('tag',0)+1
