#!/usr/bin/python

import signal
import sys

def alarm_handler(signum, frame):
	print "Shutting down..."
	sys.exit(0)

userInput = raw_input("Enter the number of seconds to wait: ")

signal.signal(signal.SIGALRM, alarm_handler)

signal.alarm(int(userInput))

print "Waiting %s seconds to shutdown!" % userInput

while True:
	pass
