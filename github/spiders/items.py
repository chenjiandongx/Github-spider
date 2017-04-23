# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubItem(scrapy.Item):

    # item for repo's stars and forks
    # repo = scrapy.Field()
    # repo_watch = scrapy.Field()
    # repo_star = scrapy.Field()
    # repo_fork = scrapy.Field()


    # item for user's data
    # user = scrapy.Field()
    # user_repo = scrapy.Field()
    # user_star = scrapy.Field()
    # user_follower = scrapy.Field()
    # user_following = scrapy.Field()


    # item for repo's language
    language = scrapy.Field()
    language_cnt = scrapy.Field()