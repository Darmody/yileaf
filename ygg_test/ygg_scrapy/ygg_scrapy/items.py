# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from ygg_app.models import site_hupu_today, site_hupu_topic, site_hupu_data, site_sinaNBA_video, site_smzdm_notice

class YggScrapyItem(Item):

    testvalue = Field()

class hupuTodayItem(DjangoItem):

    django_model = site_hupu_today

class hupuTopicItem(DjangoItem):

    django_model = site_hupu_topic

class hupuDataItem(DjangoItem):

    django_model = site_hupu_data

class sinaNBAVideoItem(DjangoItem):

    django_model = site_sinaNBA_video

class smzdmNoticeItem(DjangoItem):

    django_model = site_smzdm_notice

class weiboItem(Item):

    page_source = Field()

class zhidaoItem(Item):

    question = Field()

    post_time = Field()

    questioner = Field()

    # page_source = Field()

    key_word = Field()

    profile = Field()