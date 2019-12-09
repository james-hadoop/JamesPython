import os
import time
import datetime
from selenium import webdriver
import pymysql

conn = None

keys = ['创新',
        '创业',
        '改革',
        '促进',
        '发展',
        '措施',
        '进一步',
        '扩大',
        '培育',
        '工作方案',
        '行动计划',
        '专项资金',
        '鼓励',
        '扶持',
        '加快',
        '管理',
        '推动',
        '激发',
        '实施方案',
        '推广',
        '产业',
        '推进',
        '加强',
        '改进',
        '提升',
        '规划',
        '落实',
        '政策',
        '征集',
        '建设',
        '构建',
        '行动方案',
        '实现',
        '开展',
        '开放',
        '总体方案',
        '投资',
        '补贴',
        '申报',
        '征收',
        '引导基金',
        '资助',
        '降低',
        '深化']

url = "http://www.hangzhou.gov.cn/col/col1346101/"

_sql = """
    insert into yqc_spider(id, title, url, pub_time, pub_org, doc_id, index_id, key_cnt, region, update_time, cont) values (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
      """


def getDbConnection():
    dbparams = {'host': '127.0.0.1',
                'port': 3306,
                'user': 'developer',
                'password': 'developer',
                'database': 'developer',
                'charset': 'utf8'
                }
    global conn
    conn = pymysql.connect(**dbparams)


getDbConnection()

cursor = conn.cursor()

browser = webdriver.Chrome(executable_path=r"/Users/qjiang/install/chromedriver")
browser2 = webdriver.Chrome(executable_path=r"/Users/qjiang/install/chromedriver")
browser.get(url)
source = browser.page_source
time.sleep(1)

targets = browser.find_elements_by_xpath("//tr[@class='tr_main_value_even']")
print(">>>")
i = 0
for t in targets:
    title = t.find_element_by_xpath("./td[1]/a").get_attribute('title')
    url = t.find_element_by_xpath("./td[1]/a").get_attribute('href')
    pub_time = t.find_element_by_xpath("./td[3]").text
    pub_org = t.find_element_by_xpath("./td[2]").text
    region = str('杭州')
    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    t.click()

    browser2.get(url)
    time.sleep(1)

    doc_id = browser2.find_element_by_xpath("/html/body/div[3]/table[2]/tbody/tr[2]/td[2]").text
    index_id = browser2.find_element_by_xpath("/html/body/div[3]/table[2]/tbody/tr[1]/td[2]").text
    cont = browser2.find_element_by_xpath("//td[@class='bt_content']").text

    key_cnt = 0
    for key in keys:
        if key in title:
            key_cnt += 1

    if key_cnt > 0:
        print(">>>")
        print(title)
        print(url)
        print(pub_time)
        print(pub_org)
        print(doc_id)
        print(index_id)
        print(key_cnt)
        cursor.execute(_sql, (
            title, url, pub_time, pub_org, doc_id, index_id, key_cnt, region, update_time, cont))

        conn.commit()
    i += 1