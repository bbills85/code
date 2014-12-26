#!/usr/bin/python

import zipfile
import optparse
from threading import Thread
import time
import sys

end = False

def passwdTest(zFile, password):
	try:
		zFile.extractall(pwd = password)
		print "[+] found password " + password

                stop = time.time()
		stop = stop - start
		global end
		end = True
		print "total seconds to solve: " + str(stop)
	except:
		print "it was not: " + password
		pass

def main():
	parser = optparse.OptionParser("usage: %prog" + "-f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest = 'zname', type = 'string', help = 'specify zip file')
	parser.add_option('-d', dest = 'dname', type = 'string', help = 'specify dictionary file')
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname

	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)

	global start
	start = time.time()

	for line in passFile.readlines():
		if end:
			break
		password = line.strip('\r\n')
		passwdTest(zFile, password)
#		t = Thread(target = passwdTest, args = (zFile, password))
#		t.start()

	
if __name__ == '__main__':
	main()
