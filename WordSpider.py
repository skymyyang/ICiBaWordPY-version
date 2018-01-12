import requests
import json
import re
from bs4 import BeautifulSoup

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
        get_url = "http://www.iciba.com/index.php"
        gethtmlurl = "http://www.iciba.com/"
        r = requests.get(url=get_url, headers=header, params=parameter)
        if r.status_code == requests.codes.ok:
            s1 = r.text.split("(", 1)
            s2 = s1[1].rsplit(")", 1)
            inp_dict = json.loads(s2[0])
            try:
                symbols = inp_dict["baesInfo"]["symbols"]
                # 获取英国音标
                self.ph_en = symbols[0]["ph_en"]
                # print(self.ph_en)
                # 获取美国音标
                self.ph_an = symbols[0]["ph_am"]
                # 获取释义
                self.parts = symbols[0]["parts"]
                # 获取例句
                sentence_dict = {}
                try:
                    for sen1 in inp_dict["sentence"]:
                        sentence_dict[sen1["Network_en"]] = sen1["Network_cn"]
                    self.sentence.append(sentence_dict)
                except KeyError as e:
                    print("There is no have sentence...., the err is %s" % e)

                # 获取英式发音
                ph_en_mp3 = symbols[0]["ph_en_mp3"]
                try:
                    yingres = requests.get(ph_en_mp3, stream=True)
                    with open("voice\\" + self.word + "ying.mp3", "wb") as f:
                        for chunk in yingres.iter_content(chunk_size=100):
                            f.write(chunk)
                    self.ph_en_mp3 = "/voice/" + self.word + "ying.mp3"
                except:
                    #如果用api返回的response无法获取到英式发音，就直接请求web界面，然后解析html获取
                    print("The Response is no ph_en_mp3 of ths %s..." % self.word,"try with http://www.iciba.com/"+self.word)
                    r = requests.get(url=gethtmlurl+self.word.replace(' ','%20'),headers=header)
                    bs = BeautifulSoup(r.text, "html.parser")
                    mp = bs.findAll("i", {"class": "new-speak-step"})
                    bbb = "(http://.*.mp3)"
                    mp3urllist = []
                    for i in mp:
                        mp3url = i.get("ms-on-mouseover")
                        mp3url2 = re.findall(bbb, mp3url)[0]
                        mp3urllist.append(mp3url2)
                    #print(mp3urllist)
                    yingres = requests.get(mp3urllist[0], stream=True)
                    with open("voice\\" + self.word + "ying.mp3", "wb") as f:
                        for chunk in yingres.iter_content(chunk_size=100):
                            f.write(chunk)
                    self.ph_en_mp3 = "/voice/" + self.word + "ying.mp3"






                # 获取美式发音
                ph_am_mp3 = symbols[0]["ph_am_mp3"]
                try:
                    meires = requests.get(ph_am_mp3, stream=True)
                    with open("voice\\" + self.word + "mei.mp3", "wb") as f:
                        for chunk in meires.iter_content(chunk_size=100):
                            f.write(chunk)
                    self.ph_an_mp3 = "/voice/" + self.word + "mei.mp3"
                except:
                    print("There is no ph_am_mp3 of ths %s..." % self.word)
                    r = requests.get(url=gethtmlurl + self.word.replace(' ','%20'), headers=header)
                    bs = BeautifulSoup(r.text, "html.parser")
                    mp = bs.findAll("i", {"class": "new-speak-step"})
                    bbb = "(http://.*.mp3)"
                    mp3urllist = []
                    for i in mp:
                        mp3url = i.get("ms-on-mouseover")
                        mp3url2 = re.findall(bbb, mp3url)[0]
                        mp3urllist.append(mp3url2)
                    #print(mp3urllist)
                    try:
                        meires = requests.get(mp3urllist[1], stream=True)
                        with open("voice\\" + self.word + "mei.mp3", "wb") as f:
                            for chunk in meires.iter_content(chunk_size=100):
                                f.write(chunk)
                        self.ph_an_mp3 = "/voice/" + self.word + "mei.mp3"
                    except:
                        print("彻底没有美式发音了")
            except KeyError as e:
                try:
                    symbols = inp_dict["baesInfo"]#此时只能获取例句了
                    sentence_dict = {}
                    try:
                        for sen1 in symbols["sentence"]:
                            sentence_dict[sen1["Network_en"]] = sen1["Network_cn"]
                        self.sentence.append(sentence_dict)
                    except KeyError as e:
                        print("There is no have sentence...., the err is %s" % e)
                except:
                    print("do not have this word %s" %self.word)







        else:
            print("requeest is fail......")
        return self



# tt = WordSpider("fuck")
# rs = tt.workSpider()
# print(rs.word)
# print("-----")
# print(rs.ph_en)
# print(str(rs.sentence))

