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
import threading
from bs4 import BeautifulSoup
import timeit

#threadLock = threading.Lock()

class webSpider(threading.Thread):
	"""class that instantiates a thread"""
	def __init__(self, linkQueue, linkDepth, masterList, i):
		# call the parent class init???????????????
		threading.Thread.__init__(self)
		# store the passed in variables into the class variables
		self.linkQueue = linkQueue
		self.linkDepth = linkDepth
		self.masterList = masterList
		self.thread = i

	def run(self):
		while True:
			url, depth = self.linkQueue.get()
			if depth <= self.linkDepth:
				print "THREADAAAAAAAAAAAAAAAAA: " + str(self.thread)
				print "LINK DEPTH: " + str(self.linkDepth)
				print "CURRENT DEPTH: " + str(depth)
				print "CURRENT URL: "+ url
				print "AT DEPTH: " + str(depth)
				# erorr check login to ftp site
#				try:
				print "[DEBUG] **run()** - Now visiting URL: " + url
				current_link_list = self.findLinks(url)
				print "CUURENT LINK LIST:"
				print current_link_list
				self.checkList(current_link_list, depth + 1)
			else:
				self.linkQueue.task_done()
				continue
			
				print "MASTER LIST"
				print self.masterList
	
			self.linkQueue.task_done()
		print "\n\nCLEANING UP!"
		while not self.linkQueue.empty():
			url, depth = self.linkQueue.get()
			print url
			print depth
			self.linkQueue.task_done()
	

	def checkList(self, links, current_depth):
		for link in links:
			if link in self.masterList:
				print "[DEBUG] **checkList** - URL already in list: " + link
			else:
				print "[DEBUG] **checkList** - Add URL: " + link + " and depth: " + str(current_depth)
#				threadLock.acquire()
				self.masterList.append(link)
				self.linkQueue.put((link, current_depth))
#				threadLock.release()

	def findLinks(self, url):
        	links = []
	        print "[DEBUG] **findLinks()** - Current URL: " + url

	        #if self.check_url(url):
	        if self.check_url(url) == 200:

			'''
			html = urllib.urlopen(url)
			soup = BeautifulSoup(html.read())

			for link in soup.findAll('a'):
				if '.html' in link['href']:
					print "[DEBUG] **findLinks()** - Discovered URL: " + link['href']
                                        links.append(link['href'])
			'''
			br = mechanize.Browser()
			br.open(url)

			for link in br.links():
#				if link.url.endswith('html'):
				if 'html' in link.url:
#					threadLock.acquire()
					print "[DEBUG] **findLinks()** - Discovered URL: " + mechanize.urljoin(url, link.url)
					links.append(mechanize.urljoin(url, link.url))
#					threadLock.release()
			
			return links
                else:
                        print "[DEBUG] **findLinks()** HTTP Code Error - Goodbye"
                        return links


	def check_url(self, url):
		try:
			br = mechanize.Browser()
                        br.open(url)

#	        	httpResponse = urllib2.urlopen(req)

#			z = httpResponse.code
#			print "[DEBUG] **checkURL()** HTTP code: " + str(z)

			#if httpResponse.code == 200: return True #return httpResponse.code
#			return httpResponse.code
			return 200
		except:
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
	start = timeit.default_timer()

	linkQueue = Queue.Queue()
	masterList = []

	depth = 0

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

	print "[DEBUG] **main()** - Starting depth: " + str(depth)

	linkQueue.put((url, 0))

	for i in range(5):
		print "[+] Creating Thread: %d ..." % i
#		# calls the class ftpLogin sending the Queue and number range
		workerThread = webSpider(linkQueue, depth, masterList, i)
		# sets Daemon to True; when main thread terminates
		# all threads terminate
		workerThread.setDaemon(True)
		# start thread
		workerThread.start()
		print "[+] Thread %d created ..." % i

	# waits until all items in the Queue have been
	# processed (related to *.taskdone())
	
	linkQueue.join()

	print "DONE"
	print masterList
	stop = timeit.default_timer()
	print stop - start
if __name__ == "__main__":
	main()
