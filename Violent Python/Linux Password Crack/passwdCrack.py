#!/usr/bin/python

import crypt

passFile = open('/etc/shadow')

blah = ['test', 'baseball', 'book', 'blah']

def passTest(salt, passwd):
	# cycles through dictionary
	for i in range(0, len(blah)):
		# compares words encrypted with salt versus actual passwd
		if crypt.crypt(blah[i], salt) == passwd[1]:
			print "[+] password found ...."
			print '[+] username: ' + passwd[0] + ' .... password: ' + blah[i]
		else:
			print '[-] no password found for username: ' + passwd[0]

def main():
	print "[+] linux password cracker initialized ...."
	print "[+] reading in enrypted passwords ...."

	#reads each line from the shadowfile
	for line in passFile.readlines():
		line = line.split(':')
		#only looks for users with acutal passwords
		if line[1][0] is '$':
			# stores name and full password hash
			passwd = line[0:2]
			# splits the shadow password from its hash and salt
			shadow = line[1].split('$')
			# recreates the salt
			salt = '$' + shadow[1] + '$' + shadow[2] + '$'
			# calls passTest with salt and full passwd
			passTest(salt, passwd)
		else:
			print '[+] username: ' + line[0] + ' .... no password on file'


	print "[+] finished reading password file ...."
	print "[+] shutting down ...."

if __name__ == "__main__":
	main()
