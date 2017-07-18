import download
import bf

def write_txt():
    htm = download.download('http://www.jcrb.com/')
    htm2 = bf.bf(htm)                     #bf
    fo = open("content.txt", "w")
    fo.write(htm)
    fo1 = open("scrape.txt", "w")
    fo1.write(htm2)
    fo1.close()
    fo.close()

