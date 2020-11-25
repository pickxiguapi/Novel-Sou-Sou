# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import codecs
import json
import pymongo
from scrapy.utils.project import get_project_settings


class BookspiderPipeline(object):
    def __init__(self):
        self.post = None
        self.current_dir = os.getcwd()
        self.get_setting()

    def get_setting(self):
        settings = get_project_settings()
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]

        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    '''
    def process_item(self, item, spider):
        """
        output json function
        :param item: 
        :param spider: 
        :return: 
        """
        dir_path = os.path.join(self.current_dir, 'novel')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        novel_path = os.path.join(dir_path, 'novel_data.json')

        novel_file = codecs.open(novel_path, 'a', 'gbk')
        line = json.dumps(dict(item), ensure_ascii=False)
        novel_file.write(line)
        novel_file.close()
        return item
    '''

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert_one(data)
        return item
