import serial
import sys
import os
from subprocess import Popen
first='/home/pi/Videos/1.mp4'
second='/home/pi/Videos/2.mp4'
third='/home/pi/Videos/3.mp4'
ser=serial.Serial('/dev/ttyS0',19200,timeout=1)


while True :
 input=ser.readline()
 print(input)
 if input=='first':
  os.system('killall omxplayer.bin')
  omxc= Popen(['omxplayer','-b',first])
 if input=='second':
  os.system('killall omxplayer.bin')
  omxc= Popen(['omxplayer','-b',second])
