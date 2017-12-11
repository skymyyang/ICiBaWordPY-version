from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, DATE, Table, BigInteger, TEXT

#create_engine()用来初始化数据库连接
engine = create_engine("mysql+pymysql://root:123456@192.168.180.187/lytest?charset=utf8")
#创建对象的基类
Base = declarative_base()

#创建单词的基本表
class Word_base(Base):
    __tablename__ = 'word_base'
    id = Column(Integer, primary_key=True)
    f_word = Column(String(32))
    f_esymbol = Column(String(255))
    f_asymbol = Column(String(255))
    f_explain = Column(TEXT)
    f_liju = Column(TEXT)
    f_espoken = Column(String(255))
    f_aspoken = Column(String(255))

if __name__ == "__main__":
    Base.metadata.create_all(engine)




