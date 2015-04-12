#!/usr/bin/python

# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
# http://pymotw.com/2/getopt/
# http://stackoverflow.com/questions/15993238/python-invalid-literal-for-int-base-10
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# http://palewi.re/posts/2008/04/20/python-recipe-grab-a-page-scrape-a-table-download-a-file/
# http://stackoverflow.com/questions/15956597/beautifulsoup-parsing-and-writing-the-data-in-a-text-file
# http://www.tutorialspoint.com/python/python_files_io.htm
# http://www.tutorialspoint.com/python/python_database_access.htm

import getopt
import sys
import Queue
import sqlite3
import urllib
import mechanize
from bs4 import BeautifulSoup

linkQueue = Queue.Queue()
url_list = []
depth = 0

def checkList(url):
	global url_list
	global linkQueue

	if not url in url_list:
		print "not in list"
		url_list.append(url)
		linkQueue.put(url)
	else:
		print "in list"	

def webspider(url, depth):
	global url_list
	global linkQueue

	inFile = open("html.txt", 'wb')

	br = mechanize.Browser()
	br.open(url)

	html = br.response().read() 
	soup = BeautifulSoup(html)

#	for link in soup.find_all('a'):
#		print link
#		if ".html" in link['href'] and link['base url'] == url:
#			inFile.write(url + ' : ' + link['href'] + ' : ' + str(depth) + '\n')

	for link in br.links():
#		print link
		if ".html" in link.url: #and link.base_url == url:
#			url2 = link.base_url + link.url
			checkList(link.url)
#			inFile.write(link.text + ' : ' + link.url + ' : ' + str(depth) + '\n')
	print url_list
	
	while not linkQueue.empty():
		z = linkQueue.get()
		print z

	for form in br.forms():
#		print form
		inFile.write(str(form) + '\n')

def check_url(url):
	httpResponse = urllib.urlopen(url)

	if httpResponse.code == 200:
		return 1
	else:
		return 0

def usage():
        print "Webspider"
        print
        print "Usage: " + sys.argv[0] + " -u http://www.test.com -d 3"
        print "-u --url		- listen on [host]:[port] for incoming connections"
        print "-d --depth =		- execute the given file upon receiving a connection"
        print
        print
        print "Examples: "
        sys.exit(0)

def main():
	global depth

	# execute usage if no arguments provided
        if not len(sys.argv[1:]):
                usage()

        # read the commandline options
        try:
                # parses all command line arguments into lists starting at position 1 and store in opts
		# options that require an argument should be followed by a colon (:)
                opts, args = getopt.getopt(sys.argv[1:], "hu:d:", ["help", "url", "depth"])
        except getopt.GetoptError as err:
                print str(err)
                usage()

        for o, a in opts:
                if o in ("-h", "--help"):
                        usage()
                elif o in ("-u", "--url"):
                        url = a
                elif o in ("-d", "--depth"):
                        depth = int(a)
                else:
			assert False, "Unhandled Option"

	if check_url(url):
		while depth > 0:
			print depth
			webspider(url, depth)
			depth -= 1
			print depth

if __name__ == "__main__":
	main()
