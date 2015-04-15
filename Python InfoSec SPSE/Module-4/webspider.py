#!/usr/bin/python

########################################################################################################
# Webspider Program
# Date: 15 April 2015
# Author: bbills85
# Version: 1
# Tested with: Python 2.7.6 on Ubuntu 14.04.2 LTS
########################################################################################################
# References:
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
# http://pymotw.com/2/getopt/
# http://stackoverflow.com/questions/15993238/python-invalid-literal-for-int-base-10
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# http://palewi.re/posts/2008/04/20/python-recipe-grab-a-page-scrape-a-table-download-a-file/
# http://stackoverflow.com/questions/15956597/beautifulsoup-parsing-and-writing-the-data-in-a-text-file
# http://www.tutorialspoint.com/python/python_files_io.htm
# http://www.tutorialspoint.com/python/python_database_access.htm
# https://docs.python.org/2/library/argparse.html
# http://pymotw.com/2/argparse/
########################################################################################################

import argparse
import Queue
import urllib
import mechanize
import threading
from bs4 import BeautifulSoup
import MySQLdb
import timeit

threadLock = threading.Lock()

class webSpider(threading.Thread):
	"""class that instantiates a thread"""
	def __init__(self, linkQueue, linkDepth, masterList, thread):
		# call the parent class init???????????????
		threading.Thread.__init__(self)
		# store the passed in variables into the class variables
		self.linkQueue = linkQueue
		self.linkDepth = linkDepth
		self.masterList = masterList
		self.thread = thread

	def run(self):
		while not self.linkQueue.empty():
			url, depth = self.linkQueue.get()
			try:
				if depth <= self.linkDepth:
					print "[DEBUG] **run()** - Thread: %d" % int(self.thread + 1)
					print "[DEBUG] **run()** - Current URL: "+ url
					print "[DEBUG] **run()** - Current Depth: " + str(depth)

					current_link_list = self.findLinks(url)

					print "[DEBUG] **run()** - Current Link List:"
					print current_link_list

					self.checkList(current_link_list, depth + 1)
				else:
					self.linkQueue.task_done()
					continue
			
			except:
		                self.linkQueue.task_done()
				continue
			try:
 	              		# connect to db and insert site
				#current_form_list = self.findForms(self.masterList)
				(formName, formInput, formAttrs) = self.findForms(self.masterList)
				print formName
				print formInput
				print formAttrs

				print "[DEBUG] **run()** - Current Form List:"
				print current_form_list
            		except:
                		print "can not insert url: {0} into database".format(url)
            		finally:
				print "[DEBUG] **run()** - Generating SQL DB"
				self.addSQL(self.masterList)
				self.linkQueue.task_done()
#					return 
	
	def addSQL(self, masterList):
		# Open database connection
		db = MySQLdb.connect("localhost","wsinkey","","testdb" )

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		# Drop table if it already exist using execute() method.
		cursor.execute("DROP TABLE IF EXISTS LINKS")

		# Create table as per requirement
		sql = """CREATE TABLE LINKS (Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(1000))"""
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
				print "[DEBUG] **checkList** - Add URL: " + link + " at depth: " + str(current_depth)
#				threadLock.acquire()
				self.masterList.append(link)
				self.linkQueue.put((link, current_depth))
#				threadLock.release()

	def findForms(self, masterList):
		forms = []

		for link in masterList:
			print "[DEBUG] **findForms** - Current URL to Search for Forms: " + str(link)

			html = urllib.urlopen(link).read()
			soup = BeautifulSoup(html)

			forms = soup.find_all('form')

			for form in forms:
				inputs = form.find_all('input')
				for input in inputs:
					formName = form.name
					formInput = input
					formAttrs = input.attrs
		
		return (formName, formInput, formAttrs)

	def findLinks(self, url):
        	links = []
	        print "[DEBUG] **findLinks()** - Current URL: " + url

	        if self.check_url(url) == 200:
			br = mechanize.Browser()
			br.open(url)

			for link in br.links():
				if 'html' in link.url:
#					threadLock.acquire()
					print "[DEBUG] **findLinks()** - Discovered URL: " + mechanize.urljoin(url, link.url)
					links.append(mechanize.urljoin(url, link.url))
#					threadLock.release()
					
			
			return links
                else:
                        print "[DEBUG] **findLinks()** HTTP Code Error URL not recorded"

                        return links


	def check_url(self, url):
		try:
			br = mechanize.Browser()
                        br.open(url)

			return 200
		except:
			return 0

def main():
	start = timeit.default_timer()

	linkQueue = Queue.Queue()
	masterList = []

	parser = argparse.ArgumentParser(description =
					 'Webspider for links and form data')
	parser.add_argument('-u', '--url', required = True, dest = 'url',
			    action = 'store', metavar = 'http://www.google.com',
			    help = 'base url to web spider')
	parser.add_argument('-d', '--depth', required = False, dest = 'depth',
			    action = 'store', metavar = '3', default = 0, type = int,
			    help = 'depth for web spider')
	parser.add_argument('-t', '--threads', required = False, dest = 'threads',
			    action = 'store', metavar = '5', default = 1, type = int,
			    help = 'number of threads')
	parser.add_argument('--version', action = 'version', version = '%(prog)s 1.0')

	args = parser.parse_args()

	print "[DEBUG] **main()** - Starting Webspider at Depth: " + str(args.depth)

	linkQueue.put((args.url, 0))

	masterList.append(args.url)
	
	for thread in range(args.threads):
		print "[DEBUG] **main()** - Creating Thread: %d" % int(thread + 1)
		# calls the class ftpLogin sending the Queue and number range
		workerThread = webSpider(linkQueue, args.depth, masterList, thread)
		# sets Daemon to True; when main thread terminates
		# all threads terminate
		workerThread.setDaemon(True)
		# start thread
		workerThread.start()
		print "[DEBUG] **main()** - Thread %d created" % int(thread + 1)

	# waits until all items in the Queue have been
	# processed (related to *.taskdone())
	linkQueue.join()

	print "[DEBUG] **main()** - Master List"
	print masterList

	stop = timeit.default_timer()
	print "[DEBUG] **main()** Run Time: %.2f seconds" % float(stop - start)
	print "[DEBUG] **main()** - Program Terminated"

if __name__ == "__main__":
	main()
