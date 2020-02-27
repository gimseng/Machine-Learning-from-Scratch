#import sys,re
# regex=sys.argv[1]

# for line in sys.stdin:
#     if re.search (regex,line):
#         sys.stdout.write(line)
#count=0
#for line in sys.stdin:
#    count+=1
#   print (line, count)

#print (count)

from bs4 import BeautifulSoup

import requests

html=requests.get('http://www.example.com').text
soup=BeautifulSoup(html,'html5lib')
first_paragraph=soup.find('p')
first_paragraph_text=soup.p.text
first_paragraph_words=soup.p.text.split()

print (first_paragraph,"--")
print (first_paragraph_words,'**')