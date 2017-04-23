# -*- coding: utf-8 -*-

# Scrapy settings for github project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'github'

SPIDER_MODULES = ['github.spiders']
NEWSPIDER_MODULE = 'github.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'github (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# encoding setting
FEED_EXPORT_ENCODING = 'utf-8'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Maximum number of concurrent items (per response) to process in parallel in the Item Processor(defalut:100)
CONCURRENT_ITEMS = 100

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# The maximum limit for Twisted Reactor thread pool size. (defalut:10)
REACTOR_THREADPOOL_MAXSIZE = 10

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'github.middlewares.GithubSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
   # 'github.middlewares.MyCustomDownloaderMiddleware': 543,
   'github.middleware.useragent.RandomUserAgentMiddleware':400,
   'github.middleware.httpproxy.ProxyMiddleware':750,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'github.pipelines.GithubPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True


# The amount of time (in secs) that the downloader will wait before timing out.(defalut:180)
# Unless you are crawling from a very slow connection (which shouldn’t be the case for broad crawls)
# reduce the download timeout so that stuck requests are discarded quickly and
# free up capacity to process the next ones.
# recommend : DOWNLOAD_TIMEOUT = 15
DOWNLOAD_TIMEOUT = 180


# his setting is also affected by the RANDOMIZE_DOWNLOAD_DELAY setting (which is enabled by default).
# By default, Scrapy doesn’t wait a fixed amount of time between requests,
# but uses a random interval between 0.5 * DOWNLOAD_DELAY and 1.5 * DOWNLOAD_DELAY.
# DOWNLOAD_DELAY = 8
DOWNLOAD_DELAY = 4

# retry times when you failed a item
RETRY_TIMES = 5


# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
