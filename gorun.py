from ReadExcel.readexcel import ReadExcel
from models.SqlHelper import InsertWordBase
from WordSpider import WordSpider


if __name__ == "__main__":
    readExcel = ReadExcel()
    words = readExcel.readsheet("wordExcel\\word.xlsx")
    print(len(words))
    for tmpword in words:
        tmpword = str(tmpword)
        tmpword = tmpword.replace("",'').replace("",'').replace("）",'').replace("（",'').replace("…"," ").replace('’','\'').rstrip()
        print("start the word of %s is spiding..." %tmpword)
        example = WordSpider(tmpword)
        thedata = example.workSpider()
        InsertWordBase(thedata.word, thedata.ph_en, thedata.ph_an, str(thedata.parts), str(thedata.sentence), thedata.ph_en_mp3, thedata.ph_an_mp3)
        print("the word of %s is spider end"  %(tmpword))

