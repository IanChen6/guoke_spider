# -*- coding: utf-8 -*-

# Scrapy settings for guoke_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'guoke_spider'

SPIDER_MODULES = ['guoke_spider.spiders']
NEWSPIDER_MODULE = 'guoke_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guoke_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

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
#    'guoke_spider.middlewares.GuokeSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'guoke_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'guoke_spider.pipelines.JsonExporterPipeline': 2,
   #  'scrapy.pipelines.images.ImagesPipeline':1,
    'guoke_spider.pipelines.ArticleImagePipeline': 1,
    # 'guoke_spider.pipelines.ArticleImagePipeline': 1,
    # 'guoke_spider.pipelines.MysqlTwistedPipline': 3
    'guoke_spider.pipelines.MysqlPipeline': 2
    # 'guoke_spider.pipelines.MysqlTwistedPipline': 2

}
IMAGES_URLS_FIELD = "front_image_url"     # ITEM 中的图片 URL，用于下载
PROJECT_IMAGE_PATH = os.path.abspath(os.path.dirname(__file__))   # 获取当前文件所在目录
IMAGES_STORE = os.path.join(PROJECT_IMAGE_PATH, "images")         # 下载图片的保存位置,加上目录下的images文件夹（若不存在，会自动创建）

# IMAGES_MIN_WIDTH=100
# IMAGES_MIN_HEIGHT=100
#可自定义图片大小等参数

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
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

# DB_SERVER = 'MySQLdb'
# DB_CONNECT = {
#     'host' : 'localhost',
#     'user' : 'root',
#     'passwd' :1029384756,
#     'port' : 3306,
#     'db' :'bole_spider',
#     'charset' : 'utf8',
#     'use_unicode' : True
# }
