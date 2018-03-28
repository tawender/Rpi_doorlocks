#!/usr/bin/env python

# This script should be automatically run at power-on. It will set the door locks in the appropriate state
# in the event of power being restored to the raspberry pi

import sys
sys.path.append("/home/pi/Documents/css/RpiDoorLock/")
import ReadHolidays
	
from datetime import datetime as dt

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)

NORMAL_BUSINESS_HOURS_START = 8		#8:00am
NORMAL_BUSINESS_HOURS_END	= 22	#5:00pm

#The doors will come up on the locked state.
#The next block of code checks to see if doors should be unlocked

#continue if weekday
if dt.today().weekday() in range(0,5):
	
	#continue if not a holiday
	if dt.now().strftime("%Y-%m-%d") not in ReadHolidays.readHolidays():
		
		#continue if current time is within normal business hours
		if dt.today().hour in range(NORMAL_BUSINESS_HOURS_START,NORMAL_BUSINESS_HOURS_END):
			
			#unlock the doors
			GPIO.output(12,1)


