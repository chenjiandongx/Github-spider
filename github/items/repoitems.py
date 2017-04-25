import scrapy

class Item(scrapy.Item):

    repo = scrapy.Field()
    repo_watch = scrapy.Field()
    repo_star = scrapy.Field()
    repo_fork = scrapy.Field()