# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:52:08 2022

@author: user
"""
from checking.temperature import checkT
from checking.humidity import checkH
from checking.light import checkL
from checking.soilMois import checkS

tmep=input("Enter temperature: ")
humi=input("Enter humidity: ")
light=input("Enter light intensity: ")
sMois=input("Enter soil moisture: ")
checkT(temp)