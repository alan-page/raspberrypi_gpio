# requests and Beautiful Soup
#
# Installation
# pip3 install requests
# pip3 install beautifulsoup4
#


print "import requests"
import requests

print "import bs4"
from bs4 import BeautifulSoup

URL = 'http://www.flaminglogos.net/theotherside/'


page = requests.get(URL)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
