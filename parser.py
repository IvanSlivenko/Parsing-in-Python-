import requests
from bs4 import BeautifulSoup
import csv

from const import HOST, URL, HEADERS


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='sc-182gfyr-0 jmBHNg')
    cards = []
    count = 0
    for item in items:
        count += 1
        cards.append(
            {

                'title': item.find('div', class_='be80pr-15 kwXsZB').get_text(),
                'link_produkt': item.find('div', class_='be80pr-15 kwXsZB').find('a').get('href'),


                # 'bank_produkt': item.find('span', class_='be80pr-21 dksWIi').get_text(),
                # 'produkt_name': item.find('a', class_='cpshbz-0 eRamNS').get_text(),

            }
        )
        print(cards)
    # print(cards)
    return cards

      # testing

        # curent_item_name = item.find('a', class_='cpshbz-0 eRamNS').get_text()
        # curent_item_bank = item.find('span',class_='be80pr-21 dksWIi').get_text()
        # print(f"{count}. Банк {curent_item_bank} - {curent_item_name}")
    # print(cards)
    # print(len(cards))



html = get_html(URL)
get_content(html.text)

