import scrapy

class Item(scrapy.Item):

    user = scrapy.Field()
    user_repo = scrapy.Field()
    user_star = scrapy.Field()
    user_follower = scrapy.Field()
    user_following = scrapy.Field()
