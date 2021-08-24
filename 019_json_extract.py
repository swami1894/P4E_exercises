import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum = 0

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    sum = 0

    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    comments=dict()
    comments = json.loads(data)
    counts=comments['comments']

    for item in counts:
        count = item['count']
        sum = sum + int(count)
    print('Count: ', len(counts))
    print('Sum: ', sum)
