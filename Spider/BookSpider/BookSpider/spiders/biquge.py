# -*- coding: utf-8 -*-
import scrapy
from items import BookspiderItem


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    # allowed_domains = ['xxx.com']
    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']

    def parse(self, response):
        novel_urls = response.xpath('.//ul/li/a/@href').extract()
        novel_names = response.xpath('.//ul/li/a/text()').extract()

        novel_urls = novel_urls[10:]
        novel_names = novel_names[10:]
        for novel_name, novel_url in zip(novel_names, novel_urls):
            yield scrapy.Request(novel_url, meta={'novel_name': novel_name, 'novel_url': novel_url}, callback=self.getDetail)

    def getDetail(self, response):
        novel_name = response.meta["novel_name"]
        novel_url = response.meta["novel_url"]
        # print(novel_name, novel_url)

        novel_author = response.xpath("//*[@id='info']/p[1]").extract()[0]
        novel_introduction = response.xpath('//*[@id="intro"]/p[2]/text()').extract()[0]
        novel_update_last_time = response.xpath("//*[@id='info']/p[3]").extract()[0]
        novel_update_last_url = response.xpath("//*[@id='info']/p[4]/a/@href").extract()[0]
        novel_update_last_name = response.xpath("//*[@id='info']/p[4]/a/text()").extract()[0]

        novel_introduction = self.easyIntroduction(novel_introduction)
        novel_author = self.authorToString(novel_author)
        novel_update_last_time = self.lastTimeToTime(novel_update_last_time)

        item = BookspiderItem()
        item['novel_name'] = novel_name
        item['novel_url'] = novel_url
        item['novel_author'] = novel_author
        item['novel_introduction'] = novel_introduction
        item['novel_update_last_time'] = novel_update_last_time
        item['novel_update_last_url'] = novel_update_last_url
        item['novel_update_last_name'] = novel_update_last_name

        return item

    def authorToString(self, string):
        string = repr(string)
        string = string.replace('<p>', '')
        string = string.replace('</p>', '')
        string = string.replace(r'\xa0', '')
        string = string.replace('作者：', '')
        string = string.replace("'", '')
        return string

    def lastTimeToTime(self, time):
        time = time.replace('<p>', '')
        time = time.replace('</p>', '')
        time = time[5:]

        return time

    def easyIntroduction(self, introduction):
        introduction = introduction.replace(' ', '')
        introduction = introduction.replace('\r', '')
        introduction = introduction.replace('\n', '')
        return introduction


