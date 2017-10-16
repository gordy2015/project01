
class Dog(object):
    def __init__(self,name):
        self.name = name

    @property
    def eat(self):
        print("%s is eating..." % self.name)


def bulk(self):
    print('%s is yelling...' % self.name)

d = Dog('aa')
#print(d.eat)
#print(d.name)
choice = input(">>").strip()

if hasattr(d,choice):
    #getattr(d,choice)
    #print(choice)
    pass

else:
    setattr(d,choice,bulk)
    func = getattr(d,choice)
    func(d)


#----------------------------------------
# class Foo(object):
#     def __init__(self):
#         self.name = 'wu'
#     def func(self):
#         return 'func'
# obj = Foo()
#
# # q = hasattr(obj,'name')
# # t = hasattr(obj,'func')
# # print(q)
# # print(t)
#
# # n = getattr(obj,'name')
# # f = getattr(obj,'func')
# # print(n)
# # print(f)
# #
# print(obj.name)
# p = setattr(obj, 'name', 'waaa')
# print(obj.name)
# setattr(obj, 'show', lambda num: num + 1)
# #
# a = delattr(obj,'name')
# print(a)
# # delattr(obj,'func')