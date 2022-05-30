# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:52:08 2022

@author: user
"""
import pyb
from pyb import UART
from checking.temperature import checkT
from checking.humidity import checkH
from checking.light import checkL
from checking.pressure import checkP


def send(status, factor):
    if status:
        uart.write('Area is sutable for planting.')
    else:
        uart.write('Area is not sutable for planting, '+factor+' not sutable.')


redLED = pyb.LED(1)
greenLED = pyb.LED(2)
blueLED = pyb.LED(3)
data = []
uart = UART(1)
uart.init(115220, bits=8, parity=None, stop=1, timeout=0, flow=0, timeout_char=0, read_buf_len=64)
for i in range(2):
    if uart.read == "":
        break
    else:
        redLED.on()
greenLED.on()
blueLED.on()
data = uart.read()
if checkT(data[0]):
    if checkH(data[1]):
        if checkL(data[2]):
            if checkP(data[3]):
                send(True, None)
            else:
                send(False, 'pressure')
        else:
            send(False, 'light')
    else:
        send(False, 'humidity')
else:
    send(False, 'temperature')
blueLED.off()
