import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import re
import urllib
import os

nsf_url = 'https://www.nsf.gov/awardsearch/download.jsp'
nsf_response = requests.get(nsf_url)
nsf_page = nsf_response.text

soup = BeautifulSoup(nsf_page,"lxml")

listofdownloads = []
for element in soup.find(class_='downloadcontent'):
    listofdownloads.append(element)
  
downloadfilelinks = []
for l in listofdownloads:
    link = str(str(l).split('"')[3]).split('&')[0] 
    downloadfilelinks.append('https://www.nsf.gov/awardsearch/{}&All=true'.format(link))

for d in downloadfilelinks:
    f = urllib.request.urlopen(url)
    with open("code2.zip", "wb") as code:
        code.write(f.read())
