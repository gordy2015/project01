#_*_coding:utf-8_*_


import time


# print(time.altzone)
# print(time.asctime())   #返回时间格式"Mon Mar 27 11:16:30 2017"
# print(time.localtime()) #返回本地时间的 struct time对象格式
#print(time.gmtime(time.time()-86400*3))  #返回utc时间的struc时间对象格式
#
# print(time.asctime(time.gmtime()))   #返回格式 Mon Mar 27 11:16:30 2017
#
# print(time.ctime())  #返回格式 Mon Mar 27 11:16:30 2017
#
# print(time.ctime(time.time()-86400))
# print(time.gmtime(time.time()-86400))
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#
# stra = time.strptime("2017/03/27 11:50:05", "%Y/%m/%d %H:%M:%S")
# print(stra)
# print(time.mktime(stra))
#
# s = time.localtime()
#
# print(time.mktime(s))
#
# print(time.gmtime(time.time()))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
#
# import datetime
#
# print(datetime.datetime.now())
# print(datetime.date.fromtimestamp(time.time()))


#json
# import json
# s1 = '{"k1":123}'
# dic = json.loads(s1)
# print(s1,type(dic))
#
# s2 = '["alex","eric",234]'
# stt = json.loads(s2)
# print(stt,type(stt))
#
# s3 = {"k3":"mp3"}
# sta = json.dumps(s3)
# print(sta,type(sta))
#
# s4 = ['meal','milk','hotdog']
# dia = json.dumps(s4)
# print(dia,type(dia))
#
# import pickle
# data = {'k4':999,'k5':555}
# p = pickle.dumps(data)
# print(p,type(p))
#
# # li = '[11,22,43]'
# # json.dump(li,open('db','a+'))
#
# li = json.load(open('db','r'))
# print(li,type(li))

#-------------------------------------------------------
# #LOGGING日志模块
# import logging
# #
# # logging.basicConfig(filename='test.log',level=logging.WARNING,format='%(asctime)s %(levelname)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
#
# #定义logger
# LOG = logging.getLogger("TTT")
# LOG.setLevel(logging.DEBUG)  #日志级别全局定义
#
# #定义一个用于屏幕输出/一个用于文件输出的handler
# ci = logging.StreamHandler()
# ci.setLevel(logging.INFO)
#
# fi = logging.FileHandler('tg.log')
# fi.setLevel(logging.INFO)
#
# #定义日志格式
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#
# #定义handler使用什么格式
# ci.setFormatter(formatter)
# fi.setFormatter(formatter)
#
# #添加ci和fi到logger
# LOG.addHandler(ci)
# LOG.addHandler(fi)
#
# #测试log数据
# LOG.debug('user [qin] login out')
# LOG.info('[qin] del a file a.txt')
# LOG.critical('find a work')

#------------------------------------------------------------

# import md5
# hash = md5.new()
# hash.update('admin')
# print(hash.hexdigest())
#
# import sha
# hash = sha.new()
# hash.update('admin')
# print(hash.hexdigest())
#
# import hashlib
# hash = hashlib.md5()
# hash.update('root')
# print(hash.hexdigest())
#
# hash2 = hashlib.sha1()
# hash2.update('admin')
# print(hash2.hexdigest())
#
# hash3 = hashlib.sha256()
# hash3.update('admin')
# print(hash3.hexdigest())
#
# hash = hashlib.md5('898oaFs09f')
# hash.update('admin')
# print(hash.hexdigest())
#
# import hmac
# h = hmac.new('root')
# h.update('admin')
# print(h.hexdigest())

# import commands
# rs = commands.getoutput('cmd')
#
#
# import subprocess
# rs2 = subprocess.call(["ls","-l"],shell=False)
# rs3 = subprocess.check_output(["echo","hello world!"])



# import re
#
# a = '123abc456'
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).groups())
#
# obj2 = re.search('\d+','fa123uu989aas')
# obj = re.findall('\d+','fa123uu989aas')
# print(obj2.group())
# print(obj)
#
# new_a = re.sub('\d+','sb',a,1)
# print(new_a)
#
# content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4-3)/(16-3*2)）"
# new_con = re.split('\+',content,1)
# print(new_con)
#
# new_con2 = re.split('[\+\-\*\/]+',content)
# print(new_con2)
#
# pp = '1-2*((60-30 +(-40-5)*(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
# npp = re.sub('\s*','',pp)
# print(npp)
# new_con3 = re.split('\(([\+\-\*\/]?\d+[\+\-\*\/]?\d+){1}\)',npp,1)
# print(new_con3)

#-------------------------------
#
# import ConfigParser
# config = ConfigParser.ConfigParser()
# config['DEFAULT'] = {'ServerAliveInterval':'45',
#                       'Compression':'yes',
#                       'CompressionLevel':'9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini','w') as configfile:
#     config.write(configfile)

