from bs4 import BeautifulSoup
import requests
import os
import spider_Lib
import json

if __name__ == "__main__":
    url = 'http://music.163.com/#/song?id=287035'
    ans = spider_Lib.requestHtmlText(url)
    soup = BeautifulSoup(ans, "html.parser")
    commentPart = soup.find_all('div', class_='cnt f-brk')
    for each in commentPart:
        print(each.text)


