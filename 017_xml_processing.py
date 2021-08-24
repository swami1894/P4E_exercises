import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
number = 0
address = input('Enter location: ')

if len(address) < 1:
    address = 'https://py4e-data.dr-chuck.net/comments_291186.xml'

url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')
for comment in comments:
    count = comment.find('count').text
    sum = sum + int(count)

print('Count: ', len(comments))
print('Sum: ', sum)
