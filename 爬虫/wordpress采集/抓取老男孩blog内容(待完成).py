

import re,urllib.request

def web_spider(url):
    global dhtml
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    dhtml = html.decode('GBK')

    #print(dhtml)
    #write_fo_file('oldboyblog.txt',dhtml)
    #print('write to file success')
    return dhtml



def write_fo_file(filename,txt):
    file = open(filename,'w+',encoding='GBK')
    file.write(txt)
    file.close()

def spider_side(html):
    some = re.compile(r'<h3 class="artTitle"><a href="(.*?)">.*?</a>')
    get = some.findall(html)
    print(len(get))
    for i in get:
        print(i)
        q = web_spider('http://oldboy.blog.51cto.com' + i)
        # write_fo_file(i[9:]+'.html',q)
        # print('%s write to file success' % ('oldboy51ctoblog'+i[9:]+'.html'))
        #print(q)
        msome = re.compile(r'<!--正文 begin-->.*?<div class="showContent">(.*?)</div>.*?<!--正文 end-->',re.S)
        mget = msome.findall(q)
        #print(mget)
        #nw = str(mget).encode('GBK').decode('UTF-8')
        write_fo_file(i[9:] + '.html', str(mget))
        print('%s write to file success' % ('oldboy51ctoblog'+i[9:]+'.html'))

web_spider('http://oldboy.blog.51cto.com/2561410/d-8')
spider_side(dhtml)