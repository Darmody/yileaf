#coding=utf-8
#-*- coding: UTF-8 -*-

'''

@author: caihuanyu
'''

from scrapy.spider import Spider
from scrapy.selector import Selector

from ygg_scrapy.items import smzdmNoticeItem

from ygg_app.models import site_smzdm_notice

class smzdmSpider(Spider):
    
    name = "smzdm"
    allowed_domains = ["smzdm.com"]        # 什么值得买
    start_urls = [
        "http://www.smzdm.com/"      # 首页
    ]
    
    def parse(self, response):
        
        sel = Selector(response)
       
        # 资讯信息
        reslist = sel.xpath('//div[@class="perContentBox"]/div[@class="conCenterBlock"]/div[@class="conBox excerptBox"]')
        # 清空数据
        site_smzdm_notice.objects.all().delete()


        items = []

        for resItem in reslist:

            item = smzdmNoticeItem()
            # 解析数据
            item['zdmLink'] = [s.encode('unicode_escape') for s in resItem.xpath('div[@class="conRightBlock"]/div[@class="conRightPic"]/a/@href').extract()]
            item['zdmCoverLink'] = [s.encode('unicode_escape') for s in resItem.xpath('div[@class="conRightBlock"]/div[@class="conRightPic"]/a/img/@src').extract()]
            item['zdmTitle'] = [s.encode('unicode_escape') for s in resItem.xpath('div[@class="conRightBlock"]/div[@class="conRightPic"]/a/img/@title').extract()]
            item['buyLink'] = [s.encode('unicode_escape') for s in resItem.xpath('div[@class="conRightBlock"]/div[@class="bugBlock"]/a/@href').extract()]
            item['zdmContent'] = [s.encode('unicode_escape') for s in resItem.xpath('div[@class="p_excerpt"]/p[@class="p_excerpt"]/text()').extract()]

            items.append(item)


        return items