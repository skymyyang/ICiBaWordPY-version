import requests
import json


class WordSpider():
    def __init__(self, word):
        """初始化变量"""
        self.word = word
        self.ph_en = "" #英式发音
        self.ph_an = "" #美式发音
        self.parts = [] #释义,默认是一个空列表，列表中的元素是字典，对应的是相对应的词性和解释
        self.sentence = [] #例句，默认是一个空列表，列表中的元素也是字典，一个例句对应一个中文释义
        self.ph_en_mp3 = "" #英式发音
        self.ph_an_mp3 = "" #美式发音
    def workSpider(self):
        parameter = {"callback":"jQuery19005947467512740838_1512442403921",
                     "a":"getWordMean",
                     "c":"search",
                     "list":"1,2,3,4,5,8,9,10,12,13,14,15,18,21,22,24,3003,3004,3005",
                     "word": self.word,
                     "_":"1512442403922"}
        header = {
            'Host': r'www.iciba.com',
            'Connection': 'keep-alive',
            'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }



