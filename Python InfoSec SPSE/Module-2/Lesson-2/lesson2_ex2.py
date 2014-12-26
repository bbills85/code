#!/usr/bin/python

import os, sys, glob, time

for root, dir, files in os.walk(sys.argv[1]):
	x = root.split('/')
	if root == sys.argv[1]:
		print "[+] starting %s directory navigation" % root
		if root == sys.argv[1] and x[-1] == '':
			print '[' + x[-2] + ']'
		else:
			print '[' + x[-1] + ']'
	else:
		print '-' * len(x) + '[' + x[-1] + ']'
		for name in glob.glob(os.path.join(root, '*')):
			shortName = name.split('/')
			print ('--' * len(x) + shortName[-1]
				+ '\n\t-size:          ' + str(os.path.getsize(name))
				+ '\n\t-created:       ' + str(time.ctime(os.path.getctime(name)))
                                + '\n\t-last modified: ' + str(time.ctime(os.path.getmtime(name)))
                                + '\n\t-path:          ' + os.path.realpath(name))
