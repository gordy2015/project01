
# import urllib.request
# import re
# import time
#
# url =  'http://blog.51cto.com/zt/703'
#
# request = urllib.request.urlopen(url)
# response = request.read()
#
# print(response)
#
# first = response.find(r'<img src=')
# # print(first)
# f = response.find(r'href=',first)
# # print(href)
# html = response.find(r'.png',first)
# # print(html)
# link = data[first+10:html+4]
# print(link)




#------------------------



import urllib
import urllib.request

full_url = 'http://cuiqingcai.com/1052.html'
request = urllib.request.urlopen(full_url)
response = request.read()
data = response.decode('UTF-8')
#print(data)

first = data.find(r'爬虫入门')
# print(first)
href = data.find(r'href=',first)
# print(href)
html = data.find(r'.html',href)
# print(html)
link = data[href+6:html+5]
# print(link)
# q = data[first:href]
# print(q)
setw = []
setw.append(link)
for i in range(25):
    first = data.find(r'title=', html)
    #print(first)
    href = data.find(r'href=', first)
    html = data.find(r'.html',href)
    # print(html)
    link = data[href+6:html+5]
    # print(link)
    setw.append(link)
    # print(setw)
    # q = data[first+7:href-2]
    # print(q)
#
for w in setw:
     print(w)
#      rurl = 'http://cuiqingcai.com/'
#      request = urllib.request.urlopen(w)
#      response = request.read()
# #     # # data = response.decode('UTF-8')
# #      print(response)
#      q = w[+len(rurl):]
#      # print(q)
#      f = open( 'D:\BaiduNetdiskDownload\webpa\%s' % q,'wb+')
#      print('downloading %s' %q)
#      f.write(response)
#      print('%s download end' %q)
#      f.close()



