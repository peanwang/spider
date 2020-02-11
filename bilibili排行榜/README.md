##### [bilibili小视频排行榜](https://github.com/peanwang/spider/tree/master/%E5%BF%AB%E4%BB%A3%E7%90%86)
爬取[bilibili小视频排行榜](https://vc.bilibili.com/p/eden/rank#/?tab=%E5%85%A8%E9%83%A8)。
现把https://api.vc.bilibili.com/board/v1/ranking/top?信息爬取出来
import requests
import random
import re
import json
import os
import tqdm
import pymongo
from urllib.parse import urlencode
from multiprocessing import Process