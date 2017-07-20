# coding: utf-8
import download
import bf

def write_txt():
    htm = download.download('http://www.jcrb.com/')
    htm2 = bf.bf(htm)
    fo = open("content.txt", "w")
    fo1 = open("scrape.txt", "w")
    fo.write(htm)
    fo1.write(htm2)
    fo.close()
    fo1.close()


