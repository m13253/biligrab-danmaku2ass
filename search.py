#!/usr/bin/python3

import sys
import urllib.parse
import json
from biligrab import urlfetch

def print_hl(str):
    print ('\033[1m %s \033[0m' % str)


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
APPKEY = '876fe0ebd0e67a0f'


def main():
    _, resp = urlfetch('http://api.bilibili.tv/search?type=json&appkey=' + APPKEY + '&keyword=' + urllib.parse.quote(sys.argv[1]))
    data = json.loads( resp.decode('utf-8', 'replace') )
    for k, v in data['result'].items():
        print_hl(' >> ' + v['title']);
        if v['type'] == 'video':
            print('  [Video] Author:' + v['author'] + ' Play:' + v['play'] + ' Favorites:' +  v['favorites'] + ' Review:' + v['review'] + ' Comment:' + v['video_review']);
            print('  http://www.bilibili.tv/video/av' + str(v['aid']) + "\n")
        elif v['type'] == 'special':
            print("  [Special]")
            print('  http://www.bilibili.tv/sp/' + str(v['spid']) + "\n")

if __name__ == '__main__':
    sys.exit(main())
