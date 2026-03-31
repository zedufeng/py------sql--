import re
line = 'X-DSPAM-Confidence: 0.8475'
e=re.search('^X',line)
print(e)
line2='X-DSPAM-Confidence: 0.8475'
d=re.search('^X-\S:',line2)
print(d)

lines = [
    'X-DSPAM-Confidence: 0.8475',
    'X-DSPAM-Result: Innocent',
    'From: cwen@iupui.edu',
    'X-Plane is behind schedule: two weeks']
for line in lines:
    if re.findall('^X-\S+:',line):
        print(line)

line3 = 'My email is tom123@gmail.com'
c=re.findall('\S+@\S+',line3)
print(c)


