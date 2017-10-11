#coding:utf-8

import mutagen
import os
import csv
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, APIC

import sys
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数

os.chdir("..")

audio = mutagen.File("小幸运_田馥甄.mp3")
print(audio.tags.pprint())

print("==============================")
audio = mutagen.File("花海.mp3")

print(audio.tags.pprint())

# print("==============================")
# audio = mutagen.File("周杰伦 - 借口.mp3")
# print(audio.tags.pprint())

