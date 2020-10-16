import requests
from bs4 import BeautifulSoup

def get_page_link(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.bbc.co.uk/search?q=covid&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('a', {'class': 'css-vh7bxp-PromoLink e1f5wbog3'}):
            page_href = link.get('href')
            # print(page_href)
            get_item_name(page_href)
        page += 1


def get_item_name(item_href):
    source_code = requests.get(item_href)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for item_name in soup.findAll('h1', {'class': 'no-margin'}):
        title = item_name.string
        print(title)


get_page_link(3)
