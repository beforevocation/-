# coding: utf-8
from bs4 import BeautifulSoup

def bs(html):
    #用html.parser或者lxml解析html文档，lxml更好一点
    #soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html, 'lxml')
    #根据标签获取属性
    print(soup.p.attrs)
    print(soup.a.attrs)
    print(soup.p.string)
    print(soup.a.string)
    #爬电影名字
    bsObj = soup.find_all('div', {'class': 'pl2'})
    for tag in bsObj:
        div_tag = tag.contents[1].get_text()
        name = div_tag.strip('\n').replace(' ', '') + '\n'
        print(name)
    #格式化解析之后的html
    soupprettify = soup.prettify()
    return soupprettify