#------------------------------------------------------------
#
# import shelve
# d = shelve.open('shelvtest.txt')
# class Test(object):
#     def __init__(self,n):
#         self.n = n
#
# t = Test(123)
# t2 = Test(123334)
# name = ["alex","rain","test"]
# d["test"] = name
# d["t1"] = t
# d["t2"] = t2
# d.close()

#-----------------------------------------------

# def person(name,age,sex,job):
#     def walk(p):
#         print("person %s is walking..." % p['name'])
#
#     data = {
#         'name': name,
#         'age': age,
#         'sex': sex,
#         'job': job
#     }
#     return data
#
# def dog(name,dog_type):
#     def bark(d):
#         print("dog %s:wang.wang...wang.." % d['name'])
#     data = {
#         'name': name,
#         'type': dog_type
#     }
#     return data
#
#
#
#
# d1 = dog('阿京','京巴')
# p1 = person('小海',36,"F","运维")
# p2 = person("林峰",27,"F","Teacher")
# print(d1)
# print(p1)
# print(p2)


# from datetime import datetime
# format = "output-%Y-%m-%d-%H%M%S.txt"
# str    = "output-1997-12-23-030000.txt"
# t      = datetime.strptime(str, format)
# print (t)


# import socket
# HOST = ''
# PORT = 8000
# reply = 'Yes'
#
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((HOST,PORT))
# s.listen(3)
# conn, addr = s.accept()
# request = conn.recv(1024)
# print('request is:', request)
# print('Connected by:', addr)
# conn.sendall(reply)
# conn.close()

# import socket
# HOST = '192.168.2.11'
# PORT = 8000
#
# request = 'can you hear me'
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((HOST,PORT))
# s.sendall(request)
# reply = s.recv(1024)
# print('reply is:', reply)
# s.close()


# import socket
# HOST = ''
# PORT = 8000
# text_content = '''HTTP/1.X 200 OK
# Content-Type: text/html
#
# <head>
# <title>WOW</title>
# </head>
# <html>
# <p>Wow, Python Server</p>
# <IMG src="LK.png"/>
# </html>
# '''
#
# f = open('LK.png','rb')
# pic_content = '''
# HTTP/1.x 200 OK
# Content-Type: image/png
# '''
#
# pic_content = pic_content + f.read()
# f.close()
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST,PORT))
#
# while True:
#     s.listen(3)
#     conn, addr = s.accept()
#     request = conn.recv(1024)
#     method = request.split(' ')[0]
#     src = request.split(' ')[1]
#
#     if method == 'GET':
#         if src == 'LK.png':
#             content = pic_content
#         else:
#             content = text_content
#         print('Connected by', addr)
#         print('Request is:', request)
#         conn.sendall(content)
#     conn.close()

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# a = fact(5)
# print(a)


# d = {'a':1, 'b':2, 'c': 3}
# for key in d:
#     print(key)
#
# for ch in 'ABC':
#     print(ch)
#
# from collections import Iterable
# print(isinstance('abc', Iterable))
# isinstance([1,2,3],Iterable)
# isinstance(123,Iterable)
#
# for i, value in enumerate(['A','B','C']):
#     print(i, value)
#
# for x, y in [(1,1), (2,4), (3,9)]:
#     print(x, y)

#列表
# L = [x * x for x in range(10)]
# print(L)
#
# #生成器
# g = (x * x for x in range(10))
# print(g)
#
# # print(next(g))
# # print(next(g))
#
# def fib(max):
#     n, a, b  = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n = n + 1
#     return 'done'
#
# fib(5)


# std1 = {'name':'alex','score':98}
# std2 = {'name':'eric','score':81}
#
# # def print_score(std):
# #     print('%s: %s'  % (std['name'], std['score']))
# #
# # print_score(std2)
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
# bart = Student('Bart', 59)
# bart.print_score()
#
# print(bart)
# print(Student)
#
# bart.name = 'Tom'
# print(bart.name)
#

#----------------------------------------------------------------
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#     def get_grade(self):
#         if self.__score >= 90:
#             return 'A'
#         elif self.__score >= 60:
#             return 'B'
#         else:
#             return 'C'
#     def teacher(self):
#         if self.__name == 'peny':
#             return 'Miss Li'
#         else:
#             return 'Mr Wu'
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#
#     # def set_score(self,score):
#     #     self.__score = score
#     def set_score(self,score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
#     def set_name(self,name):
#         self.__name = name
# Y = Student('peny', 77)
# bart = Student('Bart Simpson', 98)
# # print(Y.name)
# # print(Y.score)
# print(Y.print_score())
# print(Y.get_grade())
# print(Y.teacher())
# print(Y.get_score())
# print(bart.get_name())
#
# a = Y.set_score(88)
# print(Y.get_score())
# print(Y._Student__name)
# print(Y.get_name())
#
# bart.__name = 'New Name'
# print(bart.__name)
# print(bart.get_name())
#
# b = bart.set_name('eric')
# print(bart.get_name())
#------------------------------------------------------

