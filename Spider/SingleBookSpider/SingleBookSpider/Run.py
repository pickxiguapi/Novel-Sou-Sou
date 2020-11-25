from scrapy import cmdline


class RunSpider(object):
    def __init__(self, url):
        self.url = url

    def run_scrapy(self):
        url = str(self.url)
        cmdline.execute(('scrapy crawl downloadBook -a url=' + url).split())


if __name__ == '__main__':
    r = RunSpider("http://www.xbiquge.la/69/69111/")
    r.run_scrapy()
