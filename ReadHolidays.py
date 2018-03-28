#!/usr/bin/env python

# This script reads through a text file containing a listing of business holidays
# and returns the contents of the file in list format containing a separate
# list entry for each date found in the file


def readHolidays():
	holidays = []
	for line in open("/home/pi/Documents/css/RpiDoorLock/holiday_list.txt"):
		if (not line.startswith("#")) and (len(line.strip())>0):
			holidays.append(line.split("#")[0].strip())
			
	return holidays
	
	
def main():
	
	h=readHolidays()
	
	print "Found %d holiday dates in the file"%(len(h))
	for item in h:
		print item

if __name__ == '__main__':
	main()
