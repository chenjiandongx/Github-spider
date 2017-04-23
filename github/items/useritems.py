import scrapy

class Item(scrapy.Item):

    # item for user's data
    user = scrapy.Field()
    user_repo = scrapy.Field()
    user_star = scrapy.Field()
    user_follower = scrapy.Field()
    user_following = scrapy.Field()
