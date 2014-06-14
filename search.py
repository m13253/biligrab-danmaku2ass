#!/usr/bin/python3

import sys
import urllib.request
import urllib.parse
import gzip
from bs4 import BeautifulSoup

def print_hl(str):
    print ('\033[1m %s \033[0m' % str)


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
URL = 'http://www.bilibili.tv/search?keyword=' + urllib.parse.quote(sys.argv[1]);



req_headers = {'User-Agent': USER_AGENT, 'Accept-Encoding': 'gzip, deflate'}
req = urllib.request.Request(url=URL, headers=req_headers)
response = urllib.request.urlopen(req, timeout=120)
data = gzip.GzipFile(fileobj=response).read()

soup = BeautifulSoup(data)
target = soup.findAll(attrs={'class':'l'})

for i in target:
    _url = i.find('a').attrs['href']
    _t = i.find(attrs={'class':'t'})
    _ca = _t.find('span').contents[0]
    _t.find('span').clear()
    _tl = ''
    for string in _t.strings:
        _tl += string
    print_hl('>> ' + _tl)
    print(_ca + ' ' + _url + "\n")

