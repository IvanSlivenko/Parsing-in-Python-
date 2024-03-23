import requests
from bs4 import BeautifulSoup
import csv

from const import HOST, URL, HEADERS, PAGINATION

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html): # Збираємо контент на одній сторінці
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='sc-182gfyr-0 jmBHNg')
    cards = []
    for item in items:
        cards.append(
            {
                'title': item.find('a', class_='cpshbz-0 eRamNS').get_text(strip=True),
                'link_produkt': item.find('div', class_='be80pr-15 kwXsZB').find('a').get('href'),
                # 'link_produkt': HOST+item.find('div', class_='be80pr-15 kwXsZB').find('a').get('href'),
                'brand': item.find('span', class_='be80pr-21 dksWIi').get_text(strip=True),
                'card_img': item.find('div', class_='be80pr-9 fJFiLL').find('img').get('srcset')
            }
        )

    return cards

# html = get_html(URL)
# print(get_content(html.text))

def parser():
    pagination = int(PAGINATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for currеnt_page in range(1, pagination+1):
            print(f"Парсимо сторінку : {currеnt_page}")
            html = get_html(URL, params={'page': currеnt_page})
            cards.extend(get_content(html.text))
        print('Парсинг сторінок завершено')
    else:
        print('Error')

parser()