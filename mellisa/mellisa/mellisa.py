import argparse
import os
import sys
mellisa = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, mellisa)
import ascii.description_ascii
from scrapy.crawler import CrawlerProcess
from spiders.m_spider import ScrapeParameters
from scrapy.utils.project import get_project_settings
import ascii

class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def start_section(self, heading):
        # Replace "positional arguments" with custom heading
        if heading.lower() == 'positional arguments':
            heading = 'COMMANDS'
        return super().start_section(heading)

def run_spider(spider_name, output_file=None, **kwargs):
    settings = get_project_settings()
 
    if output_file:
        settings.update({
        'FEED_FORMAT': 'json',
        'FEED_URI': output_file,
        'FEED_EXPORT_ENCODING': 'utf-8'
    })

    process = CrawlerProcess(settings)
    process.crawl(spider_name, **kwargs)
    process.start()

def main():
    parser = argparse.ArgumentParser(description=ascii.description_ascii.mellisa_ascii, formatter_class=CustomHelpFormatter)
    parser.add_argument('spider', help='Name of the spider to run')
    parser.add_argument('url', help="URL of the website to crawl") 
    parser.add_argument('--o', '--output', dest='output', help="Output JSON file path") 

    args = parser.parse_args()

    spider_kwargs = {}
    if args.url:
        spider_kwargs['start_urls'] = [args.url]

    run_spider(args.spider, output_file=args.output,**spider_kwargs)

if __name__ == "__main__":
    main()