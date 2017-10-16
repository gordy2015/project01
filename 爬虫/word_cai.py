import re,urllib.request
def web_spider(url):
    global dhtml
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    print(html)
    dhtml = str(html)

    #print(dhtml)
    #write_fo_file('oldboyblog.txt',dhtml)
    #print('write to file success')
    return dhtml
    print(dhmtl)

web_spider('http://roll.tech.sina.com.cn/internet_worldlist/index.shtml')