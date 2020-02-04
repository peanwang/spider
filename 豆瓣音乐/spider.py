import requests
import re
import json
import time


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36',
        'Host': 'music.douban.com'
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.text
    else:
        r.raise_for_status()
        return None


def parse_one_page(html):
    pattern = re.compile(r'<a href="https://music.douban.com/subject/.+?>(.+?)</a>.*?<p class="pl">(.+?)</p>[\s\n ]*<div class="star clearfix"><span class="allstar.."></span><span class="rating_nums">([\d.]+)</span>',re.S)
    items = pattern.findall(html)
    for item in items:
        yield{
            'song':item[0].replace('<span style="font-size:12px;">','').replace('</span>','').replace('  ','').replace('\n',' ').strip(),
            'singer':item[1].split('/')[0].strip(),
            'time':item[1].split('/')[1].strip(),
            'style':item[1].split('/',2)[2].strip(),
            'score':item[2]
        }            


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://music.douban.com/top250?start=' + str(offset)   
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)


if __name__ == "__main__":
    for i in range(10):
        main(offset = i*25) 
        time.sleep(1)