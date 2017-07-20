# coding: utf-8
from bs4 import BeautifulSoup

def bf(htm):
    htm2 = BeautifulSoup(htm, "html.parser")
    htm3 = str(htm2.find_all('li'))
    return htm3
