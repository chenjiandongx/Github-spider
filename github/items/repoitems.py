import scrapy

class Item(scrapy.Item):

    # item for repo's stars and forks
    repo = scrapy.Field()
    repo_watch = scrapy.Field()
    repo_star = scrapy.Field()
    repo_fork = scrapy.Field()