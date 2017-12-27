# coding: utf-8

import download
import bf
import time
import test
import urllib
import itertools

page = 5350026
time_start = time.time()
for tag in range(5350024, page):
    print(tag)
    html = download.download('https://movie.douban.com/subject/%d/' % tag)
    if not html == False:
        bf.bs(html)
time = time.time() - time_start
print('程序耗时：%f' % time)





