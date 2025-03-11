import scrapy
from scrapy.loader import ItemLoader
from items import MellisaItem

class ScrapeParameters(scrapy.Spider):
    name = "param_spider"

    start_urls = []
    def __init__(self, url=None, start_urls=None, *args, **kwargs):
        super(ScrapeParameters, self).__init__(*args, **kwargs)  
        if url:
            self.start_urls = [f"{url}"]
        elif start_urls:
            self.start_urls = start_urls  

    def load_xpath(self, file_path):
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]  

    def parse(self, response):
        path = "/home/yel/Mellisa_src/mellisa/mellisa/wordlist.txt"
        
        xpaths = self.load_xpath(path)

        loader = ItemLoader(item=MellisaItem(), response=response)

        for query in xpaths:
            loader.add_xpath("item_param", query)

        yield loader.load_item()
