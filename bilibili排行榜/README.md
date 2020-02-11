## [bilibili排行榜](https://github.com/peanwang/spider/tree/master/bilibili%E6%8E%92%E8%A1%8C%E6%A6%9C)
爬取[bilibili小视频排行榜](https://vc.bilibili.com/p/eden/rank#/?tab=%E5%85%A8%E9%83%A8)。
现把https://api.vc.bilibili.com/board/v1/ranking/top?信息爬取出来。返回的是JSON格式。
```python
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
```
把数据存入MongoDB

![pic](https://github.com/peanwang/spider/blob/master/bilibili%E6%8E%92%E8%A1%8C%E6%A6%9C/mongodb.PNG)


第二步：使用Python的multipleProcessing，下载图片和视频。遗憾的时，有的没有下载成功。

第三步：又写了一个爬虫，把没有下载成功的，通过MongoDB查询到对应的图片和视频网址，下载👀👀。

