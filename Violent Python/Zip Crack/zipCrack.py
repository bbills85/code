#!/usr/bin/python

import zipfile
import optparse

end = False

def passwdTest(zFile, password):
	try:
		zFile.extractall(pwd = password)
		print "[+] found password " + password

		global end
		end = True
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

	for line in passFile.readlines():
		if end:
			exit(0)
		password = line.strip('\r\n')
		passwdTest(zFile, password)
	
if __name__ == '__main__':
	main()
