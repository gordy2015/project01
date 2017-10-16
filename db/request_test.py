#
# import requests
#
# r = requests.request('get','http://www.baidu.com')
#
# print(r.content.decode('utf-8'))
# print(r.encoding)


from lxml import etree

# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
#      </ul>
#  </div>
# '''
#
# html = etree.HTML(text)
# result = etree.tostring(html)


html = etree.parse('h.html')
result = html.xpath('//li/text()')
# print(html)
print(type(result),result)
for i in result:
    print(i)
# print(type(result[0]),result[0])
# print('--------------------------')
#
# result2 = html.xpath('//li/@class')
# print(type(result2), result2)
# print('--------------------------')
#
# result3 = html.xpath('//li/a/text()')
#result3 = html.xpath('//li/a/@href')
# print(type(result3), result3)
# for m in result3:
#     print(m)
# print('--------------------------')


