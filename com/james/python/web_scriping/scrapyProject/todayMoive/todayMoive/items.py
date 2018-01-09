# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TodaymoiveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	cinema = scrapy.Field()		#影院名称
	moiveName = scrapy.Field()	#电影名字
