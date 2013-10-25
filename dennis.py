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

import json, signal, sys, time

# Dennis module imports
sys.path.append("inc/")
import world

# Variable setup
W = None

# Interrupt/Term signal handling
def sigint_handler(signum, frame):
	W.log.write("Shutting down...")
	W.running = False
signal.signal(signal.SIGINT, sigint_handler)
signal.signal(signal.SIGTERM, sigint_handler)

# Mainloop
def loop(tickspeed):
	while W.running:
		W.tick()
		time.sleep(1.0/tickspeed)

# Main Function
def main():
	global W
	
	# Read config file
	configfile = open("config.json", "r")
	try:
		config = json.load(configfile)
	except ValueError:
		return 1
	configfile.close()
	
	# Initialize World
	W = world.World(config)
	if not W.plugin_manager.autoload():
		return 1
	
	# Run the mainloop
	loop(config["dennis"]["tickspeed"])
	
	# Mainloop ended, finish plugins and save
	for plugin in W.plugin_manager:
		plugin.finish()
	W.save()
	
	# Return to OS
	return 0

# Run
main()

