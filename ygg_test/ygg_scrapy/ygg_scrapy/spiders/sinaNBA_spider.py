#coding=utf-8
#-*- coding: UTF-8 -*-

'''

@author: caihuanyu
'''

from scrapy.spider import Spider
from scrapy.selector import Selector

from ygg_scrapy.items import sinaNBAVideoItem

from ygg_app.models import site_sinaNBA_video

class sinaTodaySpider(Spider):
    
    name = "sinaNBAVideo"
    allowed_domains = ["sina.com.cn"]        # sina NBA
    start_urls = [
        "http://sports.sina.com.cn/nba/"      # 首页
    ]
    
    def parse(self, response):
        
        sel = Selector(response)
       
        # 视频信息
        reslist = sel.xpath('//div[@id="videoPageControlWrapper_1"]//div[@class="video"]')
        # 清空数据
        site_sinaNBA_video.objects.all().delete()



        items = []

        for resItem in reslist:

            item = sinaNBAVideoItem()
            # 解析数据
            item['coverAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/img/@src').extract()]
            item['videoName'] = [s.encode('unicode_escape') for s in resItem.xpath('a/span/text()').extract()]
            item['videoAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/@href').extract()]
            item['videoType'] = '0'

            items.append(item)


        # 视频信息
        reslist = sel.xpath('//div[@id="videoPageControlWrapper_5"]//div[@class="video"]')

        for resItem in reslist:

            item = sinaNBAVideoItem()
            # 解析数据
            item['coverAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/img/@src').extract()]
            item['videoName'] = [s.encode('unicode_escape') for s in resItem.xpath('a/span/text()').extract()]
            item['videoAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/@href').extract()]
            item['videoType'] = '1'


            items.append(item)

        # 视频信息
        reslist = sel.xpath('//div[@id="videoPageControlWrapper_6"]//div[@class="video"]')

        for resItem in reslist:

            item = sinaNBAVideoItem()
            # 解析数据
            item['coverAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/img/@src').extract()]
            item['videoName'] = [s.encode('unicode_escape') for s in resItem.xpath('a/span/text()').extract()]
            item['videoAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/@href').extract()]
            item['videoType'] = '2'


            items.append(item)

        # 视频信息
        reslist = sel.xpath('//div[@id="videoPageControlWrapper_8"]//div[@class="video"]')

        for resItem in reslist:

            item = sinaNBAVideoItem()
            # 解析数据
            item['coverAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/img/@src').extract()]
            item['videoName'] = [s.encode('unicode_escape') for s in resItem.xpath('a/span/text()').extract()]
            item['videoAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/@href').extract()]
            item['videoType'] = '3'


            items.append(item)

        # 视频信息
        reslist = sel.xpath('//div[@id="videoPageControlWrapper_9"]//div[@class="video"]')

        for resItem in reslist:

            item = sinaNBAVideoItem()
            # 解析数据
            item['coverAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/img/@src').extract()]
            item['videoName'] = [s.encode('unicode_escape') for s in resItem.xpath('a/span/text()').extract()]
            item['videoAddress'] = [s.encode('unicode_escape') for s in resItem.xpath('a/@href').extract()]
            item['videoType'] = '4'


            items.append(item)


        return items