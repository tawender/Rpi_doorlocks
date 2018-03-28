#!/usr/bin/env python

import sys
sys.path.append("/home/pi/Documents/css/RpiDoorLock/")
import doorsUnlocked
import doorsLocked
import Tkinter as tk
import time


import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)


def unlock_doors():
	GPIO.output(12,1)
	
def lock_doors():
	GPIO.output(12,0)
	
def keypad_entry(channel):
	unlock_doors()
	time.sleep(5)
	lock_doors()

GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(24, GPIO.FALLING, callback=keypad_entry, bouncetime=300)


root=tk.Tk()
root.title("Keypad Monitor")
root.geometry("500x150")
root.wm_state('iconic')
frame=tk.Frame(root)
frame.pack()
l=tk.Label(frame,text='This program is to always remain running.\n' +
						'It allows the raspberry pi to monitor the digital input connected\n' +
						'to the keypad and use it as a trigger to unlock the doors.\n')
l.pack()

root.mainloop()

