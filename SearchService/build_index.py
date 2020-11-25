# -*- encoding: utf-8 -*-
"""
@File    : build_index.py
@Time    : 2020/11/22
@Author  : Yuan Yifu
"""
from whoosh.fields import Schema, ID, TEXT
from whoosh.index import create_in, open_dir
from jieba.analyse import ChineseAnalyzer
import pymongo
from pymongo.collection import Collection
import os

# MongoDB database settings
# settings must be the same as before
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_DBNAME = "NovelDatabase"
MONGODB_SHEETNAME = "Biquge"


class IndexBuilder:
    def __init__(self):
        self.mongoClient = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        self.db = self.mongoClient[MONGODB_DBNAME]
        self.page = Collection(self.db, MONGODB_SHEETNAME)

    def build_index(self):
        analyzer = ChineseAnalyzer()

        # 创建索引模板
        schema = Schema(
            novelID=ID(stored=True),
            novelName=TEXT(stored=True, analyzer=analyzer),
            novelUrl=ID(stored=True),
            novelAuthor=TEXT(stored=True, analyzer=analyzer),
            novelIntroduction=TEXT(stored=True, analyzer=analyzer),
            novelUpdateTime=TEXT(stored=True),
            novelUpdateUrl=ID(stored=True),
            novelUpdateName=TEXT(stored=True)
        )

        # create/open index
        dir_path = 'novel_index'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            ix = create_in('novel_index', schema)
        else:
            ix = open_dir('novel_index')

        # build index
        writer = ix.writer()
        rows = self.page.find()
        indexed_amount = 0
        for row in rows:
            indexed_amount += 1
            writer.add_document(
                novelID=str(row['_id']),
                novelName=row['novel_name'],
                novelUrl=row['novel_url'],
                novelAuthor=row['novel_author'],
                novelIntroduction=row['novel_introduction'],
                novelUpdateTime=row['novel_update_last_time'],
                novelUpdateUrl=row['novel_update_last_url'],
                novelUpdateName=row['novel_update_last_name'],
            )
        writer.commit()
        print(indexed_amount)


if __name__ == '__main__':
    id = IndexBuilder()
    id.build_index()
