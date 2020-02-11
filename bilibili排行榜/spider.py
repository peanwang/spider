# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:43:01 2020
@author: 王航
"""

import requests
import random
import json
import os
import tqdm
import pymongo
from urllib.parse import urlencode
from multiprocessing import Process

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
    {'http':'http://36.27.28.148:9999'},
    {'http':'http://114.99.13.58:9999'},
    {'http':'http://39.106.223.207:80'},
]

def get_json(url):
    '''
        给出url_api，返回json内容
    '''
    headers ={
        'user-agent': random.choice(user_agent),
    }
    try:
        response = requests.get(url,headers=headers,timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def parse(json):
    for item in json['data']['items']:
        yield{
            'uid':          item['user']['uid'],            # up主的id
            'head_url':     item['user']['head_url'],       #up主头像的图片
            'name':         item['user']['name'],           #up主名字
            'id':           str(item['item']['id']),             #视频id
            'pic':          item['item']['first_pic'],      #视频图片
            'title':        item['item']['description'],    #视频标题
            'upload_time':  item['item']['upload_time'],    #视频上传时间
            'watched_num':  item['item']['watched_num'],    #视频观看数
            'video_url':    item['item']['video_playurl'],  #视频地址
        }  


def save_image_video(title, head_url, video_url):
    headers ={
        'user-agent': random.choice(user_agent),
    }
    if not os.path.exists(title):
        os.mkdir(title)
    try:
        pic = requests.get(head_url,headers=headers, proxies=random.choice(proxies))
        if pic.status_code == 200:
            file_path = title+'/' + title + '.jpg'
            with open(file_path, 'wb') as f:
                f.write(pic.content)
    except requests.ConnectionError:
        print('%s.jpg failed to download' % title)
    else:
        print('%s.jpg download!!' % title)
    try:       
        video = requests.get(video_url,headers=headers, proxies=random.choice(proxies), stream=True)
        chunk_size = 1024
        if video.status_code == 200:
            file_path = title+ '/' + title + '.mp4'
            with open(file_path, 'ab') as f:
                for data in video.iter_content(chunk_size=chunk_size):
                    f.write(data)
    except requests.ConnectionError:
        print('%s.mp4 failed to download' % title)                
    else:
        print('%s.mp4 download' % title)


def initDB():   
    client = pymongo.MongoClient('127.0.0.1',27017)   # 连接MongoDB
    database = client.test                            # 连接数据库
    return database


def main():
    database = initDB()
    collection = database['video']
    base_url = "https://api.vc.bilibili.com/board/v1/ranking/top?"
    for i in (x*10 for x in range(10)):
        parms = {
            "page_size":"10",
            "next_offset":i+1,
            "tag":"今日热门",
            "platform":"pc"
        }
        url = base_url + urlencode(parms)
        json = get_json(url)
        for item in parse(json):
            collection.insert_one(item)
            p = Process(target=save_image_video, args=(item['id'], item['head_url'], item['video_url']))
            p.start()  


if __name__ == "__main__":
    main()  

