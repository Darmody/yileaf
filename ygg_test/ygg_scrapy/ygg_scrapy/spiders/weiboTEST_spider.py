# -*- coding:utf-8 -*-

from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from ygg_scrapy.items import weiboItem

class WeiboSpider(CrawlSpider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = {
        '1087770692',   # 陈坤
        # '1266321801',   # 姚晨
        # '1197161814',   # 李开复
        # '1854283601',   #郭德纲
        # '1608574203',   #林志颖
        # '3994153024',   #某屌丝同学
        # '1650286893',   #某屌丝同学
        # '1781140153',   #某屌丝同学
        # '1894519637',   #某屌丝同学
        # '1769711181',   #某屌丝同学

    }

    def start_requests(self):

        yield Request('http://weibo.cn', cookies={
            '_T_WM': 'f8850442330a42c8edae9d40b94d4bee',
            'SUB': 'AR5tApUHJV6sblwsTrTcYW06e6WFt6FNyp/Hdg0yDnFgZo8y2Sibe/VLNLqxbD5V+7v+9qzaz/fDrs6EuhJ6wc+CZGYuYuOeefbGUhEb1u99Ir+fGjTVH3RautUvZKJ5EJ/THP0Bokdz1Z34c0VYxVU=',
            'gsid_CTandWM':'4uFA80911OZgXioJ0OVF5lMT2an'
        })

        for url in self.start_urls:

            yield Request('http://weibo.com/p/100808a1a975713ff307462a4cf778396a58aa', callback=self.parse_item, dont_filter=True, meta = {'renderjs': True})
            # yield Request('http://weibo.cn/' +url + '/follow', callback=self.parse_item, dont_filter=True)
            # yield Request('http://weibo.cn/' +url + '/info', callback=self.parse_item, dont_filter=True)
            # yield Request('http://weibo.cn/' +url + '/fans', callback=self.parse_item, dont_filter=True)


    def parse_item(self, response):

        items = []

        item = weiboItem()

        item['page_source'] = response.body

        items.append(item)

        return items
