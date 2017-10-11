#coding:utf-8

import mutagen
import os
import shutil
import csv
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC

import sys
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数


def getValue(key, tags):
    value = ""
    if(tags.getall(key) != []):
        if(audio.tags[key].encoding == mutagen.id3.Encoding.LATIN1):
            value = audio.tags[key].text[0].encode("iso-8859-1").decode('gbk')
        else:
            value = audio.tags[key].text[0]
    return value


files = os.listdir("../.")
os.chdir("..")
for f in files:
    if(f.endswith(".mp3") or f.endswith(".MP3")):
        audio = mutagen.File(f)
        album = getValue('TALB', audio.tags)
        if(not os.path.exists(album)):
            os.mkdir(album)
        shutil.move(f, os.path.join(album, f))
            
            

            

