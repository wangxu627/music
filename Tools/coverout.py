#coding:utf-8

import mutagen
import os
import csv
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, APIC

import sys
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数

os.chdir("..")

def dumpout(fn):
    audio = mutagen.File(fn)
    print(audio.tags.pprint())
    data = audio.tags.getall("APIC")[0].data
    f = open("cover.png", "wb")
    f.write(data)
    f.close()


dumpout("周杰伦 - 世界未末日.mp3")