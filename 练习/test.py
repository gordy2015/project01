# # class Class_basis:
# #     def ret(self):
# #         print("ret")
# #
# # obj = Class_basis()
# # obj.ret()
# #
# # class Foo:
# #     def __init__(self, name):
# #         self.Name = name
# #     def user(self):
# #         print(self.Name)
# # obj = Foo("Yangwen")
# # obj.user()
#
# # class Foo:
# #     def __init__(self, name, age):
# #         self.Name = name
# #         self.Age = age
# #     def info(self):
# #         print("""
# #     My name is %s
# #     My age is %d
# #         """ % (self.Name, self.Age))
# # ansheng = Foo("Yangwen", 18)
# # ansheng.info()
# #
# # xiaoming = Foo("xiaoming", 30)
# # xiaoming.info()
#
# # class People:
# #     def __init__(self):
# #         print("""
# #         你的通用特征有：四肢、头发、眼、耳朵
# #         """)
# # class China(People):
# #     def info(self):
# #         print("""
# #         你是中国人，你的语言是中文，皮肤是黄色
# #         """)
# # class US(People):
# #     def info(self):
# #         print("""
# #         你是美国人，你的语言是英文，皮肤是黑色
# #         """)
# #
# # c = China()
# # c.info()
# # print("""
# #         ------------------------------------------
# # """)
# # u = US()
# # u.info()
#
# # class China:
# #     def info(self):
# #         print("你是中国人")
# # class US:
# #     def info(self):
# #         print("你是美国人")
# # class My(China,US):
# #     def info(self):
# #        print("我就是我")
# # c = My()
# # c.info()
#
# # class Foo:
# #     classmembers = "公有的"
# #     __classmembers = "私有的"
# #     def members(self):
# #         print(Foo.__classmembers)
# # print(Foo.classmembers)
# # obj=Foo()
# # obj.members()
#
# # size = 2
# # if size < 0:
# #     raise ValueError('num to litile')
# # try:
# #     import test2
# #
# #     print(test2.__name__)
# # except ImportError:
# #     chardet = None
#
# # if chardet:
# #     print(1)
# # else:
# #     print(2)
#
#
# # phone_number = '1386-666-0066'
# # print(phone_number[1:9])
# # hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
# # print(hiding_number)
#
# # def g(num):
# #     print(str(num/1000) + 'kg')
# # g(0.2)
#
#
# # import cmath
# # a = 3
# # b = 4
# # c = cmath.sqrt( a ** 2 + b ** 2)
# # d = ( a ** 2 + b ** 2) ** 0.5
# # print('c is %s ' % c)
# # print(str(c)[2])
# # print(d)
# # print('The right triangle third side\'s length is %s ' % c)
# #
# # print('   *','  * *',' * * *','   |  ',sep = '\n')
# #
# # def trapezoid_area(base_up=1, base_down=2, height=3):
# #     return 1/2 * (base_up + base_down) * height
# # print(trapezoid_area(3,4))
#
#
#
# #
# # file = open('D://BaiduNetdiskDownload/text.txt','w+')
# # file.write('Hello World')
# # #file.close
# # file = open('D://BaiduNetdiskDownload/text.txt','r')
# # for i in file.readline():
# #     print(i)
#
#
# def text_create(name,msg):
#     desktop_path = 'D://BaiduNetdiskDownload/'
#     full_path = desktop_path + name
#     file = open(full_path,'w')
#     file.write(msg)
#     file.close()
#     print('Done')
# # name = 'mshi'
# # msg = 'who are you'
# # text_create(name,msg)
# #
# # file = open('D://BaiduNetdiskDownload/%s' %name,'r')
# # for i in file.readline():
# #     print(i)
#
#
# # def text_create2(word,cencored_word='lame',changed_word='Awesome'):
# #     return word.replace(cencored_word,changed_word)
# # # a = text_create2('Python is lame')
# # # print(a)
# #
# #
# # def text_censored_create(name,msg,cencored_word='lame',changed_word='Awesome'):
# #     desktop_path = 'D://BaiduNetdiskDownload/'
# #     full_path = desktop_path + name
# #     file = open(full_path,'w')
# #     msg = msg.replace(cencored_word,changed_word)
# #     file.write(msg)
# #     file.close()
# #
# # text_censored_create('ttaa','too lame for you')
# #
# # def text_censored_create2(name,msg):
# #     clean_msg = text_create2(msg)
# #     text_create(name,clean_msg)
# #
# # text_censored_create2('Try.txt','lame,a ,man')
#
#
# # def rdster():
# #     name = input('pls input your name:')
# #     passwd = input('pls input your password:')
# #     file = open('passwd.txt','a+')
# #     t = name + ',' + passwd + '\n'
# #     file.write(t)
# # #rdster()
# #
# # passwd_list = ['***','123']
# # def login():
# #     tries = 3
# #     #name = input('pls input your name:')
# #     while tries > 0:
# #         passwd = input('pls input your password:')
# #         passwd_correct = passwd == passwd_list[-1]
# #         passwd_reset = passwd == passwd_list[0]
# #
# #         if passwd_correct:
# #             print('login success')
# #         elif passwd_reset:
# #             new_p = input('pls input a new password:')
# #             passwd_list.append(new_passwd)
# #             print('password has changed successfully')
# #             print(passwd_list)
# #             login()
# #
# #         else:
# #             print('wrong password')
# #             tries = tries - 1
# #             print(tries,'time left')
# #     else:
# #         print('your account has been suspended')
# # login()
#
#
#
# #------------------
# #猜大小————版本1
# import random
# def num():
#     # global t
#     # global q
#     p1 = random.randrange(1,7)
#     p2 = random.randrange(1,7)
#     p3 = random.randrange(1,7)
#     # print(p1,p2,p3)
#     # s = p1 + p2 +p3
#     q = []
#     q.append(p1)
#     q.append(p2)
#     q.append(p3)
#     return q
#     s = sum(q)
#     # print(s)
#     if 11 <= s <= 18:
#         t = 'BIG'
#     else:
#         t = 'SMALL'
#     return t
# num()
#
#
# def cai():
#     while True:
#         print('<<<START THE GAME>>>')
#         g = input('PLS INPUT \'BIG\' OR \'SMAL\': \n>>>')
#         # num()
#         if g == t:
#             print('%s %s, YOU WIN' %(q,t))
#         else:
#             print('%s %s, YOU FAILE' %(q,t))
#
# if __name__ == '__main__':
#     cai()
#
# #------------------
# #猜大小----版本2
# def roll():
#     print('<<<START THE GAME>>>')



