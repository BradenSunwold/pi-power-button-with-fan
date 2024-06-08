#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time

def WaitForShutdownEdge() :
    currentLevel = GPIO.input(3)
    while(GPIO.input(3) == currentLevel) :
        time.sleep(.01)


GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, True)
time.sleep(0.01)
#GPIO.wait_for_edge(3, GPIO.FALLING)
WaitForShutdownEdge()

subprocess.call(['shutdown', '-h', 'now'], shell=False)
