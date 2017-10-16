

# import re
# from bs4 import BeautifulSoup
#
# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were</p>
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# '''
#
# soup = BeautifulSoup(html,'lxml')
# #print(soup.prettify())
# # print(soup.title)
# # print(soup.a.attrs)
# # print(type(soup.p))
# # print(soup.p.get('class'))
# # soup.p['class'] = 'newttt'
# # print(soup.p)
# # del soup.p['class']
# # print(type(soup.p.string))
#
#
# # print(type(soup.a.string))
# # #print(soup.a.string)
# #
# # if type(soup.a.string) == 'bs4.element.Comment':
# #     print(soup.a.string)
# # else:
# #     print('false')
#
# #print(soup.descendants)
#
# # print(soup.find_all("a", limit=1))
# #
# # for tag in soup.find_all(re.compile("^b")):
# #     print(tag.name)
#
# print(soup.select('title')[0].get_text())





#
from pymongo import MongoClient
conn = MongoClient('192.168.2.11',27017)

db = conn.testdb
if db:

    print('connect success')
    coll = db.student
    print(coll)
    information = {"name":"alex","email":"alee@qq.com","age":27}
    # #posts = db.posts
    info_id = coll.insert(information)
    print(info_id,type(info_id))
else:
    print('connect false')

