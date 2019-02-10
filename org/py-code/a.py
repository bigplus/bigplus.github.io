#! /usr/bin/env python
# coding:utf-8

# start : http://www.120ask.com/question/70000000.htm
# stop  : http://www.120ask.com/question/70599999.htm

import urllib2
# class Crawler:
def get_data_from_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0)')
    urllib2.socket.setdefaulttimeout(10) # 超时10秒
    page = urllib2.urlopen(req)
    data = page.read()
    # print data
    # print len(data) #计算字节长度
    return data

# TEMPLATE = 'http://www.120ask.com/question/70599999.htm'
TEMPLATE = 'http://www.120ask.com/question/'

def get_all():
    # http://www.120ask.com/question/65190877.htm
    # for i in range(70000000, 70599999):
    for i in range(70000030, 70000039):
        tmp_url = TEMPLATE + str(i) + '.htm'
        print tmp_url
        f = open(str(i), 'w')
        f.write(get_data_from_url(tmp_url))
        f.close()
        import time
        # time.sleep(10 * 1)
if __name__ == '__main__':
    get_all()
  # me=Crawler()
  # data = me.get_data_from_url('http://www.120ask.com/question/70657805.htm')
  # print data
