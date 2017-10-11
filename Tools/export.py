#coding:utf-8

import mutagen
import os
import time
import csv
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC

import sys
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数


def getValue(key, tags):
    value = ""
    if(tags.getall(key) != []):
        #print(audio.tags[key].encoding)
        if(audio.tags[key].encoding == mutagen.id3.Encoding.LATIN1):
            value = audio.tags[key].text[0].encode("iso-8859-1").decode('gbk')
        else:
            value = audio.tags[key].text[0]
    return value

with open(str(int(time.time() * 1000)) + '_export.csv', 'wb') as file:      # 采用b的方式处理可以省去很多问题
    writer = csv.writer(file)
    header = ['曲目名'] + ['专辑名'] + ['歌手'] + ['文件名']
    writer.writerow(header)

    os.chdir("..")
    files = os.listdir(".")
    for f in files:
        if(f.endswith(".mp3") or f.endswith(".MP3")):
            audio = mutagen.File(f)
            title = ""
            album = ""
            author = ""
            if(audio.tags != None):
                title = getValue('TIT2', audio.tags)
                album = getValue('TALB', audio.tags)
                author = getValue('TPE1', audio.tags)
            content = [title] + [album] + [author] + [f]
            writer.writerow(content)
            
            

            

