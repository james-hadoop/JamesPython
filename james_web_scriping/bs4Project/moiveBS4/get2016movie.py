#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016��8��13��

@author: hstking hstking@hotmail.com
'''

from bs4 import BeautifulSoup
import urllib2
import codecs
from mylog import MyLog as mylog


class MovieItem(object):
    movieName = None
    movieScore = None
    movieStarring = None

class GetMovie(object):
	'''获取电影信息 '''
    def __init__(self):
        self.urlBase = 'http://dianying.2345.com/list/----2016---1.html'
        self.log = mylog()
        self.pages = self.getPages()
        self.urls = []  #url池
        self.items = []
        self.getUrls(self.pages) #获取抓取页面的url
        self.spider(self.urls)
        self.pipelines(self.items)
        
    def getPages(self):
		'''获取总页数 '''
        self.log.info(u'开始获取页数')
        htmlContent = self.getResponseContent(self.urlBase)
        soup = BeautifulSoup(htmlContent, 'lxml')
        tag = soup.find('div', attrs={'class':'video_page'})
        subTags = tag.find_all('a')
        self.log.info(u'获取页数成功')
        return int(subTags[-2].get_text())
    
    def getResponseContent(self, url):
		'''获取页面返回的数据 '''
        fakeHeaders= {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}  
        request = urllib2.Request(url.encode('utf8'), headers=fakeHeaders)
        
        proxy = urllib2.ProxyHandler({'http':'http://192.168.2.99:1080'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        try:
            response = urllib2.urlopen(request)
        except:
            self.log.error(u'Python 返回URL:%s  数据失败' %url)
        else:
            self.log.info(u'Python 返回URUL:%s  数据成功' %url)
            return response.read()
    
    def getUrls(self, pages):
        urlHead = 'http://dianying.2345.com/list/----2016---'
        urlEnd = '.html'
        for i in xrange(1,pages + 1):
            url = urlHead + str(i) + urlEnd
            self.urls.append(url)
            self.log.info(u'添加URL:%s 到URLS列表' %url)
    
    def spider(self, urls):
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            anchorTag = soup.find('ul', attrs={'class':'globalPicTxt pic140 clearfix'})
            tags = anchorTag.find_all('li')
            for tag in tags:
                item = MovieItem()
                item.movieName = tag.find('span', attrs={'class':'sTit'}).get_text()
                item.movieScore = tag.find('span', attrs={'class':'pRightBottom'}).em.get_text().replace(u'分', '')
                item.movieStarring = tag.find('span', attrs={'class':'sDes'}).get_text().replace(u'主演：', '')
                self.items.append(item)
                self.log.info(u'获取电影名为：<<%s>>成功' %(item.movieName))
    
    def pipelines(self, items):
        fileName = u'2016热门电影.txt'.encode('GBK')
        with codecs.open(fileName, 'w', 'utf8') as fp:
            for item in items:
                fp.write('%s \t %s \t %s \r\n' %(item.movieName, item.movieScore, item.movieStarring))
                self.log.info(u'电影名为：<<%s>>已成功存入文件"%s"...' %(item.movieName, fileName.decode('GBK')))
            


if __name__ == '__main__':
    GM = GetMovie()
