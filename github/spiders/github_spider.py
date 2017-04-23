import scrapy
import re
from github.items import langaugeitems,repoitems,useritems


class GithubSpider(scrapy.Spider):

    name = "github"

    def start_requests(self):

        # urls that search for repo's stars > 1000
        urls = ["https://github.com/search?p={page}&o=desc&q=stars%3A%3E1000&s=stars&type=Repositories&utf8=%E2%9C%93".format(page=page)
                for page in range(1, 2)]

        # urls that search for repo's forks > 1000
        # urls = ["https://github.com/search?p={page}&o=desc&q=forks%3A%3E1000&s=forks&type=Repositories&utf8=%E2%9C%93".format(page=page)
                # for page in range(1, 3)]

        # urls that search for user's followers > 1000
        # urls = ["https://github.com/search?p={page}&o=desc&q=followers%3A%3E1000&s=followers&type=Users&utf8=%E2%9C%93".format(page=page)
        #         for page in range(1, 3)]

        # parse language data
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse_page)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_language)


    def parse_page(self, response):

        html = response.body.decode("utf-8")

        # query for repo's stars and forks
        # repos = re.findall(r'(?<="v-align-middle">)[\w\/\-\.]+', html)
        #
        # for repo in repos:
        #     yield scrapy.Request(url="https://github.com/{}".format(repo), callback=self.parse_forks_stars)


        # query for user's data
        users = re.findall('(?<=ml-2\">\n\s{6}<a href=\")\S+(?=\">)', html)

        for user in users:
            yield scrapy.Request(url="https://github.com{}".format(user), callback=self.parse_user)


    def parse_forks_stars(self, response):

        html = response.body.decode("utf-8")
        repo_data = re.findall(r'(?<=aria-label=\")\d+', html)

        item = repoitems.Item()
        item['repo'] = response.url
        item['repo_watch'], item['repo_star'], item['repo_fork'] = repo_data
        yield item


    def parse_user(self, response):

        html = response.body.decode("utf-8")
        user_data = [data.strip() for data in re.findall('(?<=Counter\">)\s+\S+\s+', html)]

        item = useritems.Item()
        item['user'] = response.url
        item['user_repo'], item['user_star'], item['user_follower'], item['user_following']= user_data
        yield item


    def parse_language(self, response):

        html = response.body.decode("utf-8")

        language = re.findall(r'(?<=</span>\n\s{14})\S+', html)
        language_cnt = [l.replace(",","") for l in re.findall(r'(?<=count\">)\d*\,?\d+', html)]

        for z in zip(language, language_cnt):
            item = langaugeitems.Item()
            item['language'], item['language_cnt'] = z
            yield item

