#!/usr/bin/env python

from ConfigParser import ConfigParser
import logging

def init_logger():
	#log configuration
	logging_configuration_filename = "/home/pi/Documents/css/RpiDoorLock/logging_config.cfg"
	c_file = open(logging_configuration_filename, 'r')
	logging_config = ConfigParser()
	logging_config.readfp(c_file)
	logfile_name = logging_config.get('log settings','filename')

	#setup of logging module 
	logging.basicConfig(format='%(asctime)s %(module)s.py:%(levelname)s:%(message)s',
						filename=logfile_name,level=logging.DEBUG)

def main():
	init_logger()

if __name__ == '__main__':
	main()
