
#说明： 以下为python2.7 亲测可以用
#/usr/bin/env python
#_*_coding=utf8_*_
#import httplib
import hashlib
import urllib
import random
import urllib.request
#import md5
import re
import json
import sys
import time
from lxml import html,etree
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media,posts
from wordpress_xmlrpc.methods.posts import NewPost
from newspaper import Article

time1 = time.time()


#得到html的源码
def gethtml(url1):
    #伪装浏览器头部
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib.request.Request(
    url = url1,
    headers = headers
    )
    html = urllib.request.urlopen(req).read()
    return html

#得到目标url
def geturls(url):
    code1 = gethtml(url)
    tree = html.fromstring(code1)
    targeturl=tree.xpath("//div[@class='zx-tl']/a/@href")
    print(targeturl)
    re_anly(targeturl)

#把图片存在本地
def write_fo_file(filename,txt):
    file = open(filename,'wb')
    file.write(txt)
    file.close()

def re_anly(targeturl):
    for i in range(0,1):
        url= targeturl[i]
        code2 = gethtml(url)
        #print('code2: %s %s' % (code2,type(code2)))

        #利用正则获取文章的标题
        d = re.compile(r'<h1>(.*?)</h1>',re.S)
        w = d.findall(code2.decode('GBK'))
        #print('CODE2: %s' %code2.decode('GBK'))
        title = w[0]
        print('title: %s %s' %(title,type(title)))
        #利用正则获取文章的内容（含内容中的图片链接）
        c = re.compile(r'<div class="simple">(.*)</p>.*<!-- 导入文章内容导航 -->',re.S)
        q = c.findall(code2.decode('GBK'))
        print(type(q),q)

        source_content = str(q)
        source_content = q[0]
        #content为处理后的正文，字符串类型
        content = source_content.replace("\r","").replace("\t","").replace("\n","")
        #print('content: %s' %content)
        p = re.compile(r'img src="(.*?)"',re.S)
        s = p.findall(content)
        #print('length of s: %s' %len(s))
        if s:
            # 以下for原本是打算把内容里的所有图片下载下来保存在本地。但后来发现目标网站并防无盗链，所以只下载第一张图上传到wp，做为文章的特征图
            for n in range(0,1):
                m = s[n]
                print('s[n]: %s' % m)

                filename = m.split('/')[-1]
                #print(filename)
                if '.jpg' in filename or '.JPG' in filename or '.png' in filename or '.PNG' in filename or 'gif' in filename:
                    pass
                else:
                    filename = filename + '.jpg'
                fullname = 'images/' + filename
                print('jpg_link: %s <----> m: %s <----> fullname: %s' %(s[0],m,fullname))
                jpg_content = gethtml(m)
                # print(type(jpg_content), jpg_content)
                write_fo_file(fullname,bytes(jpg_content))
                print('%s saved in local' % fullname)
                print('-----------------------------------------------------------------------------------------------')
        else:
            print('link of the jpg: %s <----> lenght is %s  <----> no jpg should be saved'  %(s,len(s)))
            filename = 'default5.png'
            fullname = 'images/' + filename
        sent_to_wp(filename,fullname,title,content)


def sent_to_wp(filename,fullname,title,content):
    #prepare metadata
    data = {
            'name': filename,
            'type': 'image/jpeg',  # mimetype
    }
    #
    # # read the binary file and let the XMLRPC library encode it into base64
    wp = Client('http://www.abc.cn/xmlrpc.php', 'www', 'abc16')
    # sent_to_wp(title,content)
    with open(fullname, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())
    response = wp.call(media.UploadFile(data))
    #print('response: %s' % response)
    attachment_id = response['id']
    #print('attachment_id: %s %s' %(type(attachment_id),attachment_id))

    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = 'publish'
    post.thumbnail = attachment_id
    post.id = wp.call(posts.NewPost(post))
    print('title:%s  =>post success' % title)
    print('-----------------------------------------------------------------------------------')


if __name__=='__main__':
    #http://www.ofweek.com/newquery.action?type=1&subtype=25000&keywords=NB-IoT&sumPagenum=466
    #http://www.ofweek.com/newquery.action?keywords=NB-IoT&type=0
    geturls('http://www.ofweek.com/newquery.action?type=1&subtype=0&keywords=%E7%89%A9%E8%81%94%E7%BD%91&Sequence=1&sumPagenum=72786')

    # for i in range(2,6):
    #     durl = 'http://www.ofweek.com/newquery.action?type=1&subtype=0&keywords=%E5%85%85%E7%94%B5%E6%A1%A9&sumPagenum=13545&pagenum=' + str(i) + '&Sequence=0'
    #     geturls(durl)
    #     time.sleep(1)
    #     print('-----------------------this page %s is post success-----------------------' %i)







