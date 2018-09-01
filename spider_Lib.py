import requests


def requestHtmlText(url):
    try:
        ans = requests.get(url, timeout=30)
        ans.raise_for_status()
        ans.encoding = ans.apparent_encoding
        return ans.text
    except:
        return 'Error'
