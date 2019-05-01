# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:44:46 2019

@author: pi

https://docs.python-guide.org/scenarios/scrape/
"""

from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print ('Buyers: ', buyers)
print ('Prices: ', prices)