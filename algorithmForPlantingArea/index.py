# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:52:08 2022

@author: user
"""
from multiprocessing.sharedctypes import Value
from checking.temperature import checkT
from checking.humidity import checkH
from checking.light import checkL
from checking.soilMois import checkS

def average(list):
    return sum(list)/len(list)

def worest(list):
    list=sorted(list)
    lower=list[0]
    for key, value in mark.items():
        if lower==value:
            return key

temp=input("Enter temperature (°C): ")
humi=input("Enter humidity (%): ")
light=input("Enter light (hr): ")
sMois=input("Enter soil moisture (%): ")
print("Processing...")
tMark=checkT(temp)
hMrak=checkH(humi)
lMark=checkL(light)
sMark=checkS(sMois)
mark={"temperature":tMark,"humidity":hMrak,"light":lMark,"soilMois":sMark}
markList=[mark["temperature"], mark["humidity"],mark["light"],mark["soilMois"]]
lower=worest(markList)
averMark=average(markList)
if averMark>49:
    print("This area is sutiable for planting, mark: "+str(averMark))
else: print("Area may not sutiable for planting, mark: "+str(averMark)+" (lower than 50).\n You can change this factor to amke a better environment: "+lower)