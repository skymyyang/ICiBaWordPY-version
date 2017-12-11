from xlrd import open_workbook

class ReadExcel:
    def __init__(self):
        self.words = []

    def readsheet(self, Excelpath):
        """ 读取Excel的所有单词，并添加到列表"""
        messageInfo = open_workbook(Excelpath)
        #打开excel文件读取数据
        sheetInfo = messageInfo.sheets()[0]
        #获取第一个工作表，且通过索引顺序获取
        row_index = 0
        while row_index < sheetInfo.nrows:
            v = sheetInfo.cell(row_index, 0).value
            self.words.append(sheetInfo.cell(row_index, 0).value)
            row_index += 1
        return self.words