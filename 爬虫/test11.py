# import urllib.request
#
# url = "http://www.xxx.com"
# # data = urllib.request.urlopen(url).read()
# # data = data.decode("UTF-8")
# # print(data)
#
# a = urllib.request.urlopen(url)
# print(a.getcode())

# import urllib
# import urllib.request
#
# data = {}
# data['word'] = 'nba'
# url_values = urllib.parse.urlencode(data)
# url = "http://www.baidu.com/s?"
# full_url = url + url_values
# data = urllib.request.urlopen(full_url).read()
# data = data.decode('UTF-8')
# print(data)

# import urllib
# import urllib.request
# import re
# data = {}
# data['keyword']='apple'
# url_values = urllib.parse.urlencode(data)
# # print(url_values)
# url = 'http://search.jd.com/Search?'
# full_url = url + url_values
# # print(full_url)
# data = urllib.request.urlopen(full_url).read()
# data = data.decode('UTF-8')
# #print(data)
# f = open('test11.txt','w',encoding='utf-8')
# f.write(data)
# f.close()
# src = 'titl="(.*?)"'
# s = re.findall(src,data)
# for m in s:
#     print(m)
# print('ok')


# import re
# import urllib
# import urllib.request
#
# from collections import deque
# queue = deque()
# visited = set()
#
# url = 'http://news.dbanotes.net'
# #url = 'http://www.xxx.com'
# queue.append(url)
# cnt = 0
# while queue:
#     url = queue.popleft()
#     visited |= {url}
#     print('已经抓取：' + str(cnt) + ' 正在抓取<--- ' + url)
#     cnt += 1
#     urlop = urllib.request.urlopen(url,timeout=2)
#     if 'html' not in urlop.getheader('Content-Type'):
#         continue
#     try:
#         data = urlop.read().decode('utf-8')
#     except:
#         continue
#     linkre = re.compile('href="(.+?)"')
#     for x in linkre.findall(data):
#         if 'http' in x and x not in visited:
#             queue.append(x)
#             print('加入队列 --->' + x)


#-------------------
import urllib.request
import http.cookiejar
# url = 'http://www.baidu.com/'
# req = urllib.request.Request(url, headers= {
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#     'User-Agent': 'ie/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
# })
# oper = urllib.request.urlopen(req)
# data = oper.read()
# # print(data.decode())
# print(oper.info())

# #-------------------
# def makeMyOpener(head = {
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#     'User-Agent': 'IE/11.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
# }):
#     cj = http.cookiejar.CookieJar()
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#     header = []
#     for key, value in head.items():
#         elem = (key, value)
#         header.append(elem)
#     opener.addheaders = header
#     return opener
# oper = makeMyOpener()
# uop = oper.open('http://www.baidu.com/', timeout = 1000)
# data = uop.read()
# print(data.decode())
#
# def saveFile(data):
#     save_path = "temp.out"
#     f_obj = open(save_path, 'wb')
#     f_obj.writea)
#     f_obj.close()
# saveFile(data)


#-----------------------
# import urllib
# import urllib.request
# def get_image(url):
#     request = urllib.request.Request(url)
#     response = urllib.request.urlopen(request)
#     get_img = response.read()
#     with open('001.jpg','wb') as fp:
#         fp.write(get_img)
#         print('图片下载完成')
#     return
# url = "http://upload-images.jianshu.io/upload_images/2917634-7667382cc63b833d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"
# get_image(url)

#------------------------
# import urllib
# import urllib.request
# import re
# def download_page(url):
#     request = urllib.request.Request(url)
#     response = urllib.request.urlopen(request)
#     data = response.read()
#     return data
# def get_image(html):
#     regx = r'http://[\S]*\.jpg'
#     pattern = re.compile(regx)
#     get_img = re.findall(pattern, repr(html))
#     num = 1
#     for img in get_img:
#         image = download_page(img)
#         with open('%s.jpg' %num,'wb') as fp:
#             fp.write(image)
#             num += 1
#             print('正在下载第%s张图片' %num)
#     return
#
# url = "http://www.cnblogs.com/vicowong/p/4142571.html"
# html = download_page(url)
# get_image(html)

#--------------------
import urllib.requests
ret = requests.get('http://www.baidu.com')
print(ret.url)
print(ret.text)