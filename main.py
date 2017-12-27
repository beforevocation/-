# coding: utf-8

import download
import bf
import time
import test
import urllib
import itertools

page = 1000
time_start = time.time()
f = open("movie.txt", "w")
for tag in range(0, 1000):
    print(tag)
    html = download.download('https://movie.douban.com/subject/%d/' % tag, tag, f)
    if not html == False:
        bf.bs(html, f, tag)
time = time.time() - time_start
print('程序耗时：%f' % time)
f.close()





