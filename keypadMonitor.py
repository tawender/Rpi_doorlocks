#!/usr/bin/env python

import Tkinter as tk
import time
import logging
import sys
sys.path.append("/home/pi/Documents/css/RpiDoorLock/")
import ReadHolidays
import initialize_logger
from datetime import datetime as dt
from doorlockConstants import NORMAL_BUSINESS_HOURS_START as openHour
from doorlockConstants import NORMAL_BUSINESS_HOURS_END as closeHour

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(24,GPIO.IN)

initialize_logger.init_logger()
logging.info("Keypad monitor script started")

def switch_debounce(channel):
	logging.info("Debounce interval started")
	time.sleep(0.2)
	logging.info("Debounce time ended")
	#after debounce time check if input is still low
	if GPIO.input(24) is 0:
		correct_code_entered(0)

def correct_code_entered(channel):
	logging.info("Correct code entered")
	unlock_doors()
	time.sleep(3)
	lock_doors()
	
def unlock_from_button():
	logging.info("GUI button pressed")
	unlock_doors()
	time.sleep(2)
	lock_doors()

def unlock_doors():
	GPIO.output(12,1)
	logging.info("Doors Unlocked")
	
def lock_doors():
	logging.info("Checking date/time before locking doors again...")
	lock_doors_again = True
	#continue if weekday
	if dt.today().weekday() in range(0,5):
		logging.info("weekday detected")
		
		#continue if not a holiday
		if dt.now().strftime("%Y-%m-%d") not in ReadHolidays.readHolidays():
			logging.info("weekday not in list of holidays")
			
			#continue if current time is within normal business hours
			if dt.today().hour in range(openHour,closeHour):
				
				logging.info("time falls in normal business hours. Doors remain unlocked")
				lock_doors_again = False
				
			else:
				logging.info("time is outside normal business hours")
		else:
			logging.info("holiday detected")
	else:
		logging.info("weekend day detected")

	if lock_doors_again:
		#lock the doors
		GPIO.output(12,0)
		logging.info("Doors locked")
		
		
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(24, GPIO.FALLING, callback=switch_debounce, bouncetime=100)


root=tk.Tk()
root.title("Keypad Monitor")
root.geometry("500x150")
root.wm_state('iconic')
frame=tk.Frame(root)
frame.pack()
l=tk.Label(frame,text='This program is to always remain running.\n' +
						'It allows the raspberry pi to monitor the digital input line connected\n' +
						'to the keypad and use it as an interrupt trigger to unlock the doors.\n')
l.pack()

button = tk.Button(frame,text="Open Doors",command=unlock_from_button)
button.pack()


root.mainloop()



