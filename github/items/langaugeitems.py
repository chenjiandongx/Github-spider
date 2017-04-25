import scrapy

class Item(scrapy.Item):

    language = scrapy.Field()
    language_cnt = scrapy.Field()