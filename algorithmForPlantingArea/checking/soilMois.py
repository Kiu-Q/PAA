# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:57:12 2022

@author: user
"""

def checkS(data):
    target=30.5
    data=float(data)
    if data>target:
        diff=(data-target)/target*100
        return 100 - diff
    if data<target:
        diff=(target-data)/data*100
        return 100 - diff
    if data==target:
        return 100