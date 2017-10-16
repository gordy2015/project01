#静态方法
# class Dog(object):
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def eat(self):
#         print("%s is eating" % self.name)
#
# d = Dog("alex")
# d.eat(d)

#类方法
# class Dog(object):
#     name = 'yui'
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def eat(self):
#         print("%s is eating" % self.name)
#
# d = Dog('eric')
# d.eat()

#属性方法
# class Dog(object):
#     def __init__(self,name):
#         self.name = name
#
#     @property
#     def eat(self):
#         print("is eating" % self.name)
#
# d = Dog("eric")
# d.eat

#修改属性 & 删除属性
# class Flight(object):
#     def __init__(self,name):
#         self.flight_name = name
#     def checking_status(self):
#         print("checking flight %s status" % self.flight_name)
#         return 1
#
#     @property
#     def flight_status(self):
#         status = self.checking_status()
#         if status == 0:
#             print("flight is went")
#         elif status == 1:
#             print("flight is arrived")
#         elif status == 2:
#             print("flight is canceled")
#         else:
#             print("cannot confirm the flight status...")
#
#     @flight_status.setter
#     def flight_status(self,status):
#         status_dic = {
#             0 : "went",
#             1 : "arrived",
#             2 : "canceled"
#         }
#         print("changed the flight status to ", status_dic.get(status))
#
#     @flight_status.deleter
#     def flight_status(self):
#         print("status got removed...")
#
# f = Flight('mh370')
#
# f.flight_status
#
# f.flight_status = 0
# del f.flight_status

#__doc__打印注释
# class Foo:
#     '''这是一个类信息'''
#     def func(self):
#         pass
# int(Foo.__doc__)


# from lib.aa import C
# obj = C()
# print(obj.__module__)
# print(obj.__class__)


##__call__   & __dict__
# class Foo:
#     def __init__(self,name):
#         self.name = name
#         print(self.name)
#     def __call__(self, *args, **kwargs):
#       print('__call__')
# obj oo('el')
# obj
# obj()   #调用__call__函数
#
# class Province:
#     country = 'China'
#     def __init__(self,name,count):
#         self.name = name
#         self.count = count
#     def func(self,*args,**kwargs):
#         print('func')
#
# print(Province.__dict__)
# a = Province('eric',200)
# print(a.__dict__)
# print(a.func('pa'))



# class Foo:
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return 'alex'
#
# obj = Foo('eric')
# print(obj)



# class Foo(object):
#     def __getitem__(self, item):
#         print('__getitem__', item)
#     def __setitem__(self, key, value):
#         print('__setitem__',key, value)
#     def __delitem__(self, key):
#         print('__delitem__',key)
#
# obj = Foo()
# result = obj['k1']   #自动触发执行__getitem__
# print(result)
# obj['k2'] = 'alex'   #自动触发执行__setitem__
# del obj['k1']

# class Foo(object):
#     def __init__(self,name):
#         self.name = name
#     def __call__(self, *args, **kwargs):
#         print('calhe')
#
# f = Foo('alex'rint(f())
# print(type(f))
# print(type(f()))
# print(type(Foo))


# def func(self):
#     print('hello alex')
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
# Foo = type('Foo',(object,),{'func':func,'__init__':__init__})
# f = Foo('jack',22)
# f.func()
# print(f.name)

#异常处理
# while True:
#     num1 = input('num1:')
#     num2 = input('num2:')
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         result = num1 + num2
#         print(result)
#     except Exception as e:
#         print('error', e)


# dic = ['ERIC','alex']
# try:
#     dic[10]
# except IndexError as e:
#     print(e)
#
# s1 = {'k1':'v1'}
# try:
#     s1['k20']
# except KeyError as e:
#     print(e)
#
# s2 = 'hello'
# try:
#     int(s2)

