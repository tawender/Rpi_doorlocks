#!/usr/bin/env python

import sys
sys.path.append("/home/pi/Documents/css/RpiDoorLock/")
import ReadHolidays
	
from datetime import datetime as dt

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)


def main():
		h=ReadHolidays.readHolidays()
		
		if dt.now().strftime("%Y-%m-%d") not in ReadHolidays.readHolidays():
			GPIO.output(12,0)
		
if __name__ == '__main__':
	main()
