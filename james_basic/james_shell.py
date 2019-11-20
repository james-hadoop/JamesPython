import os
import time
from selenium import webdriver
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse

url = "http://www.hangzhou.gov.cn/col/col1346101/"

# val = os.system(
#     "curl 'http://www.hangzhou.gov.cn/module/xxgk/search.jsp?texttype=0&fbtime=-1&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage=3&sortfield=,createdate:0,orderid:0' -H 'Connection: keep-alive' -H 'Accept: */*' -H 'Origin: http://www.hangzhou.gov.cn' -H 'X-Requested-With: XMLHttpRequest' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Referer: http://www.hangzhou.gov.cn/col/col1346101/' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' -H 'Cookie: JSESSIONID=F92EDACFCC10014FDDAF8BD6A0F9903F; _gscu_1342898206=732872035hmzcv17; yd_cookie=e3c1e9d2-bc54-435de00084fcd3f09f0345ffefd16ee933ce; Hm_lvt_e134fee1edb436d9a4b58261f92fdeb8=1573287268,1573690486,1574091075; Hm_lpvt_e134fee1edb436d9a4b58261f92fdeb8=1574091088' --data 'infotypeId=F010000202&jdid=149&area=&divid=div1345230&vc_title=&vc_number=&sortfield=,createdate:0,orderid:0&currpage=3&vc_filenumber=&vc_all=&texttype=0&fbtime=-1&texttype=0&fbtime=-1&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage=3&sortfield=,createdate:0,orderid:0' --compressed --insecure")
# print(val)

# browser = webdriver.Chrome(executable_path=r"/home/james/_AllDocMap/06_Software/chromedriver")
browser = webdriver.Chrome(executable_path=r"/Users/qjiang/_AllDocMap/06_Software/install/chromedriver")

browser.get(url)
source = browser.page_source
time.sleep(1)

target = browser.find_element_by_xpath(
    "/html/body/div[2]/table/tbody/tr/td[3]/table/tbody/tr/td/div/table/tbody/tr/td/table[1]/tbody/tr[7]/td[1]/a[2]")
target_url = target.get_attribute('href')

print(">>>")
print(browser.current_url)
print(target.text)
print(target_url)

target.click()

print(">>>")
print(browser.current_url)

browser.get(browser.current_url)
source = browser.page_source
time.sleep(1)

cont=browser.find_element_by_xpath("/html/body/div[3]/div[2]/table/tbody/tr/td/div")
print(">>>")
print(cont)