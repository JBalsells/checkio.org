# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:09:36 2015

@author: jorge_000
"""


def checkio(n, m):
    c=0 
    n=bin(n)
    m=bin(m)    
    n=n.replace("0b","")
    m=m.replace("0b","")
    for i in range (0,19):
        if (len(n)<=19):
            n="0"+n
        if (len(m)<=19):
            m="0"+m
    for i in range(0,20):
        if n[i]=="1" and m[i]=="0":
            c+=1
        if n[i]=="0" and m[i]=="1":
            c+=1
    return (c)
    
    
print checkio(16,15);

