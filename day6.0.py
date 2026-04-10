import urllib.error 
import urllib.parse
import urllib.request
import json
serviceurl='http://py4e-data.dr-chuck.net/json?'
while True:
    address=input('enter your location')
    if len(address)<1:
        break

url=serviceurl+urllib.parse.urlencode({'address':address})

print('Reparse',url)
uh=urllib.request.urlopen(url)
data=uh.read().decode()
print('Reparse',len(data))

try:
    js=json.load(data)
except:
    js=None

lat=js['results'][0]['gemo']['loca']['lat']
location=js['result'[0]]['form']