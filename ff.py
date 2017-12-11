
import requests
import json
from ReadExcel.readexcel import ReadExcel

reload = {"callback":"jQuery19005947467512740838_1512442403921", "a":"getWordMean", "c":"search", "list":"1,2,3,4,5,8,9,10,12,13,14,15,18,21,22,24,3003,3004,3005","word":"fuck","_":"1512442403922"}
r = requests.get(url="http://www.iciba.com/index.php", params=reload)
s1 = r.text.split("(", 1)
s2 = s1[1].rsplit(")", 1)
inp_dict = json.loads(s2[0])
symbols = inp_dict["baesInfo"]["symbols"]
ph_en = symbols[0]["ph_en"] #获取英国音标
ph_am = symbols[0]["ph_am"]#获取美国音标
parts = symbols[0]["parts"] #获取释义
sentence = inp_dict["sentence"] #获取例句
ph_en_mp3 = symbols[0]["ph_en_mp3"]#获取英式发音
ph_am_mp3 = symbols[0]["ph_am_mp3"]#获取美式发音
# print(symbols)
print(ph_en)
print(ph_am)
print(parts)
print(ph_en_mp3)
print(ph_am_mp3)
print(sentence)

