# -*- coding: utf-8 -*-
import scrapy
from items import SinglebookspiderItem


class DownloadbookSpider(scrapy.Spider):
    name = 'downloadBook'

    def __init__(self, url=None, *args, **kwargs):
        super(DownloadbookSpider, self).__init__(*args, **kwargs)
        # allowed_domains = ['xxx.com']
        url_list = list()
        url_list.append(url)
        self.start_urls = url_list

    def parse(self, response):
        novel_catalog_name = response.xpath('//*[@id="list"]/dl/dd/a/text()').extract()
        novel_catalog_url = response.xpath('//*[@id="list"]/dl/dd/a/@href').extract()
        novel_catalog_url = ['http://xbiquge.la'+novel_catalog_url[i] for i in range(len(novel_catalog_url))]
        # print(novel_catalog_name[0], novel_catalog_url[0])
        chapter_index = 0
        for chapter_name, chapter_url in zip(novel_catalog_name, novel_catalog_url):
            chapter_index += 1
            yield scrapy.Request(chapter_url, meta={'chapter_name': chapter_name, 'chapter_index': chapter_index}, callback=self.downloadChapter,
                                 dont_filter=True)

    def downloadChapter(self, response):
        chapter_name = response.meta["chapter_name"]
        chapter_index = response.meta["chapter_index"]
        # print(chapter_name)

        chapter_content = response.xpath('//div[@id="content"]/text()').extract()

        chapter_string = ''
        for c in chapter_content:
            chapter_string += repr(c)
        chapter_string = chapter_string.replace(r'\xa0', '  ')
        chapter_string = chapter_string.replace(r'\r', '\n')
        chapter_string = chapter_string.replace("'", '')
        # print(chapter_string)

        item = SinglebookspiderItem()
        item['chapter_name'] = chapter_name
        item['chapter_content'] = chapter_string
        item['chapter_index'] = chapter_index
        return item
