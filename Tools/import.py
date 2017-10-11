#coding:utf-8

import mutagen
import os
import csv
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC

import sys
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数

def setValue(key, value, tags, force = False):
    if(force == True):
        tags.delall(key)
    if(tags.getall(key) == []):
        if(key == "TIT2"):
            tags[key] = TIT2(encoding=3, text=value)
        elif(key == "TALB"):
            tags[key] = TALB(encoding=3, text=value)
        elif(key == "TPE1"):
            tags[key] = TPE1(encoding=3, text=value)
        return True
    return False

def updateFile(title, album, author, fn):
    if((fn.endswith(".mp3") or fn.endswith(".MP3")) and os.path.exists(fn)):
        print(title)
        print(album)
        print(author)
        print(fn)
        print("=======")
        audio = mutagen.File(fn)
        if(audio.tags == None):
            audio.tags = ID3()
        updated = False
        updated = setValue('TIT2', title, audio.tags, True) or updated
        updated = setValue('TALB', album, audio.tags, True) or updated
        updated = setValue('TPE1', author, audio.tags, True) or updated
        if(updated == True):
            audio.save()

with open('import.csv', 'rb') as file:      # 采用b的方式处理可以省去很多问题
    reader = csv.reader(file)
    os.chdir("..")
    fl = True
    for row in reader:
        if(fl == False):
            updateFile(row[0], row[1], row[2], row[3])
        if(fl == True):
            fl = False


