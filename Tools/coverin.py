#coding:utf-8

import mutagen
import os
import csv
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, APIC

import sys
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数

os.chdir("..")
files = os.listdir(".")

for f in files:
    if(f.endswith(".mp3") or f.endswith(".MP3")):
        audio = mutagen.File(f)
        audio.tags.add(
            APIC(
                encoding=3, # 3 is for utf-8
                mime='image/png', # image/jpeg or image/png
                type=3, # 3 is for the cover image
                data=open('cover.png').read()
            )
        )
        audio.save()
