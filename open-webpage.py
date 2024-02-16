# save-webpage.py

import urllib.request, urllib.error, urllib.parse

url = 'https://www.wired.com/beyond-the-beyond/2020/07/reading-mail-dead-scientists/'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

f = open('beyond1.html', 'w')
f.write(webContent)
f.close
