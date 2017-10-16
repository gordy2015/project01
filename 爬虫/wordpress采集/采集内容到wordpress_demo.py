#说明： 以下为python2.7 亲测可以用
#/usr/bin/env python
#_*_coding=utf8_*_
import httplib
import hashlib
import urllib
import random
import urllib2
import md5
import re
import json
import sys
import time
from lxml import html
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from newspaper import Article
reload(sys)
sys.setdefaultencoding('utf-8')
time1 = time.time()
#得到html的源码
def gethtml(url1):
    #伪装浏览器头部
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(
    url = url1,
    headers = headers
    )
    html = urllib2.urlopen(req).read()
    return html
#得到目标url源码
code1 = gethtml('http://whuhan2013.github.io/archive/')

tree = html.fromstring(code1)
#print tree

targeturl=tree.xpath("//li[@class='listing-item']/a/@href")

def sends():
    print len(targeturl)
    for i in range(len(targeturl)):
        #u=content1[i][0]
        url="http://whuhan2013.github.io"+targeturl[i]
        print url
        a=Article(url,language='zh')
        a.download()
        a.parse()
        title=a.title
        dst=a.text

        #链接WordPress，输入xmlrpc链接，后台账号密码
        wp = Client('http://127.0.0.1:22222/xmlrpc.php','www','!abc6')
        #示例：wp = Client('http://www.python-cn.com/xmlrpc.php','username','password')
        post = WordPressPost()
        post.title = title
        #post.post_type='test'
        #post.content = dst
        post.description = dst
        post.post_status = 'publish'
        #发送到WordPress
        wp.call(NewPost(post,True))
        time.sleep(3)
        print 'posts updates'

if __name__=='__main__':
    sends()
