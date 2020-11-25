# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class SinglebookspiderPipeline(object):
    def __init__(self):
        self.current_dir = os.getcwd()

    def process_item(self, item, spider):
        dir_path = os.path.join(self.current_dir, 'content')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        filepath = os.path.join(dir_path, str(item['chapter_index']) + '.' + item['chapter_name'] + ".txt")
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(item['chapter_content'])
        return item
