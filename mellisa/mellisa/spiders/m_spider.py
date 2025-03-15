import scrapy
import os
import time
from misc.misc_prompts import Misc
from scrapy.loader import ItemLoader
from items import MellisaItem

class ScrapeParameters(scrapy.Spider):
    name = "param_spider"
    start_urls = []
    def __init__(self, url=None, start_urls=None, *args, **kwargs):
        super(ScrapeParameters, self).__init__(*args, **kwargs)
        self.datas = []
        self.data_len = 0 

        if url:
            self.start_urls = [f"{url}"]
        elif start_urls:
            self.start_urls = start_urls  

    def load_xpath(self, file_path):
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()] 

    def returnNumData(self, data_len):
        print("")
        return print(f"[✓] Total number of scraped parameter/s from page: {data_len}")

    def returnNone(self, data_len):
         misc = Misc()
         if data_len == 0:
            misc.misc_saving()
            print("[!] Page might not contain any parameters to be extracted, maybe try another one?")
            time.sleep(2)
            print("[!] No parameter/s were scraped from the page")

    def parse(self, response):
        path = os.path.join(os.path.expanduser("~"), "Mellisa_src/mellisa/mellisa/wordlist.txt")
        
        xpaths = self.load_xpath(path)

        loader = ItemLoader(item=MellisaItem(), response=response)

        if isinstance(xpaths, list):
             xpaths = xpaths[0] if xpaths else ""

        misc = Misc()
        misc.misc_start()

        self.datas = response.xpath(xpaths).extract()
        self.data_len = len(self.datas)

        loader.add_value("item_param", self.datas)

        yield loader.load_item()

    def closed(self, reason):
        misc = Misc()
        if self.datas:
            misc.misc_saving()
            self.returnNumData(self.data_len)

            misc.misc_output()
        else:
            self.returnNone(self.data_len)