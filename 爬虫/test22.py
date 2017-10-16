#
import urllib
import urllib.request

url = '<a class="post-title" href="http://www.xuliangwei.com/xubusi/860.html" title="Git系列五之标签管理">Git系列五之标签管理</a>'

full_url = 'http://www.ruigaokeji.cn'
request = urllib.request.urlopen(full_url)
response = request.read()
data = response.decode('UTF-8')
# print(data)

first = data.find(r'<img src=')
# print(first)
#href = data.find(r'href=',first)
# print(href)
html = data.find(r'.png',first)
# print(html)
link = data[first+10:html+4]
print(link)

setw = []
for i in range(21):
    first = data.find(r'<img src=', html)
    # print(first)
    html = data.find(r'.png', first)
    # print(html)
    link = data[first + 10:html + 4]
    print(link)
    setw.append(link)
    # print(setw)

for w in setw:
    #print(w)
    rurl = 'http://www.xxx.com'
    request = urllib.request.urlopen(w)
    response = request.read()
    # # data = response.decode('UTF-8')
    #print(response)
    q = w[+len(rurl):]
    #print(q)
    f = open( 'D:\BaiduNetdiskDownload\webpa\%s' % q,'wb+')
    print('downloading %s' %q)
    f.write(response)
    print('%s download end' %q)
    f.close()

