#!/usr/bin/python

import subprocess

def main():
	cipher = subprocess.check_output(["openssl", "list-cipher-commands"]).split()

	for line in cipher:
		command = "openssl enc -d -" + line + \
			  " -in salary_dec2003.csv.enc -out salary_dec2003.csv -pass pass:tarot"

		try:
			if(subprocess.check_call(command, shell = True) == False):
				print "decrypted with " + line
				break
		except:
			pass

if __name__ == "__main__":
	main()
