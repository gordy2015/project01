
from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import pymysql

def gethtml(surl):
    response = requests.request('get',surl)
    global html
    html = response.text

    return html


def catch(html):
    soup = BeautifulSoup(html, 'lxml')
   # print(type(soup))
    print(len(soup.find_all("a",attrs={"target":"_top"})))

    for url in soup.find_all("a",attrs={"target":"_top"}):
        #print(url)
        title = url.string

        turl = url.get('href')
        if turl == '#':
            full_url = '#'
        else:
            full_url = 'http://code.ziqiangxuetang.com/django/' + turl
            print(full_url)
            u = gethtml(full_url)
            #print(u)
            soup2 = BeautifulSoup(u,'lxml')
            # print(soup2)
            content = str(soup2.select(r'div[id="main_content"]'))
            #print(type(content))
            # content = soup2.find_all("div",attrs={"id":"main_content"})
            # print(content)
            # filename = 'files/' + title + '.html'
            # print(filename)
            # write_to_file(filename,title,content)
            insertmysql(title,content)

def insertmysql(title,content):
    conn = pymysql.connect(host='192.168.2.11', port=3306, user='abc', passwd='rabc16', db='pydb',charset='utf8')

    a = title
    b = content
    cur = conn.cursor()
    # s = cur.execute("create table news(title VARCHAR(30), content VARCHAR(100))")
    # print(s)
    s = cur.execute("insert into news values(%s, %s)", [title, content])
    conn.commit()
    conn.close()
    print('-----------------------')


# def write_to_file(filename,title,content):
#     f = open(filename,'w',encoding='gbk')
#     f.write(title)
#     f.write(content)
#     f.close()
#     print('%s is writed' %title)
#     print('-----------------------')


gethtml('http://code.ziqiangxuetang.com/django/django-tutorial.html')
catch(html)
