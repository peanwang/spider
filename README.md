# Python3 爬虫学习
-------------------
##### [囧事百科](https://github.com/peanwang/spider/tree/master/%E5%9B%A7%E4%BA%8B%E7%99%BE%E7%A7%91)
爬虫初体验：使用urllib (仅下载了HTML文件)



##### [豆瓣英语](https://github.com/peanwang/spider/tree/master/%E8%B1%86%E7%93%A3%E9%9F%B3%E4%B9%90)
使用requests下载网页。使用正则表达式提取信息，遍历提取结果并生成字典。最后使用JSON库里的dumps()方法实现字典的序列化



##### [笔趣阁](https://github.com/peanwang/spider/tree/master/%E7%AC%94%E8%B6%A3%E9%98%81)
使用requests下载网页。使用Python的multipleProcessing，实现多进程下载(多进程下载好快)。使用Beautiful Soup提取信息，遍历提取结果并生成字典。最后使用JSON库里的dumps()方法实现字典的序列化(Beautiful Soup挺好用，可以节约时间)

##### [拉勾网](https://github.com/peanwang/spider/tree/master/%E6%8B%89%E5%8B%BE%E7%BD%91)
使用requests下载网页，使用Python的multipleProcessing，实现多线程下载。使用XPATH提取信息(lxml库)。使用sqlite3把结果存入数据库。

##### [快代理](https://github.com/peanwang/spider/tree/master/%E5%BF%AB%E4%BB%A3%E7%90%86)
使用requests下载网页。使用Beautiful Soup提取信息。使用Python的multipleProcessing，实现多线程检测代理ip是否有用。最后存入txt