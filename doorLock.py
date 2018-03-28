#!/usr/bin/env python


import ReadHolidays
from datetime import datetime as dt



def main():
	
	if dt.now().strftime("%Y-%m-%d") in ReadHolidays.readHolidays():
		print "holiday today!"
	else:
		print "unlocking doors"

if __name__ == '__main__':
	main()