#/usr/bin/env python
# -*- coding: gbk -*-
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
from wordpress_xmlrpc.methods.posts import NewPost
from newspaper import Article

# wp = Client('http://192.168.2.11:22222/xmlrpc.php', 'www', '!@#www2016')
# if wp:
#     print('ok')
#     # 示例：wp = Client('http://www.python-cn.com/xmlrpc.php','username','password')
#     post = WordPressPost()
#     post.title = 'hi'
#     post.description = 'AAAAA'
#     post.post_status = 'publish'
#     # print(post.title)
#     # print(post.definition)
#     # 发送到WordPress
#     wp.call(NewPost(post,True))
#     time.sleep(3)
#     print('posts updates')
# else:
#     print('false')


from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import re,urllib.request

def web_spider(url):
    global dhtml
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()


    #
    write_fo_file('oldboyblog.jpg',html)
    print('write to file success')
    #



def write_fo_file(filename,txt):
    file = open(filename,'wb')
    file.write(txt)
    file.close()

web_spider('http://img.zhinengsuobaike.com/20170720307.jpg/mw640_webp')

#----------以下测试成功
# client = Client('http://192.168.2.11:22222/xmlrpc.php', 'www', '!@#www2016')
#
# # set to the path to your file
# filename = '222.png'
#
# # prepare metadata
# data = {
#         'name': '222.png',
#         'type': 'image/jpeg',  # mimetype
# }
#
# # read the binary file and let the XMLRPC library encode it into base64
# with open(filename, 'rb') as img:
#         data['bits'] = xmlrpc_client.Binary(img.read())
#
# response = client.call(media.UploadFile(data))
# # response == {
# #       'id': 6,
# #       'file': 'picture.jpg'
# #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
# #       'type': 'image/jpeg',
# # }
# attachment_id = response['id']
#
# post = WordPressPost()
# post.title = 'Picture of the Day'
# post.content = 'What a lovely picture today!'
# post.post_status = 'publish'
# post.thumbnail = attachment_id
# post.id = client.call(posts.NewPost(post))