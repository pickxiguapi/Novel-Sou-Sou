from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
import sys
import os
sys.path.append('..')
from SearchService.search import Searcher
import subprocess

# Create your views here.
s = Searcher('../SearchService/novel_index')


def search(request):
    print("request: ", request.method)
    if request.method == "POST":
        results = dict()
        search_name = request.POST.get('searchname')
        if 'zonghe' in request.POST:
            results = s.search(search_name)
            res_dict = {
                "results_num": len(results),
                "results": results,
            }
            # print("结果条数:", len(results))
        elif 'zuozhe' in request.POST:
            results = s.search_author(search_name)
            res_dict = {
                "results_num": len(results),
                "results": results,
            }
        elif 'shuming' in request.POST:
            results = s.search_name(search_name)
            res_dict = {
                "results_num": len(results),
                "results": results,
            }
        elif 'csrfmiddlewaretoken' in request.POST:
            url_dict = dict(request.POST)
            for url in url_dict:
                if url != 'csrfmiddlewaretoken':
                    print(url)
                    # r = RunSpider(url)
                    # r.run_scrapy()

                    # subprocess.Popen(r'G:\本科课程学习资料\NovelSearchEngine\Spider\SingleBookSpider\SingleBookSpider\Run.py', shell=True)

            res_dict = {
                "results_num": 1,
                "results": {"novelName": "Download Now!"},
                "results_download": "正在下载中......"
            }

        return render(request, 'SearchNovel/result.html', res_dict)
    else:
        return render(request, 'SearchNovel/search.html')


def result(request):
    pass
    return render(request, 'SearchNovel/result.html')

