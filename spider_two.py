import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import locale
import sys
from lxml import etree
import re
import chardet

url = "http://www.shicimingju.com/book/sanguoyanyi.html"  # 三国演义的URL
menuCode = urllib.request.urlopen(url).read()
soup = BeautifulSoup(menuCode, 'html.parser')
menu = soup.find_all(id="mulu")
values = ','.join(str(v) for v in menu)
soup2 = BeautifulSoup(values, 'html.parser')
soup2 = soup2.ul
bookName = soup.h1.string
f = open('G://' + bookName + '.txt', 'a', encoding='utf8')
bookMenu = []  # 章节list
bookMenuUrl = []  # 章节url的list
for i in range(1, len(soup2.contents)-1):  # 依次爬取书的章节
    bookMenu.append(soup2.contents[i].string)
    bookMenuUrl.append(soup2.contents[i].a['href'])
urlBegin="http://www.shicimingju.com"  # 解决url为本地的问题

for i in range(0, len(bookMenuUrl)):  # 依次替换url，读取每章页面的内容
    chapterCode = urllib.request.urlopen(urlBegin+bookMenuUrl[i]).read()
    result = chardet.detect(chapterCode)   # 检验读取的页面的编码方式
    if(result['confidence'] > 0.5):   # 如果概率大于0.5 即采取这种编码
        chapterCode = chapterCode.decode(result['encoding'])
    chapterSoup = BeautifulSoup(chapterCode, 'html.parser')   # 使用BS读取解析网页代码
    chapterResult = chapterSoup.find_all(id='con2')  # 找到id=‘con2’的节点
    chapterResult = ','.join(str(v) for v in chapterResult)    # 将节点内的代码转为str类型
    chapterSoup2 = BeautifulSoup(chapterResult, 'html.parser')   # 使用BS解析节点内代码
    chapterSoup2 = chapterSoup2.br
    f.write(bookMenu[i])   # 写入文件每章标题
    for j in range(0, len(chapterSoup2)):   # 循环写入每章内容
        chapterText = chapterSoup2.contents[j].string
        f.write(chapterText)


