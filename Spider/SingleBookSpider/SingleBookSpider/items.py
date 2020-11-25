# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinglebookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chapter_name = scrapy.Field()  # 章节名
    chapter_content = scrapy.Field()  # 章节内容
    chapter_index = scrapy.Field()  # 章节索引
