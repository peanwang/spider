# -*- coding: utf-8 -*-
"""
Created on Tue Feb 6 17:54:01 2020
@author: 王航
"""

import requests
import random
from lxml import etree
import sqlite3
import time
from multiprocessing import Pool

user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]


proxies = [
    {'http':'http://221.229.252.98:9797'},
    {'http':'http://119.57.156.90:53281'},
    {'http':'http://163.125.64.131:9797'},
    {'http':'http://1.197.16.228:9999'},
    {'http':'http://1.197.11.200:9999'},
    {'http':'http://112.12.37.196:53281'},
]

def get_html(url):
    '''
        给出url，返回网站内容
    '''
    headers ={
        'user-agent': random.choice(user_agent),
    }
    try:
        response = requests.get(url,headers=headers,proxies=random.choice(proxies),timeout=5)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError:
        raise requests.ConnectionError
        return None


def parse(html):
    root = etree.fromstring(html, parser=etree.HTMLParser())
    for item in root.xpath(r'//li[contains(@class,"con_list_item default_list")]'):
        yield{
            'company':              item.get('data-company'),
            'salary':               item.get('data-salary'),
            'require':              ''.join(item.xpath(r'descendant::div[@class="p_bot"]/div[@class="li_b_l"]/text()')).strip(),
            'Company benefits':     item.xpath(r'descendant::div[@class="li_b_r"]/text()')[0],
            'feature':              ''.join(item.xpath(r'descendant::div[@class="list_item_bot"]//div[@class="li_b_l"]/span/text()')),
            'industry':             item.xpath(r'descendant::div[@class="industry"]/text()')[0].strip(),
        }


def init_database(name):
    ''' 创建数据库，并初始化表'''
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE job (id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    company TEXT NOT NULL,salary TEXT NOT NULL,require TEXT NOT NULL,\
                    company_benefits TEXT NOT NULL,feature TEXT NOT NULL,industry TEXT NOT NULL)')
    cursor.close()
    conn.commit()
    conn.close()


def write_to_database(name, content):
    ''' 创建数据库，并初始化表'''
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO job (company,salary,require,company_benefits,feature,industry) \
                    VALUES (?,?,?,?,?,?)',\
                    (content['company'],content['salary'],content['require'],content['Company benefits'],content['feature'],content['industry']))
    cursor.close()
    conn.commit()
    conn.close()


def main(i):
    url = "https://www.lagou.com/zhaopin/Python/"+str(i)+"/"
    html = get_html(url)
    for item in parse(html):
        write_to_database('job.db', item)
    time.sleep(60)    
    print('page %s done.' % url)


if __name__ == "__main__":
    init_database('job.db')
    p = Pool()
    for i in range(1,31):
        p.apply_async(main, args=(i,))
    p.close()
    p.join()
    print('Done')   

