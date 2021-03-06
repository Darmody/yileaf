#coding=utf-8
#-*- coding: UTF-8 -*-

'''

@author: caihuanyu
'''

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader.processor import Join

from ygg_scrapy.items import hupuTodayItem, hupuTopicItem, hupuDataItem

from ygg_app.models import site_hupu_today, site_hupu_topic, site_hupu_data

class hupuTodaySpider(Spider):
    
    name = "hupuToday"
    allowed_domains = ["hupu.com"]        # hupu NBA
    start_urls = [
        "http://nba.hupu.com"      # 首页
    ]
    
    def parse(self, response):
        
        sel = Selector(response)
       
        # 赛况信息
        reslist = sel.xpath('//div[@class="gamespace_list_no"]')
        # 清空数据
        site_hupu_today.objects.all().delete()

        items = []

        for resItem in reslist:

            item = hupuTodayItem()
            # 解析数据
            item['teamlogo1'] = [s.encode('unicode_escape') for s in resItem.xpath('table/tbody/tr[1]//span[contains(@class, "teamlogo")]/@class').extract()]
            item['title'] = [s.encode('unicode_escape') for s in resItem.xpath('table/tbody/tr[1]//span[@class="bifen"]/a/@title').extract()]
            item['titleLink'] = [s.encode('unicode_escape') for s in resItem.xpath('table/tbody/tr[1]//span[@class="bifen"]/a/@href').extract()]
            item['alert'] = [s.encode('unicode_escape') for s in resItem.xpath('table/tbody/tr[2]/td[1]/a/text()').extract()]
            item['alertLink'] = [s.encode('unicode_escape') for s in resItem.xpath('table/tbody/tr[2]/td[1]/a/@href').extract()]

            items.append(item)

        return items

class hupuTopicSpider(Spider):

    name = "hupuTopic"
    allowed_domains = ["hupu.com"]        # hupu NBA
    start_urls = [
        "http://nba.hupu.com"      # 首页
    ]

    def parse(self, response):

        sel = Selector(response)

        # 话题信息
        reslist = sel.xpath('//div[@class="retie"]//div[@class="list"]//li[not(@class="qu")]')

        # 清空数据
        site_hupu_topic.objects.all().delete()

        items = []

        i = 0;

        for resItem in reslist:

            item = hupuTopicItem()
            # 解析数据
            item['title'] = [s.encode('unicode_escape') for s in resItem.xpath('span[1]/a/text()').extract()]
            item['titleLink'] = [s.encode('unicode_escape') for s in resItem.xpath('span[1]/a/@href').extract()]
            item['reply'] = [s.encode('unicode_escape') for s in resItem.xpath('span[2]/text()').extract()]

            items.append(item)

            i += 1

            if i > 15:

                break

        return items

class hupuDataSpider(Spider):

    name = "hupuData"
    allowed_domains = ["hupu.com"]        # hupu NBA
    start_urls = [
        "http://nba.hupu.com"      # 首页
    ]

    def parse(self, response):

        sel = Selector(response)

        # 东部信息
        reslist = sel.xpath('//div[@id="zhanjitab_div0"]/div/table/tbody//tr')

        items = []
        # 所有属性赋值
        for i in range(1, len(reslist)):

            item = hupuDataItem()

            item['rank'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[1]/div/text()').extract()]
            item['teamName'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[2]/a/text()').extract()]
            item['win'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[3]/text()').extract()]
            item['lose'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[4]/text()').extract()]
            item['streak'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[5]/text()').extract()]
            item['difGames'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[6]/text()').extract()]
            item['dataType'] = '10'
            item['name'] = ['']

            items.append(item)

        # 西部信息
        reslist = sel.xpath('//div[@id="zhanjitab_div1"]/div/table/tbody//tr')

        # #所有属性赋值
        for i in range(1, len(reslist)):

            item = hupuDataItem()

            item['rank'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[1]/div/text()').extract()]
            item['teamName'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[2]/a/text()').extract()]
            item['win'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[3]/text()').extract()]
            item['lose'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[4]/text()').extract()]
            item['streak'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[5]/text()').extract()]
            item['difGames'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[6]/text()').extract()]
            item['dataType'] = '20'
            item['name'] = ['']

            items.append(item)

        # 球员当日得分数据
        reslist = sel.xpath('//div[@id="shujutab_div0"]/div/table/tbody//tr')

        # 所有属性赋值
        for i in range(1, len(reslist)):

            item = hupuDataItem()

            item['rank'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[1]/div/text()').extract()]
            item['name'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[2]/a/text()').extract()]
            item['teamName'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[3]/a/text()').extract()]
            item['win'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[4]/text()').extract()]
            item['dataType'] = '30'
            item['lose'] = ['']
            item['streak'] = ['']
            item['difGames'] = ['']

            items.append(item)

        #球员当日篮板数据
        reslist = sel.xpath('//div[@id="shujutab_div1"]/div/table/tbody//tr')

        # 所有属性赋值
        for i in range(1, len(reslist)):

            item = hupuDataItem()

            item['rank'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[1]/div/text()').extract()]
            item['name'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[2]/a/text()').extract()]
            item['teamName'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[3]/a/text()').extract()]
            item['win'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[4]/text()').extract()]
            item['dataType'] = '40'
            item['lose'] = ['']
            item['streak'] = ['']
            item['difGames'] = ['']

            items.append(item)

        #球员当日助攻数据
        reslist = sel.xpath('//div[@id="shujutab_div2"]/div/table/tbody//tr')

        # 所有属性赋值
        for i in range(1, len(reslist)):

            item = hupuDataItem()

            item['rank'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[1]/div/text()').extract()]
            item['name'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[2]/a/text()').extract()]
            item['teamName'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[3]/a/text()').extract()]
            item['win'] = [s.encode('unicode_escape') for s in reslist[i].xpath('td[4]/text()').extract()]
            item['dataType'] = '50'
            item['lose'] = ['']
            item['streak'] = ['']
            item['difGames'] = ['']

            items.append(item)


        # 清空数据
        site_hupu_data.objects.all().delete()


        return items