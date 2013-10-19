#########################################
## DennisX User-Managed MUD Server Kit ##
## dennis.py                           ##
## Main Program and Config Reader      ##
## Copyright 2013 PariahSoft LLC       ##
#########################################

## **********
## Permission is hereby granted, free of charge, to any person obtaining a copy 
## of this software and associated documentation files (the "Software"), to 
## deal in the Software without restriction, including without limitation the 
## rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
## sell copies of the Software, and to permit persons to whom the Software is 
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in 
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
## IN THE SOFTWARE.
## **********

import sys, time, signal

# Python 2/3 import handling
if sys.version_info[0] == 3:
	import configparser
else:
	import ConfigParser as configparser

# Dennis module imports
sys.path.append("inc/")
import world, log

# Variable setup
W = None
log = log.Log()

# Interrupt/Term signal handling
def sigint_handler(signum, frame):
	log.write("Shutting down...")
	W.running = False
signal.signal(signal.SIGINT, sigint_handler)
signal.signal(signal.SIGTERM, sigint_handler)

# Mainloop
def loop():
	while W.running:
		W.tick()
		time.sleep(1.0/60)

# Main Function
def main():
	global W
	
	# Read config file
	config = configparser.RawConfigParser()
	configfile = open("config.ini", "r")
	config.readfp(configfile)
	configfile.close()
	
	# Initialize World
	W = world.World(config, log)
	
	# Run the mainloop
	loop()
	
	# Mainloop ended, save
	W.save()
	
	# Return to OS
	return 0

# Run
main()

