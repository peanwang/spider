import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import time
import socket


def write_file(response, filename):
    content = response.read()
    with open(filename, 'wb') as f:
        f.write(content)


def spider(url, headers, array):
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    _headers = list()
    for item in headers:
        _headers.append((item, headers[item]))
    opener.addheaders = _headers
    print('\n\n\n')
    for i in array:
        if i%500 == 0:
            time.sleep(60)
        _url = url+str(i)+'.html'
        try:
            response = opener.open(_url, timeout=5)
        except urllib.error.HTTPError as e:
            print(e.reason, e.code, e.headers)
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                print('Time Out\n')
            else:
                print(e.reason)
        else:
            filename = str(i)+'.html'
            write_file(response, filename)


if __name__ == '__main__':
    url = 'http://www.cnxox.com/news/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Connection': 'keep - alive',
        'Host': 'www.cnxox.com'
    }
    array = range(13500, 13510)
    spider(url, headers, array)
