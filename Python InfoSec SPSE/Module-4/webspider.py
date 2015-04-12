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

def findLinks(url):
	links = []
	print "current url: " + url + '\n'
	if check_url(url):
		br = mechanize.Browser()
		br.open(url)

		for link in br.links():
			if ".html" in link.url:
				print "Discovered url: " + mechanize.urljoin(url, link.url)
				links.append(mechanize.urljoin(url, link.url))
	else:
		print "BAD LINK"
		sys.exit(0)
	return links

def checkList(links, current_depth):
	global url_list
	global linkQueue
	print current_depth
	for link in links:
		if not link in url_list:
			print "ADD LINK: " + link
			url_list.append(link)
			linkQueue.put((link, current_depth))

def webspider(url, depth):
	global url_list
	global linkQueue
	
	current_depth = 0;

	linkQueue.put((url, current_depth))

	while current_depth <= depth:
		print current_depth

		url, b = linkQueue.get()
		print "grabbing: " + url + " : Depth: " + str(b)

		links = findLinks(url)
		checkList(links, current_depth + 1)
		print url_list
		while not linkQueue.empty() and current_depth <= depth:
			url, b = linkQueue.get()
			print b
			if b == current_depth:
				print "Visiting: " + url
				links = findLinks(url)
				checkList(links, current_depth + 1)
			else:
				linkQueue.put((url, b))
				current_depth += 1

#		current_depth += 1

	print url_list


def check_url(url):
	httpResponse = urllib.urlopen(url)

	if httpResponse.code == 200:
		print httpResponse.code
		return True
	else:
		return False

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
	global linkQueue

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
	print "depth is: " + str(depth)
	webspider(url, depth)

if __name__ == "__main__":
	main()
