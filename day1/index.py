

# import copy
# n1 = {"k1":"wu","k2":123,"k3":["alex",456]}
# n3 = copy.copy(n1)
#
# s = id(n1)
# print(s)
# p = id(n3)
# print(p)

# def func(arg1,arg2):
#     if arg1 == 0:
#         print(arg1,arg2)
#     arg3 = arg1 + arg2
#     print(arg3)
#     func(arg2,arg3)
# func(0,1)


# tp1 = "i am {}, age {}, {}".format("seven",18,"alex")
# print(tp1)
#
# tp1 = "i am {}, age {}, {}".format(*["seven",18,"alex"])
# print(tp2)

from test import Hello
h = Hello()
print(h.hello())
print(type(h))