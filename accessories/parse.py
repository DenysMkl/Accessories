import json
import time

import requests
import schedule
from bs4 import BeautifulSoup as bs
from pymongo.errors import DuplicateKeyError

import config
from storage.mongoDB import MongoDB

mongodb = MongoDB()
mydb = mongodb.db_name


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

            item_dict.update(parse_params(full_link, header))
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


def parse_all_links(database):
    with open('../urls_parse.json') as file:
        urls = json.load(file)
        for name, url in urls.items():
            mongodb.delete_data(database[name])
            parse_cases(url, config.HEADERS, mydb, name)


def run():
    # schedule.every().day.at("12:00").do()
    parse_all_links(mydb)


if __name__ == '__main__':
    run()
