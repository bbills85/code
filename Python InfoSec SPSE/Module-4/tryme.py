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
import MySQLdb
import timeit
import time
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
#		while True:
		while not self.linkQueue.empty():
			url, depth = self.linkQueue.get()
			try:
				if depth <= self.linkDepth:
					print "THREADAAAAAAAAAAAAAAAAA: " + str(self.thread)
					print "LINK DEPTH: " + str(self.linkDepth)
					print "CURRENT DEPTH: " + str(depth)
					print "CURRENT URL: "+ url
					print "AT DEPTH: " + str(depth)
					print "[DEBUG] **run()** - Now visiting URL: " + url
#					current_form_list = self.findForms(url)
					current_link_list = self.findLinks(url)
					print "CUURENT LINK LIST:"
					print current_link_list
					self.checkList(current_link_list, depth + 1)
				else:
					self.linkQueue.task_done()
					continue
			
			except:
		                self.LinkQueue.task_done()
				continue
			try:
 	              		# connect to db and insert site
				self.addSQL(self.masterList)
            		except:
                		print "can not insert url: {0} into database".format(url)
            		finally:
				print "I AM IN FINALLY"
				self.linkQueue.task_done()
#				print "\n\nCLEANING UP!"
#				print threading.current_thread()
#				while not self.linkQueue.empty():
#					url, depth = self.linkQueue.get()
#					print url
#					print depth
#					self.linkQueue.task_done()
#				if self.linkQueue.empty():
#					"THE PROGRAM WILL END!!!!!!"
#					return 
	
	def addSQL(self, masterList):
		# Open database connection
		db = MySQLdb.connect("localhost","wsinkey","","testdb" )

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		# Drop table if it already exist using execute() method.
		cursor.execute("DROP TABLE IF EXISTS LINKS")

		# Create table as per requirement
		sql = """CREATE TABLE LINKS (Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(50))"""
		cursor.execute(sql)
		db.commit()

		for link in masterList:
			sql = """INSERT INTO LINKS (Name) VALUES (%s)"""
			arg = link
			cursor.execute(sql, arg)
			db.commit()


   		cursor.execute("SELECT * FROM LINKS")
		rows = cursor.fetchall()

		for row in rows:
			print row

		# disconnect from server
		db.close()

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

	def findForms(self, url):
		forms = []

	        if self.check_url(url) == 200:
			html = urllib.urlopen(url).read()
			soup = BeautifulSoup(html)

			forms = soup.find_all('form')
			for form in forms:
#				print form
				inputs = form.find_all('input')
				for input in inputs:
					print form.name
					print "  -> %s" % (input.attrs) 

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

	threads = []

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
		threads.append(workerThread)

	# waits until all items in the Queue have been
	# processed (related to *.taskdone())
	linkQueue.join()
#	time.sleep(1)
	print "DONE"
	print masterList
	stop = timeit.default_timer()
	print stop - start
if __name__ == "__main__":
	main()
