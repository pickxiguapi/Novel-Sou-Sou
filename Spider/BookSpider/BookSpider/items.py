# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novel_name = scrapy.Field()  # 小说名称
    novel_url = scrapy.Field()  # 小说链接
    novel_author = scrapy.Field()  # 小说作者
    novel_introduction = scrapy.Field()  # 小说简介
    novel_update_last_time = scrapy.Field()  # 最新章节更新时间
    novel_update_last_url = scrapy.Field()  # 最新章节链接
    novel_update_last_name = scrapy.Field()  # 最新章节名
