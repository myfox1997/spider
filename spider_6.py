import requests
import time

weburl = r"http://area.sinaapp.com/bingImg/"
page = requests.get(weburl)
img_name = time.strftime("%Y%m%d") + '.jpg'
with open(img_name,'wb') as f:
    f.write(page.content)

print('download successful')

