

# import urllib.request
#
# hhh = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0",
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Host":"aljun.me"
# }
#
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read())


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
fab(3)

# def fab1(max):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max:
#         L.append(b)
#         a, b = b, a + b
#         n = n + 1
#     return L
#
# for s in fab1(5):
#     print(s)

# class fab2(object):
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#     def __iter__(self):
#         return self
#     def next(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
# for t in fab2(2):
#     print(t)

def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        #print(b)
        a, b = b, a + b
        n = n +1
# for q in fab3(1):
#     print(q)

f = fab3(5)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())


from inspect import isgeneratorfunction
print(isgeneratorfunction(fab))
