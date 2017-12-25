import urllib.request

def download(url, num_retries=5, user_agent = 'ljw'):
    print('Downloading:', url)
    try:
        #设置代理，注意是花括号
        headers = {'User-agent':user_agent}
        request = urllib.request.Request(url, headers=headers)
        #打开链接，并读取网页
        html = urllib.request.urlopen(request).read()
        #捕获可能抛出的URLError异常
    except urllib.URLError as e:
        print('Download error:', e.reason)
        html = None
        #设置尝试的次数
        if num_retries > 0:
            #错误码(e.code)在某个范围之内，即确定错误:4xx错误发生在请求存在问题;5xx 错误则发生在服务端存在问题
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html
