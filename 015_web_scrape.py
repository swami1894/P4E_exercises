from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count: "))
pos = int(input("Enter position: "))
start = True
urlcnt = 0

while count >= 0:
    if start:
        start = False
        if len(url) < 1:
            url =  'http://py4e-data.dr-chuck.net/known_by_Chrystal.html'
    else:
        url = newurl
    print('Retrieving: ',url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    for tag in tags:
        urlcnt = urlcnt + 1
        if urlcnt == pos:
            newurl = str(tag.get('href', None))
            count = count - 1
            urlcnt = 0
            break
