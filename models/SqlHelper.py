from sqlalchemy.orm import sessionmaker
from models.SqlInit import *



def InsertWordBase(word, ph_en, ph_am, parts, sentence, ph_en_mp3, ph_am_mp3):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    wordall = Word_base(f_word=word, f_esymbol=ph_en, f_asymbol=ph_am, f_explain=parts, f_liju=sentence, f_espoken=ph_en_mp3, f_aspoken=ph_am_mp3)
    session.add(wordall)
    session.commit()
    session.close()


