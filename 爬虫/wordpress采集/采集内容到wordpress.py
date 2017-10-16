
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

# reload(sys)
# sys.setdefaultencoding('utf-8')
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

#得到目标url源码
def geturls():
    code1 = gethtml('http://zhinengsuobaike.com/topic/wiki/page/2/')

    tree = html.fromstring(code1)
    #print(tree)
    # print(type(tree))
    # print(str(code1))

    #targeturl=tree.xpath("//li[@class='ling-item']/a/@href")
    targeturl=tree.xpath("//h2[@class='entry-title']/a/@href")
    #
    print(targeturl)
    #sends(targeturl)
    re_anly(targeturl)

#使用newspaper库提取标题和文本内容（文本无图片）
# def sends(targeturl):
#     print(len(targeturl))
#     for i in range(len(targeturl)):
#         url= targeturl[i]
#         print(url)
#         a=Article(url,language='zh')
#         a.download()
#         a.parse()
#         title=a.title
#         dst=a.text
#         print('%s title: %s' % (i,title))
#         print('%s content: %s' %(i,type(dst)))
#         sent_to_wp(title,dst)


#把图片存在本地
def write_fo_file(filename,txt):
    file = open(filename,'wb')
    file.write(txt)
    file.close()

def re_anly(targeturl):
    for i in range(1,2):
        url= targeturl[i]
        code2 = gethtml(url)
        print('code2: %s %s' % (code2,type(code2)))

        #以下是使用newspaper库进行提取标题和内容
        # a=Article(url,language='zh')
        # a.download()
        # a.parse()
        # title=a.title
        # print('title: %s' % title)
        #dst = a.text
        # print(dst)
        #print(code2.decode('utf-8'))
        #tree = html.fromstring(code2)
        # tree = etree.HTML(code2)
        # content = tree.xpath("//*[@id='post-3160']/div/div[1]/p")
        #print(content)

        #利用正则获取文章的标题
        d = re.compile(r'<h1 class="entry-title">(.*?)</h1>')
        w = d.findall(code2.decode('utf-8'))
        title = w[0]
        print('title: %s %s' %(title,type(title)))
        #利用正则获取文章的内容（含内容中的图片链接）
        c = re.compile(r'<div class="entry-content">(.*?)<div class="clear">',re.S)
        q = c.findall(code2.decode('utf-8'))
        print(type(q[0]),type(q[:]))
        #source_content = str(q)
        source_content = q[0]
        content = source_content.replace("\r","").replace("\t","").replace("\n","")
        #print('content: %s' %content)
        p = re.compile(r'src="(.*?)"',re.S)
        s = p.findall(content)
        #print(len(s))


        if s:
            # 以下for原本是打算把内容里的所有图片下载下来保存在本地。但后来发现目标网站并防无盗链，所以只下载第一张图上传到wp，做为文章的特征图
            # for jpg_link in range(len(s)):
            # # set to the path to your file
            # print(jpg_link)
            # m = s[jpg_link]
            m = s[0]
            #print('jpg_link: %s m: %s' %(jpg_link,m))
            filename = m.split('/')[3]
            #print(filename)
            if '.jpg' in filename or '.JPG' in filename or '.png' in filename or '.PNG' in filename:
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
            filename = 'default.jpg'
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
    wp = Client('http://www.abc.com/xmlrpc.php', 'www', 'abc16')
    # sent_to_wp(title,content)
    with open(fullname, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())
    response = wp.call(media.UploadFile(data))
    print('response: %s' % response)
    attachment_id = response['id']
    print('attachment_id: %s %s' %(type(attachment_id),attachment_id))

    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = 'publish'
    post.thumbnail = attachment_id
    post.id = wp.call(posts.NewPost(post))
    print('title:%s  =>post success' % title)
    print('-----------------------------------------------------------------------------------------------')


# #-------------------------------------
# 以下是不上传特征图的操作， 链接WordPress，输入xmlrpc链接，后台账号密码
# def sent_to_wp(title,content):
#     wp = Client('http://192.168.2.11:22222/xmlrpc.php','www','abc16')
#     if wp:
#         print('ok')
#         #示例：wp = Client('http://www.python-cn.com/xmlrpc.php','username','password')
#         post = WordPressPost()
#         post.title = title
#         #post.description = content  #有的wordpress_xmlrpc 上传内容是用post.description. 有的是post.content
#         post.content = content
#         post.post_status = 'publish'
#         # print(post.title)
#         #发送到WordPress
#         wp.call(NewPost(post))
#         time.sleep(3)
#         print('posts updates')
#     else:
#         print('false')
# #


if __name__=='__main__':
    geturls()







