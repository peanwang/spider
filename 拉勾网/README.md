### [拉勾网](https://github.com/peanwang/spider/tree/master/%E6%8B%89%E5%8B%BE%E7%BD%91)
使用requests下载网页，使用Python的multipleProcessing，实现多线程下载。使用XPATH提取信息(lxml库)。使用sqlite3把结果存入数据库。

拉勾网爬取的速度太快会导致验证码出现。试过很多方法：随机headers，随机代理(用的网上免费的)，最后还是sleep，降低爬取速度，才把数据全部爬完。


结果(使用SQLiteSpy可视化)
<br>
![result](https://github.com/peanwang/spider/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91/result.PNG)