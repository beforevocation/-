# coding: utf-8

import download
import bf

html = download.download('https://movie.douban.com/chart')
# print(html)
bf.bs(html)




