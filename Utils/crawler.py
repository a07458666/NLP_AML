import requests
from bs4 import BeautifulSoup

websiteNameDic = {
    'news.cnyes.com' : [0,0,0]
}

def getWebsiteCategory(stringData):
    return stringData.split('/')[2]

def getSoup(url):
    headers = {'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit / 537.36 Chrome / 70.0.3538.102 Safari / 537.36'} 
    resp = requests.get(url, headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup

def getContext(websiteCategory, url):
    name1, name2, name3 = websiteNameDic[websiteCategory]

    return name1, name2, name3