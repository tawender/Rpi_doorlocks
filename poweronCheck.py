#!/usr/bin/env python

# This script should be automatically run at power-on. It will set the door locks in the appropriate state
# in the event of power being restored to the raspberry pi

import logging
import sys
sys.path.append("/home/pi/Documents/css/RpiDoorLock/")
import ReadHolidays
import initialize_logger
initialize_logger.init_logger()

from doorlockConstants import NORMAL_BUSINESS_HOURS_START as openHour
from doorlockConstants import NORMAL_BUSINESS_HOURS_END as closeHour
	
from datetime import datetime as dt

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)


#The doors will come up in the locked state at power-up.
#The next block of code checks the date/time to see if doors should be unlocked

logging.info("Power-up script executed. Checking date/time...")
#continue if weekday
if dt.today().weekday() in range(0,5):
        logging.info("weekday detected")
	
	#continue if not a holiday
	if dt.now().strftime("%Y-%m-%d") not in ReadHolidays.readHolidays():
		logging.info("weekday not in list of holidays")
		
		#continue if current time is within normal business hours
		if dt.today().hour in range(openHour,closeHour):
			
			logging.info("time falls in normal business hours...")
			
			#unlock the doors
			GPIO.output(12,1)
			logging.info("Doors Unlocked")
		else:
                        logging.info("time is outside normal business hours. Doors remain locked")
        else:
                logging.info("holiday detected. Doors remain locked")
else:
        logging.info("weekend day detected. Doors remain locked")

