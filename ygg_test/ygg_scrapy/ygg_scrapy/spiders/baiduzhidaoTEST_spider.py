# -*- coding:utf-8 -*-

from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from ygg_scrapy.items import zhidaoItem

import urllib

class WeiboSpider(CrawlSpider):
    name = 'baiduzhidao'
    allowed_domains = ['baidu.com']
    start_urls = {
        '一汽大众'

    }

    def start_requests(self):

        for url in self.start_urls:

            yield Request('http://zhidao.baidu.com/index?pn=0&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=10&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=20&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=30&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=40&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=50&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=60&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=70&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=80&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=90&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=100&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=110&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=120&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=130&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=140&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=150&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=160&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=170&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=180&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})
            yield Request('http://zhidao.baidu.com/index?pn=190&device=mobile&word='+url, callback=self.parse_question_url,
                          meta = {'key_word': url})


    def parse_question_url(self, response):

        sel = Selector(response)

        reslist = sel.xpath('//div[@class="slist"][1]//a[@class="a2"]')

        for resItem in reslist:

            url = 'http://zhidao.baidu.com' + \
                  [s.encode('unicode_escape') for s in resItem.xpath('@href').extract()][0] + '&device=mobile'

            # 解析数据
            yield Request(url, callback=self.parse_item, meta = {'start_url': url, 'key_word': response.meta['key_word']})

    def parse_item(self, response):

        sel = Selector(response)

        # print response.meta['start_url']

        res = sel.xpath('//div[3]')

        items = []

        item = zhidaoItem()

        item['question'] = [s.encode('unicode_escape') for s in res.xpath('p[@class="b"]/text()').extract()]
        item['questioner'] = [s.encode('unicode_escape') for s in res.xpath('p[3]/a/text()').extract()]
        item['post_time'] = [s.encode('unicode_escape') for s in res.xpath('p[3]/span/text()').extract()]
        item['key_word'] = response.meta['key_word']

        question = item['question']
        questioner = item['questioner']
        post_time = item['post_time']
        key_word = item['key_word']

        if len(question) > 0:
            question = question[0]
        else:
            question = ''

        if len(questioner) > 0:
            questioner = questioner[0]
        else:
            questioner = ''

        if len(post_time) > 0:
            post_time = post_time[0]
        else:
            post_time = ''

        yield Request('http://www.baidu.com/p/' + urllib.quote(questioner.decode('unicode_escape').encode('utf-8')) + '/detail', callback=self.parse_item_profile, dont_filter=True,
                          meta = {'question': question, 'questioner': questioner, 'post_time': post_time, 'key_word': key_word})

    def parse_item_profile(self, response):

        sel = Selector(response)

        res = sel.xpath('//dl[@class="userdetail-profile-basic"]')

        profile = ''

        items = []

        item = zhidaoItem()

        item['question'] = response.meta['question']
        item['questioner'] = response.meta['questioner']
        item['post_time'] = response.meta['post_time']
        item['key_word'] = response.meta['key_word']

        for resItem in res:

            attrs = [s.encode('unicode_escape') for s in resItem.xpath('//span/text()').extract()]

            for i in range(0, len(attrs)):

                if i % 2 == 0:
                    profile += attrs[i] + ':'
                else:
                    profile += attrs[i] + ','

        item['profile'] = profile

        items.append(item)

        return items