# coding: utf-8
from bs4 import BeautifulSoup

def bs(html, file, tag):
    #用html.parser或者lxml解析html文档，lxml更好一点
    #soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html, 'lxml')
    #根据标签获取属性
    # print(soup.h1.attrs)
    # print(soup.a.attrs)
    # print(soup.p.string)
    # print(soup.a.string)
    # print(soup.find_all('h1'))
    #tObj的类型是：<class 'bs4.element.ResultSet'>，是不是封装的什么我也不知道
    tObj = soup.find_all('h1')
    # print(type(tObj))
    # if tObj.__len__() > 0:
    print("ID:%d" % tag, tObj.pop(0).contents[1].get_text(), file=file)
    # for tag in tObj:
    #     div_tag = tag.contents[1].get_text()
    #     print(div_tag)

    # #爬电影名字
    # bsObj = soup.find_all('div', {'class': 'pl2'})
    # for tag in bsObj:
    #     div_tag = tag.contents[1].get_text()
    #     name = div_tag.strip('\n').replace(' ', '') + '\n'
    #     print(name)
    # #格式化解析之后的html
    # soupprettify = soup.prettify()
    #  return soupprettify

