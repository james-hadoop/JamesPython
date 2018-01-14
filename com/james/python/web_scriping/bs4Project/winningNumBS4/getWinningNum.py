#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016年8月7日

@author: hstking hstking@hotmail.com
'''


import re
from bs4 import BeautifulSoup
import urllib2
from mylog import MyLog as mylog
from save2excel import SavaBallDate


class DoubleColorBallItem(object):
    date = None
    order = None
    red1 = None
    red2 = None
    red3 = None
    red4 = None
    red5 = None
    red6 = None
    blue = None
    money = None
    firstPrize = None
    secondPrize = None

class GetDoubleColorBallNumber(object):
    '''这个类用于获取双色球中奖号码， 返回一个txt文件
    '''
    def __init__(self):
        self.urls = []
        self.log = mylog()
        self.getUrls()
        self.items = self.spider(self.urls)
        self.pipelines(self.items)
        self.log.info('beging save data to excel \r\n')
        SavaBallDate(self.items)
        self.log.info('save data to excel end ...\r\n')
      
        
    def getUrls(self):
        '''获取数据来源网页
        '''
        URL = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
        htmlContent = self.getResponseContent(URL)
        soup = BeautifulSoup(htmlContent, 'lxml')
        tag = soup.find_all(re.compile('p'))[-1]
        pages = tag.strong.get_text()        
        for i in xrange(1, int(pages)+1):
            url = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(i) + '.html'
            self.urls.append(url)
            self.log.info(u'添加URL:%s 到URLS \r\n' %url)
            
    def getResponseContent(self, url):
        '''这里单独使用一个函数返回页面返回值，是为了后期方便的加入proxy和headers等
        '''
        try:
            response = urllib2.urlopen(url.encode('utf8'))
        except:
            self.log.error(u'Python 返回URL:%s  数据失败  \r\n' %url)
        else:
            self.log.info(u'Python 返回URUL:%s  数据成功 \r\n' %url)
            return response.read()
        
            
    def spider(self,urls):
        '''这个函数的作用是从获取的数据中过滤得到中奖信息
        '''
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            tags = soup.find_all('tr', attrs={})
            for tag in tags:
                if tag.find('em'):
                    item = DoubleColorBallItem()
                    tagTd = tag.find_all('td')
                    item.date = tagTd[0].get_text()
                    item.order = tagTd[1].get_text()
                    tagEm = tagTd[2].find_all('em')
                    item.red1 = tagEm[0].get_text()
                    item.red2 = tagEm[1].get_text()
                    item.red3 = tagEm[2].get_text()
                    item.red4 = tagEm[3].get_text()
                    item.red5 = tagEm[4].get_text()
                    item.red6 = tagEm[5].get_text()
                    item.blue = tagEm[6].get_text()
                    item.money = tagTd[3].find('strong').get_text()
                    item.firstPrize = tagTd[4].find('strong').get_text()
                    item.secondPrize = tagTd[5].find('strong').get_text()
                    items.append(item)
                    self.log.info(u'获取日期为:%s 的数据成功' %(item.date))
        return items
    
    def pipelines(self,items):
        fileName = u'双色球.txt'.encode('GBK')
        with open(fileName, 'w') as fp:
            for item in items:
                fp.write('%s %s \t %s %s %s %s %s %s  %s \t %s \t %s %s \n'
                      %(item.date,item.order,item.red1,item.red2,item.red3,item.red4,item.red5,item.red6,item.blue,item.money,item.firstPrize,item.secondPrize))
                self.log.info(u'将日期为:%s 的数据存入"%s"...' %(item.date, fileName.decode('GBK')))
                    

if __name__ == '__main__':
    GDCBN = GetDoubleColorBallNumber()
