# -*- coding:utf-8 -*-

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from Scrapy2.items import sinaPageSourceItem, sinaWeiboItem

class SinaWeiboSpider(CrawlSpider):

    name = 'sina_weibo_cn'

    def start_requests(self):

        allowed_domains = ['weibo.cn']
        start_urls = ['1087770692']					# 微博账号
        # 伪造Cookie登录（账号：yuxiaowei34@sina.com,密码：abcd1234）
        yield Request('http://weibo.cn', cookies={
            '_T_WM': 'f8850442330a42c8edae9d40b94d4bee',
            'SUB': 'AdtD7kDS/0F1ypCUw3GaLE+ADRiuG8kLWYK/DOIoKUWiUk+ScX2oPWFuIR/1/7CbLV8qI0H9oBC/q9vGB1c1eVaQpp8VjofL9RwF0M8jmqaRTUh+/rO1+SIrxTpG/ZLGIw7s5ugkfMp0KbdVgh+Jh68=',
            'gsid_CTandWM':'4uVa809114QMn0b4ki7JqlMT2an'
        })

        for url in self.start_urls:

            yield Request('http://weibo.cn/' + url, callback=self.parse_item)


    def parse_item(self, response):

        items = []

        # 保存网页源码
        page_source = sinaPageSourceItem()

        page_source['page_source'] = response.body
        page_source['url'] = response.url
        page_source['category'] = 'weibo'

        items.append(page_source)

        # 解析微博数据
        sel = Selector(response)

        weibos = sel.xpath('//div[@class="c"]')

        for weibo in weibos:

            item = sinaWeiboItem()
            item['user_id'] = response.url
            item['like'] = [s.encode('unicode_escape') for s in weibo.xpath('a[starts-with(@href, "http://weibo.cn/attitude")]/text()').extract()]
            item['forward'] = [s.encode('unicode_escape') for s in weibo.xpath('a[starts-with(@href, "http://weibo.cn/repost")]/text()').extract()]
            item['comment'] = [s.encode('unicode_escape') for s in weibo.xpath('a[starts-with(@href, "http://weibo.cn/comment") and contains(@href, "uid")]/text()').extract()]
            item['post_time'] =  [s.encode('unicode_escape') for s in weibo.xpath('span[@class="ct"]/text()').extract()]
            item['content1'] = [s.encode('unicode_escape') for s in weibo.xpath('div[1]//span[@class="ctt"]/text()').extract()]
            item['content2'] = [s.encode('unicode_escape') for s in weibo.xpath('div[3]/text()').extract()]
            item['forward_weibo_id'] = [s.encode('unicode_escape') for s in weibo.xpath('div[2]//a[@class="cc"]/@href').extract()]
            item['weibo_id'] = [s.encode('unicode_escape') for s in weibo.xpath('@id').extract()]

            items.append(item)

        return items




