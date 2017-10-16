import urllib.request
import re

def load_webpage(url):
    #url = 'http://www.ruigaokeji.cn'
    user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;)'
    headers = {'User-Agent':user_agent}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def write_to_file(filename,txt):
    file = open(filename,'w+',encoding='UTF-8')
    file.write(txt)
    file.close()

def spider_web(url,begin_page,end_page):
   for i in range(begin_page,end_page + 1):
        pn = 50 * ( i - 1 )
        #print(pn)
        html = load_webpage(url+str(pn))
        dhtml = html.decode('UTF-8')
        # filename = str(i) + '.html'
        # write_to_file(filename,dhtml)
   html = load_webpage(url)
   dhtml = html.decode('UTF-8')
   # filename = 'test.txt'
   # write_to_file(filename,dhtml)
   #print(dhtml)
   deal_page(dhtml)



def deal_page(html):
    '''
    < div class ="threadlist_title pull_left j_th_tit " > < a class ="j_th_tit " href=".*?" title=".*?" target="_blank" >.* ? < / a >   <a href=.*?>.*?   
    #<div class="threadlist_title pull_left j_th_tit ">.*?</a></div>
    '''
    # s = re.compile(r'<div class="threadlist_title pull_left j_th_tit .*?">(.*?)</div>',re.S)
    # print(s)
    # print(type(q))
    # m = re.compile(r'class="j_th_tit ">(.*?)</a>')  #加上上面一条正则，即两条正则表达式进行筛选
    # n = m.findall(str(q))
    # print(q)

    s = re.compile(r'<div class="threadlist_title pull_left j_th_tit .*? title="(.*?)" target="_blank" class="j_th_tit ">',re.S)  #一条正则表达式进行筛选
    q = s.findall(html)
    for a in q:
        print(a)

#load_webpage('https://tieba.baidu.com/f?kw=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&ie=utf-8&pn=50') #王者荣耀贴吧地址

if __name__ == '__main__':
    spider_url = input('pls input the spider url:')
    begin_page = int(input('begin_page:'))
    end_page = int(input('end_page:'))
    spider_web(spider_url,begin_page,end_page)

