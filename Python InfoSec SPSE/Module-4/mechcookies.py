#!/usr/bin/python

import mechanize

def main():
	print "[+] first login ...."
	# create cookie object
	cookies = mechanize.CookieJar()
	# create browser object
	br = mechanize.Browser()
	# open dvwa
	br.open('http://localhost/dvwa/')
	# set the cookie to the cookie jar
	br.set_cookiejar(cookies)
	# print the title of the current page
	print br.title()

	print "[+] logging in ...."
	# select the first form
	br.select_form(nr = 0)
	# set username and password
	br.form['username'] = 'admin'
	br.form['password'] = 'password'
	# submit the form
	br.submit()
	# print the title of the current page
	print br.title()

	print "[+] attempting login with new object and same cookie ...."
	# create a new browser object
	br2 = mechanize.Browser()
	# set the cookie to the one in the cookie jar
	br2.set_cookiejar(cookies)
	# open dvwa and no need to login
	br2.open('http://localhost/dvwa/')
	# print the title of the current page
	print br2.title()

	print "[+] attempting login with new object and no cookie ...."
        # create a new browser object
        br3 = mechanize.Browser()
        # open dvwa without cookie, need to login again
        br3.open('http://localhost/dvwa/')
        # print the title of the current page
        print br3.title()

if __name__ == "__main__":
	main()
