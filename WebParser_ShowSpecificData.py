# Pythone v3.6

import requests
from bs4 import BeautifulSoup
# Reference: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

#--------------------------------------------------#

def get_web_page(url):
    request = requests.get(url)

    if request.status_code != 200:
        print("Invalid url: ", request.url)
        return None
    else:
        return request.text

#--------------------------------------------------#

url = "http://8comic.se/103903/"
page = get_web_page(url)
webParser = BeautifulSoup(page, "html.parser")

# the title
print("[title] " + webParser.title.string)

# the descriptions (from meta tag)
for meta_data in webParser.find_all("meta"):
    if meta_data.get("name") == "description":
        print("[descriptions] \r\n" + meta_data.get("content"))
        break;

# the url (from meta tag)
print("[url] " + webParser.find(property = "og:url").get("content"))

