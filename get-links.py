import requests
from bs4 import BeautifulSoup

badurls = [19,22,35,39,72,88,156,162,165,234,245,312,371,385,407,429,432,441,476,484,570,594,629]

for i in badurls:
	url = 'https://www.wired.com/tag/beyond-the-beyond/?page='+str(i)
	grab = requests.get(url)
	soup = BeautifulSoup(grab.text, 'html.parser')

	# opening a file in write mode
	f = open("badurls/page"+str(i)+".txt", "w")
	# traverse paragraphs from soup
	for link in soup.find_all('a', class_="summary-item__hed-link"):
		data = "https://www.wired.com"+link.get('href')
		f.write(data)
		f.write("\n")

	f.close()
