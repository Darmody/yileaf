__author__ = 'caihuanyu'
#coding=utf-8
#-*- coding: UTF-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector

class YyetsSearchSpider(Spider):

    name = "YyetsSearchSpider"
    allowed_domains = ["yyets.com"]
    start_urls = [

    ]

    def __init__(self, p='', domain=None):
        self.start_urls = ['http://www.yyets.com/search/%s' % p]


    def parse(self, response):

        sel = Selector(response)

        resList = sel.xpath('//div[@class="resource-list-box"]/dl[@class="resource-list"]')
        resItems = resList.xpath('//dd[@class=" resource-item" and @data-season="4"] | //dd[@class="odd resource-item" and @data-season="4"]')     #获取第4季

        print self.start_urls

        items = []

        # for resItem in resItems:

            # item['testvalue'] = [s.encode('unicode_escape') for s in resItem.xpath('a[not(@class="type")]/text()').extract()]

            # item['downloadLink'] = (resItem.xpath('span/a[@data-download-type="1"]/@href').extract())
            #
            # if len(resItem.xpath('a[not(@class="type")]/img/@src').extract()) > 0:
            #
            #     item['isNew'] = True
            # else:
            #
            #     item['isNew'] = False

            # items.append(item)

        return items


