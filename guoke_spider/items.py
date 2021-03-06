# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join, TakeFirst
import re
from util_for_url.common import get_md5

class GuokeSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JoBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    tag = scrapy.Field()
    content = scrapy.Field()

#    # 重定义Item类
    # def get_nums(value):
    #     """
    #     通过正则表达式获取 评论数，点赞数和收藏数
    #     """
    #     re_match = re.match(".*?(\d+).*", value)
    #     if re_match:
    #         nums = (int)(re_match.group(1))
    #     else:
    #         nums = 0
    #
    #     return nums
    #
    # def get_date(value):
    #     re_match = re.match("([0-9/]*).*?", value.strip())
    #     if re_match:
    #         create_date = re_match.group(1)
    #     else:
    #         create_date = ""
    #     return create_date
    #
    # def remove_comment_tag(value):
    #     """
    #     去掉 tag 中的 “评论” 标签
    #     """
    #     if "评论" in value:
    #         return ""
    #     else:
    #         return value
    #
    # def return_value(value):
    #     """
    #     do nothing, 只是为了覆盖 ItemLoader 中的 default_processor
    #     """
    #     return value
    # title = scrapy.Field()
    # create_date = scrapy.Field(     # 创建时间
    #     input_processor = MapCompose(get_date),
    #     output_processor = Join("")
    # )
    # url = scrapy.Field()            # 文章路径
    # front_image_url = scrapy.Field(    # 文章封面图片路径,用于下载，赋值时必须为数组形式
    #     # 默认 output_processor 是 TakeFirst()，这样返回的是一个字符串，不是 list，此处必须是 list
    #     # 修改 output_processor
    #     output_processor = MapCompose(return_value)
    # )
    # front_image_path = scrapy.Field()
    # # front_image_url = scrapy.Field()
    # fav_nums = scrapy.Field(        # 收藏数
    #     input_processor=MapCompose(get_nums)
    # )
    # comment_nums = scrapy.Field(    # 评论数
    #     input_processor=MapCompose(get_nums)
    # )
    # vote_nums = scrapy.Field(       # 点赞数
    #     input_processor=MapCompose(get_nums)
    # )
    # tags = scrapy.Field(           # 标签分类 label
    #     # 本身就是一个list, 输出时，将 list 以 commas 逗号连接
    #     input_processor = MapCompose(remove_comment_tag),
    #     output_processor = Join(",")
    # )
    # content = scrapy.Field(        # 文章内容
    #     # content 我们不是取最后一个，是全部都要，所以不用 TakeFirst()
    #     output_processor=Join("")
    # )
    # url_object_id = scrapy.Field()      # 文章内容的md5的哈希值，能够将长度不定的 url 转换成定长的序列
    #

# class ArticleItemloader(ItemLoader):
#     """
#       自定义 ItemLoader, 就相当于一个容器
#       """
#     # 这里表示，输出获取的 ArticleItemLoader 提取到的值，都是 list 中的第一个值
#     # 如果有的默认不是取第一个值，就在 Field() 中进行修改
#     default_output_processor = TakeFirst()