import random
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

class ProxyMiddleware(HttpProxyMiddleware):

    def __init__(self, proxies):
        self.proxies = proxies

    def process_request(self, request, spider):
        """  使用外部代理方法 """

        proxy = self.proxy_xxnet()
        request.meta['proxy'] = proxy

    @staticmethod
    def proxy_xxnet():
        """ 使用 xx-net 代理 """

        proxy = "http://127.0.0.1:8087"
        return proxy

    @staticmethod
    def proxy_shadowsocks():
        """ 使用 shadowsocks 代理 """

        proxy = "http://127.0.0.1:1080"
        return proxy

    @staticmethod
    def proxy_freeip():
        """ 使用免费 ip 代理，不过这个效果不佳 """

        ip_ports = [
            "http://82.43.21.165:3128",
            "http://185.112.234.4:80",
            "http://118.189.13.178:8080",
            "http://37.187.117.157:3128",
            "http://62.201.200.17:80",
            "http://181.143.28.210:3128",
            "http://216.190.97.3:3128",
            "http://183.111.169.205:3128"
        ]
        proxy = random.choice(ip_ports)
        return proxy
