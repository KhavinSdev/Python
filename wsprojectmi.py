#!/usr/bin/env python
# coding: utf-8

import lxml
import bs4
import requests


sf = int(input('How many pages of the shop would you like to view the titles?' + ' '))

for pg in range(sf + 1):
    request = requests.get(f'https://books.toscrape.com/catalogue/page-{pg}.html')
    wscrape = bs4.BeautifulSoup(request.text, 'lxml')
    for i in range(len(wscrape.select('.image_container'))):
        print(wscrape.select('.image_container')[i].select('img')[0]['alt']) 







