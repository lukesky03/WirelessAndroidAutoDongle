#!/usr/bin/env python3
# coding: utf-8
# Author: Edoardo Paolo Scalafiotti>> Fixed and updated by HoRo Tech
import os
import time
import signal
import sys
import RPi.GPIO as GPIO
pin = 14 # The pin ID, edit here to change it
maxTMP = 45 # The maximum temperature in Celsius after which we trigger the fan
GPIO.setmode (GPIO.BCM)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.setwarnings(False)
    return()
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    print("temp is {0}".format(temp)) #Uncomment here for testing
    return temp
def fanON():
    setPin(True)
    return()
def fanOFF():
    setPin(False)
    return()
def getTEMP():
    CPU_temp = float(getCPUtemperature())

    if CPU_temp>maxTMP:
        fanON()

    else:
        fanOFF()

    return()
def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()

try:
        setup()
        while True:
                getTEMP()
                time.sleep(8)
except KeyboardInterrupt:
        GPIO.cleanup()
