# -*- encoding: utf-8 -*-
"""
@File    : search.py
@Time    : 2020/11/22 
@Author  : Yuan Yifu
"""
import os
from whoosh.index import open_dir
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh import sorting

LIMIT = None  # 显示所有匹配的结果


class Searcher(object):
    def __init__(self, path):
        if os.listdir(path):
            self.ix = open_dir(path)
            self.searcher = self.ix.searcher()

    def search(self, key_word):
        # qp = QueryParser("novelName", schema=self.ix.schema)
        qp = MultifieldParser(["novelName", "novelAuthor", "novelIntroduction"], schema=self.ix.schema)
        q = qp.parse(key_word)

        # score
        scores = sorting.ScoreFacet()

        results = self.searcher.search(q, limit=LIMIT, sortedby=[scores])
        print(len(results))
        for i in results:
            print(i)
            # print(i.highlights())
            # print(i.more_like_this("novelAuthor"))

        return results

    def search_author(self, key_word):
        qp = QueryParser("novelAuthor", schema=self.ix.schema)
        q = qp.parse(key_word)

        # score
        scores = sorting.ScoreFacet()

        results = self.searcher.search(q, limit=LIMIT, sortedby=[scores])
        print(len(results))
        for i in results:
            print(i)

        return results

    def search_name(self, key_word):
        qp = QueryParser("novelName", schema=self.ix.schema)
        q = qp.parse(key_word)

        # score
        scores = sorting.ScoreFacet()

        results = self.searcher.search(q, limit=LIMIT, sortedby=[scores])
        print(len(results))
        for i in results:
            print(i)

        return results

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.searcher.close()
        print('Search End')


if __name__ == '__main__':
    s = Searcher('./novel_index')
    s.search("乌贼")
