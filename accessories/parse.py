import time

import requests
from bs4 import BeautifulSoup as bs
from pymongo.errors import DuplicateKeyError

from storage.mongoDB import MongoDB

db = MongoDB()
mydb = db.db_name

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }
url_cases = 'https://www.ctrs.com.ua/chexly-i-sumki-dlya-noutbukov/'
url_headphones = 'https://www.ctrs.com.ua/naushniki/'
url_hdd = 'https://www.ctrs.com.ua/vneshnie-zhestkie-diski/tip-nakopitelya_hdd/'


def parse_cases(acc_url, header, db, collection) -> None:
    page_number = 1
    prev_page = None
    curr_collection = db[collection]
    while True:
        curr_url = f'{acc_url}/page_{page_number}/'
        page = requests.get(curr_url, headers=header)
        page_number += 1

        if page.url == prev_page:
            break

        soup = bs(page.content, 'html.parser')
        card_class = 'CatalogProductCard-module__productCardCategory___7jPa-'
        catalog = soup.find('div', class_='catalog-facet')
        product_cards = catalog.find_all('div', class_=card_class)

        for card in product_cards:
            item_dict = dict()

            item_url = card.find('a')
            item_dict['model'] = item_url.get('title')
            link = item_url.get('href')
            image = card.find('img',
                              class_='LinkImage-module__image___2h3-Q')
            full_link = f'{acc_url}{link}'
            try:
                card_price = card.find('div',
                                       class_='Price-module__price___1fKLA')
                item_dict['price'] = f"{card_price.get('data-price')}₴"
            except AttributeError as error:
                continue

            item_dict.update(parse_params(full_link, headers))
            item_dict.update({'_id': full_link})
            item_dict.update({'image_link': image.get('src')})

            try:
                curr_collection.insert_one(item_dict)
            except DuplicateKeyError as e:
                continue

        prev_page = page.url
        time.sleep(1)


def parse_params(item_url, header):
    curr_url = f'{item_url}?tab=characteristic'
    page = requests.get(curr_url, headers=header)
    soup = bs(page.content, 'html.parser')
    dictionary_of_data = dict()
    params = soup.find_all('div',
                           class_='Characteristic_characteristic__K9KI-')
    for block in params:
        characteristics = list(map(lambda x: x.text,
                                   block.find_all('div', class_='row')))
        data_about_each = list(map(lambda x: x.text,
                                   block.find_all('p')))
        dictionary_of_data.update(dict(zip(characteristics, data_about_each)))

    time.sleep(1)
    return dictionary_of_data


# parse_cases(url_cases, headers, mydb, 'Cases')
# parse_cases(url_headphones, headers, mydb, 'Headphones')
parse_cases(url_hdd, headers, mydb, 'HDD_disks')
