from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
import random

class ProxyMiddleware(HttpProxyMiddleware):
    """ overwrite process request """

    def __init__(self, proxy):
        self.proxy = proxy

    def process_request(self, request, spider):
        # Set the location of the proxy

        # using XX-NET port
        proxy = "http://127.0.0.1:8087"

        # using shadowsocks port
        # proxy = "http://127.0.0.1:1080"

        # proxy = random.choice(self.proxies_list)
        request.meta['proxy'] = proxy

    proxies_list = [
        "http://82.43.21.165:3128",
        "http://185.112.234.4:80",
        "http://118.189.13.178:8080",
        "http://37.187.117.157:3128",
        "http://62.201.200.17:80",
        "http://181.143.28.210:3128",
        "http://216.190.97.3:3128",
        "http://183.111.169.205:3128"
    ]
