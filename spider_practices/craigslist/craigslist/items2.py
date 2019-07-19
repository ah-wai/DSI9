# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class CraigslistItem(scrapy.Item):
    # Define the fields for your item here like:
    # name = scrapy.Field()
    restaurant_name = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    calories = scrapy.Field()
    fats = scrapy.Field()
    carbs = scrapy.Field()
