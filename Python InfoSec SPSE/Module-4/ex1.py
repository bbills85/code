#!/usr/bin/python

import urllib
import sys
import time

def statusCheck(count, block_size, total_size):
	"""simple function used to display percentage of file downloaded"""
	# if statement veifying when size = 0
	if not count:
		print "connection established ..."

	# simple variable calculating total sized downloaded
	current_state = (block_size * count / float (total_size)) * 100

	# utilizing stdout versus print to stay on one line
	# /r returns to the beginning of the line, allows % to increase
	sys.stdout.write("\rdownloading ... %d%%" % current_state)
	# flush stdout's buffer and allow it to write now
	sys.stdout.flush()

	# ***used to delay % for bedugging purposes only***
	time.sleep(.025)

	# once the block size is equal to total size, file is 100%
	if (block_size * count) == total_size:
	        sys.stdout.write("\rdownloading ... complete!\n")
		sys.stdout.flush()
	

def main():
	"""main function used to download file"""
	# simple variable used to hold webpage
	url = "http://localhost/files/GitHub.rar"

	print "downloading from ... " + url

	# containing url, what the file will be named on local box,
	# and calls function statusCheck
	urllib.urlretrieve(url, "GitHub.rar", reporthook = statusCheck)

if __name__ == '__main__':
	main()