# class Animal(object):
#     def run(self):
#         print("Animal is running...")

# dog = Dog()
# print(dog.run())
# cat = Cat()
# print(cat.run())

# class Dog(Animal):
#     def run(self):
#         print("Dog is running...")
#     def eat(self):
#         print("Eating meat...")
# class Cat(Animal):
#     def run(self):
#         print("Cat is running...")
# dog = Dog()
# print(dog.run())
# print(dog.eat())

# cat = Cat()
# print(cat.run())

# a = list()
# b = Animal()
# c = Dog()

# print(isinstance(a,list))
# print(isinstance(b,Animal))
# print(isinstance(c,Animal))


# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# print(run_twice(Animal()))
#
# print(run_twice(Dog()))
# #
# print(run_twice(Cat()))

# class Tortoise(Animal):
#     def run(self):
#         print('Tortoise is running slowly...')

# run_twice(Tortoise())


# a = Animal()
# d = Dog()
#
# c = isinstance(a,Dog)
# # print(c)
#
# class MyDog(object):
#     def __len__(self):
#         return 100
# dd = MyDog()
# # print(len(dd))
#
# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#     def power(self):
#         return self.x * self.x
# obj = MyObject()
# g = hasattr(obj,'power')
# h = setattr(obj,'y',19)
# m = getattr(obj,'z',404)
#
# print(obj.x)
# print(g)
#
# print(m)
# print(obj.y)
#
# fn = getattr(obj, 'power')
# #三种写法都是power属性
# print(MyObject().power())
# print(fn())
# print(obj.power())
#
# sum = obj.x +obj.y
# print(sum)
#
# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None

# class Student(object):
#     def __init__(self,name):
#         self.name = name
# s = Student('Pee')
# s.score = 90
# print(s.score)
#
# class Student(object):
#     name = 'Student'
# s = Student()
# print(s.name)
# print(Student.name)
# s.name = 'Kaka'
# print(s.name)
# print(Student.name)
# del s.name
# print(s.name)


# s = Student()
# s.name = 'Harry'
# print(s.name)

# def set_age(self, age):
#     self.age = age
# from types import MethodType
# s.set_age = MethodType(set_age, s)
# s.set_age(25)
# # print(s.age)
#
# def set_score(self,score):
#     self.score = score
# Student.set_score = set_score
#
# s.set_score(100)
# # print(s.score)
#
# s2 = Student()
# s2.set_score(99)
# # print(s2.score)
#
# class Student(object):
#     __slots__ = ('name', 'age')
# t = Student()
# t.name = 'Ben'
# t.age = 25
# #t.score = 81
# print(t.name)
# print(t.age)
# # print(t.score)
#
# class Gstudent(Student):
#     pass
# g = Gstudent()
# g.name = 'ti'
# g.score = 89
# print(g.name)
# print(g.score)
#
# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self,value):
#         if not isinstance(value, int):
#             raise ValueError("score must be an interger")
#         if value < 0 or value > 100:
#             raise ValueError("score must between 0 ~ 100")
#         self._score = value
#
# u = Student()
# u.set_score(69)
# print(u.get_score())
#
#
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value, int):
#             raise ValueError("score must be an interger")
#         if value < 0 or value > 100:
#             raise ValueError("score must between 0 ~ 100")
#         self._score = value
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2015 - self._birth
#
#
# i = Student()
# i.score = 99
# print(i.score)
#
# i.birth('2011-11-22')
# print(i.birth)

#
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#     __repr__ = __str__
# print(Student('Michael'))
# s = Student('Michael')
#
#
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100000:
#             raise StopIteration()
#         return self.a
#
#
# # for n in Fib():
# #    print(n)
#
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a+b
#         return a
#     if isinstance(n, slice):
#         start = n.start
#         stop = n.stop
#         if start is None:
#             start = 0
#         a, b = 1, 1
#         L = []
#         for x in range(stop):
#             if x >= start:
#                 L.append(a)
#             a, b = b, a + b
#         return L
#
# f = Fib()
# print(f[0])
# print(f[1])
# print(f[2])
# print(f[51])
#
# print(list(range(100))[5:11])

# JAN = 1
# FEB = 2
# MAR = 3
#
# from enum import Enum, unique
# Month = Enum('Month',('Jan','Feb','Mar','Apr',',May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
#
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# day1 = Weekday.Mon
# print(day1)

