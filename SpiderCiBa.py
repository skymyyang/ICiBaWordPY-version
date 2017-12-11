#coding:utf-8

from bs4 import BeautifulSoup
from urllib import request
import re

def workspider():
    word = "fuck"
    url = "http://www.iciba.com/"+word
    #print(type(url))
    header = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }
    req = request.Request(url=url, headers=header)
    html = request.urlopen(req)
    bs = BeautifulSoup(html, "html.parser")
    mp = bs.findAll("i",{"class":"new-speak-step"})
    bbb = "(http://.*.mp3)"
    for i in mp:
        mp3url = i.get("ms-on-mouseover")
        print(re.findall(bbb, mp3url))
        #print(mp3url)
        # print(type(i.get("ms-on-mouseover")))
        # obj = re.compile(i, bbb)
        # print(obj)



workspider()

# /html/body/div[4]/div[6]/div[2]/div[1]/div/div/div[1]/div/div[1]/span[1]/i