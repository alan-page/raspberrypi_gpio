# requests and Beautiful Soup
#
# Installation
# pip3 install requests
# pip3 install beautifulsoup4
#


import requests
from bs4 import BeautifulSoup

URL = 'http://www.flaminglogos.net/theotherside/'
page = requests.get(URL)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