# class Hello(object):
#     def hello(self,name='world'):
#         print('Hello, %s.' % name)
#
# def fn(self, name = 'world'):
#     print('Hello, %s.' % name)
# Hello = type('Hello',(object,), dict(hello=fn))
# h = Hello()
# print(h.hello())
# print(type(Hello))
# print(type(h))
#
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls,name,bases,attrs)
# class MyList(list, metaclass = ListMetaclass):
#     pass
# L = MyList()
# L.add(1)
# print(L)

# def foo():
#     r = -1
#     if r == (-1):
#         return (-1)
#     return r
# def bar():
#     r = foo()
#     if r == (-1):
#         print('Error')
#     else:
#         pass

# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     #print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')


# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar(0)
    # try:
    #     bar(0)
    # except Exception as e:
    #     print('Error:', e)
    # finally:
    #     print('finally...')
#
# main()

# import logging
# def foo(s):
#     return 10 / int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     try:
#         bar(0)
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

# class BooError(ValueError):
#     pass
# def boo(s):
#     n = int(s)
#     if n == 0:
#         raise  BooError('invalid value: %s' % s)
#     return 10 / n
# boo('0')

# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
# bar()
#
#
# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error')

#
# def foo(s):
#     n = int(s)
#     assert n != 0,  'n is zero!'
#     return 10 / n
# def main():
#     foo('0')
# main()

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)


# class Dict(dict):
#     def __init__(self, **kw):
#         super().__init__(**kw)
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"Dict' object has no attribute '%s'"  % key)
#     def __setattr__(self, key, value):
#         self[key] =value
# d = Dict(a=1,b='test')
# print(d)
# import unittest
# class TestDict(unittest.TestCase):
#     def test_init(self):
#         d = Dict(a=1,b='test')


#from io import StringIO
# f = StringIO()
# f.write('hello')

# #from io import StringIO
# import io
# f = stringIO('Hello\nHi\n')

# from io import BytesIO
# f = bytesIO()
# f.read()

d = dict(name='Bob', age=20, score=88)


# import pickle
# d = dict(name='Bob', age=20, score=88)
# s = pickle.dumps(d)
# print(s)
#
# # f = open('test.log','wb')
# # pickle.dump(d,f)
# # f.close()
#
# f = open('test.log','rb')
# s = pickle.load(f)
# f.close()
# print(s)

# import json
# d = dict(name='Bob', age=20, score=88)
# s = json.dumps(d)
# print(s,type(s),type(d))
#
# json_str = '{"age":20, "score":88, "name": "Bob"}'
# t = json.loads(json_str)
# print(t,type(t),type(json_str))
#
# f = open('test.log','wb')
# t = json.dump(d,f)
# print(t,type(t))

# import json
# class Student(object):
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# s = Student('Pi',23,90)
#
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
#
# def dict2student(d):
#     return Student(d['name'],d['age'],d['score'])
# # print(json.dumps(s,default=student2dict))
#
# print(json.dumps(s,default=lambda obj:obj.__dict__))
# m = '{"name":"Ben", "age":39, "score":54}'
# print(json.loads(m,object_hook=dict2student))


# import os
# print('Process (%s) start...'  % os.getpid())
#
# pid = os.fork()
# print(pid)
# if pid ==0:
#     print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s)' % (os.getpid(), pid))


#------------------------------

# class std(object):
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#
#     def std_score(self):
#         print('%s score is %s'  % (self.name, self.score))
#
# d = std('li',23,88)
# print(d.std_score())


# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Cat(Animal):
#     def talk(self):
#         print('%s miaomiao' %self.name)
# class Dog(Animal):
#     def talk(self):
#         print('%s wangwang' %self.name)
#
#
# c = Cat('qin')
# d = Dog('li')
# # c.talk()
# # d.talk()
#
# def fun(a):   #一种接口， 多种形态
#     a.talk()
# fun(c)
# fun(d)
#------------------------------


class SchoolMember(object):
    members = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def enroll(self):
        '''注册'''
        SchoolMember.members += 1
        print("new member [%s] is enrolled, now there are [%s] members" % (self.name, SchoolMember.members))
    def __del__(self):
        '''析构方法'''
        print("member [%s] is added" %self.name)

class Teacher(SchoolMember):
    def __init__(self,name,age,course,salary):
        super(Teacher,self).__init__(name,age)
        self.course = course
        self.salary = salary
        self.enroll()

    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher''' %(self.name, 'oldboy', self.course)
        print(msg)

class Student(SchoolMember):
    def __init__(self,name,age,grade,sid):
        super(Student,self).__init__(name,age)
        self.grade = grade
        self.sid = sid
        self.enroll()
    def tell(self):
        pass

# p = SchoolMember('li',23)
# p.enroll()
#
# q = SchoolMember('qin', 37)
# q.enroll()

if __name__ == '__main__':
    t1 = Teacher('op',23,'pe',8000)
    t1.teaching()
    t1.tell()
    s1 = Student("Qin",24,"python s12",1483)
