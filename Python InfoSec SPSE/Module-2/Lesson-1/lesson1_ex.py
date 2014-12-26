#!/usr/bin/python

from sys import argv

# error handling
try:
	logFile = open(argv[1])
except:
	print "[-] file \'%s\' does not exist" % argv[1]
else:
	print "[+] searching for \'usb\' in the \'%s\' file" % argv[1]

	# searches for white space around usb for exact matches
	for line in logFile.readlines():
		#if ' usb ' in line.lower(): # lowercases entire line
		if ' usb ' in line: # whitespace added to caputre only usb
			print line.strip()

	print "[+] serach completed"

	logFile.close()
