# coding=utf-8
import string
import base64
import codecs
import ctypes
import re

buf2=[]
llehscode = open('payload.py')
llehscode = llehscode.read()
#print(llehscode)
buf=re.findall("\\\\[a-z0-9]+",llehscode)

#print(buf)
for i in buf:
    i=re.findall("[a-z0-9]+",i)[0]
    buf2.append(i)
print(buf2)