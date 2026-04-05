import urllib.error
import urllib.request
import urllib.parse
counts=dict()
frand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in frand:
    words=line.decode().strip().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)