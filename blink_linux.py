#!/usr/bin/env python
 
import os
import time
 
 
os.system("echo 8 > /sys/class/gpio/unexport")
os.system("echo 8 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio35/direction")
 
count = 0
while count < 4:
        print "______LED is ON_____"
        os.system("echo 1 > /sys/class/gpio/gpio35/value")
        time.sleep(1)
        print "_____LED is off ____"
        os.system("echo 0 > /sys/class/gpio/gpio35/value")
        time.sleep(1)
        count = count +1