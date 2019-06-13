#!/usr/bin/env python

import logging
import sys
sys.path.append("/home/pi/Documents/css/RpiDoorLock/")
import ReadHolidays
import initialize_logger
	
from datetime import datetime as dt

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)



def main():
		initialize_logger.init_logger()
		
		h=ReadHolidays.readHolidays()
		
		if dt.now().strftime("%Y-%m-%d") not in ReadHolidays.readHolidays():
			GPIO.output(12,0)
			logging.info("Doors Locked")
		
if __name__ == '__main__':
	main()
