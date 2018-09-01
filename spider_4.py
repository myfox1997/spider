# -*- coding: UTF-8 -*-
import sys
from bs4 import BeautifulSoup
import urllib.request
import chardet
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import lxml.html
import requests

class Render(QWebEngineView):
    def __init__(self, url):
        self.html = ''
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)       # 子类构造函数继承父类，这种写法python2和3通用，还可以是super().__init__()
        self.loadFinished.connect(self._loadFinished)
        self.load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self):
        self.page().toHtml(self.callable)

    def callable(self, data):
        self.html = data
        self.app.quit()

if __name__ == '__main__':
    url = 'https://cn.bing.com'
    re = Render(url)
    result = re.html
    soup = BeautifulSoup(result, 'html.parser')
    aTag = soup.find(id='sh_cp')
    # print(aTag.get('title'))
    weburl = r"http://area.sinaapp.com/bingImg/"
    page = requests.get(weburl)
    fileName = aTag.get('title').split('(')
    fileName = fileName[0]
    with open('C://Users//moyuan//Desktop//' + fileName + '.jpg', 'wb') as f:
        f.write(page.content)

    print('download successful')

