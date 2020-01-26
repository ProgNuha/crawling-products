# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductsECommerceItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    source_image = scrapy.Field()
    link_url = scrapy.Field()
