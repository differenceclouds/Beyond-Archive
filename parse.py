from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import os
from urllib.parse import urlparse
from os.path import basename

# file = "/Users/Radagast/python/beyond/parsing_tests/Xeni digitally snapping away WIRED.html"
page_URL = "https://www.wired.com/2004/03/xeni-digitally-/"
page = requests.get(page_URL)

page_data = page.content

path = "./out"
uri = urlparse(page_URL).path
os.makedirs(path + uri)
output_directory = path + uri

def get_metadata(doc) -> str:
# with open(file) as doc:

    meta_strainer = SoupStrainer(['time', 'h1'])
    meta_soup = BeautifulSoup(doc, "html.parser", parse_only=meta_strainer)


    time = meta_soup.time
    del time['class']
    del time['data-testid']

    h1 = meta_soup.h1
    del h1['class']
    del h1['data-testid']

    # print(meta_soup.prettify())
    return meta_soup.prettify()

def get_content(doc, output_directory) -> str:
# with open(file) as doc:

    #these are the only tags needed
    strainer = SoupStrainer(class_="body__inner-container")
    content_soup = BeautifulSoup(doc, "html.parser", parse_only=strainer)


    #remove extraneous junk
    paywalls = content_soup.find_all(class_="paywall")
    for p in paywalls:
        del p['class']

    advertisements = content_soup.find_all(class_="ad")
    for ad in advertisements:
        ad.decompose()

    consumermarketing = content_soup.find_all(class_="consumer-marketing-unit")
    for ad in consumermarketing:
        ad.decompose()

    vma = content_soup.find_all(class_="viewport-monitor-anchor")
    for ad in vma:
        ad.decompose()


    #download images
    images = content_soup.find_all('img')

    url = "https://www.wired.com"

    for image in images:
        src = image.get('src')
        with open(output_directory + basename(src), "wb") as f:
            f.write(requests.get(url+src).content)
        #change src attribure
        image['src'] = basename(src)


    # print(content_soup.prettify())
    return content_soup.prettify()


metadata = get_metadata(page_data)
original_url = "\nRetrieved From: <a href=\'" + page_URL + "\' class=\'wired-link\'>" + page_URL + "</a>\n<br/>\n\n"
content = get_content(page_data, output_directory)
generated_html = original_url + metadata + content



with open(output_directory + "index.html", "w", encoding = 'utf-8') as file: 
    # prettify the soup object and convert it into a string 
    file.write(generated_html) 