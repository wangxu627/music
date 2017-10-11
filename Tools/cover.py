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
print(type(audio.tags.getall("APIC")[0].data))
data = audio.tags.getall("APIC")[0].data
f = open("cover.jpg", "wb")
f.write(data)
f.close()
print("==============================")
audio = mutagen.File("花海.mp3")
if(audio.tags == None):
    audio.tags = ID3()
audio.tags.add(
    APIC(
        encoding=3, # 3 is for utf-8
        mime='image/png', # image/jpeg or image/png
        type=3, # 3 is for the cover image
        #desc=u'cover front',
        data=open('cover.png').read()
    )
)
print(audio.tags.pprint())
audio.save()
# print("==============================")
# audio = mutagen.File("周杰伦 - 借口.mp3")
# print(audio.tags.pprint())

