import urllib.request
import time

merge = open("merge.txt", "r")
page1 = open("paginated-urls/page1test.txt")
lines = page1.read().split("\n")

def download_html_with_retries(url, filename, max_retries=3, retry_delay=2):
    retries = 0
    while retries < max_retries:
        try:
            with urllib.request.urlopen(url) as response:
                return urllib.request.urlretrieve(url, filename)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")
            retries += 1
            time.sleep(retry_delay)
    print(f"Could not download {url} after {max_retries} retries.")
    return None

for index, page in enumerate(lines):
    formatted_index = str(index).zfill(4)
    uri = page.rsplit('/', 1)[-1]
    filename = "out/"+formatted_index+"_"+uri+".html"
    returned_page = download_html_with_retries(page, filename)
    if returned_page:
        print(f"downloaded {page}")
    else:
        print(f"failed to download {page}")

    # urllib.request.urlretrieve(page, "out/"+formatted_index+"_"+name+".html")
