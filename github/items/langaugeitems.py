import scrapy

class Item(scrapy.Item):

    # item for repo's language
    language = scrapy.Field()
    language_cnt = scrapy.Field()