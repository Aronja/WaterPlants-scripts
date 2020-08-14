#!/usr/bin/env python

import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)
time.sleep(2)

GPIO.output(17, GPIO.HIGH)
GPIO.cleanup()
~
~
~
~
~
~
~
                                                                                     16,14         All
