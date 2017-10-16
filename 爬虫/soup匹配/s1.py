from bs4 import BeautifulSoup
import requests
from lxml import html,etree


html = requests.get('http://www.ituring.com.cn/book/1863').content
#print(html)
print('-------------------------------------------------------------')
soups = BeautifulSoup(html,'lxml')
title = soups.select("table > tr > td > a")

print(title)


