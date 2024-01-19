import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from stack.items import StackItem

class StackCrawlerSpider(CrawlSpider):
    name = "stack_crawler"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest"]

    rules = (Rule(LinkExtractor(allow=r"questions\?tab=newest&page=\b[0-9]\b"), callback="parse_item", follow=True),)
    print('--------------------------------------------------')
    print(rules)
    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        questions=response.xpath('//h3[@class="s-post-summary--content-title"]')

        for question in questions:
            item=StackItem()
            item['title']=question.xpath('a[@class="s-link"]/text()').extract()[0]
            item['url']=question.xpath('a[@class="s-link"]/@href').extract()[0]
            yield item