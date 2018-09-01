from bs4 import BeautifulSoup
import requests
import urllib.request


def RequestHtmlText(url):
	try:
		ans = urllib.request.urlopen(url).read()
		ans = ans.decode('utf-8')
		return ans
	except:
		return "Error"
		

def SaveImg(url, name):
	tmpFile = requests.get(url)
	with open("G:\imgFile\\" + str(name) + ".jpg", "wb") as file:
		file.write(tmpFile.content)	

def GetElement(url):
	menuCode = RequestHtmlText(url)
	soup = BeautifulSoup(menuCode, "html.parser")
	ImgUrls = soup.find_all("img", class_="BDE_Image")
	global indexOfImg
	for img in ImgUrls:
		indexOfImg += 1
		print("this is the " + str(indexOfImg) + " Img, Url is: " + img['src'])
		SaveImg(img['src'], indexOfImg)
	return ImgUrls
	
def GetPage(url):
	menuCode = RequestHtmlText(url)
	soup = BeautifulSoup(menuCode, "html.parser")
	htmlPage = soup.find_all("span", class_="red")
	return int(htmlPage[1].text)

if __name__=="__main__":
	indexOfImg = 0
	url = "http://tieba.baidu.com/p/5556285983"
	pageNum = GetPage(url)
	GetElement(url)
	if(pageNum >= 2):
		for num in range(2, pageNum + 1):
			tmpUrl = url + "?pn=" + str(num)
			print("this is the " + str(num) + " page")
			GetElement(tmpUrl)
  
  

