#!/usr/bin/python

# import the following modules
import threading
import Queue
import time
import sys
from ftplib import FTP

# opens file listed in the first argument and stores it in ftpFile
ftpFile = open(sys.argv[1])
# reads the file and splits it at every \n storing it in ftpList
ftpList = (ftpFile.read()).split('\n')
# removes the final \n as it is not needed
ftpList.pop()

# prints list for debugging purposes
print ftpList, '\n'

# class named WorkerThread which takes in the class threading.Thread as a parameter
class WorkerThread(threading.Thread):

	# initilization function which takes in self and queue as parameters
	def __init__(self, queue):
		# ???????????????????????????????????
		threading.Thread.__init__(self)
		# creates a variable queue from queue inside the class
		self.queue = queue

	def run(self):
		# debugging purposes
		print "In WorkerThread"
		# execute this statement
		while True:
			# create a variable named counter, which stores the first item in the queue (FIFO)
			counter = self.queue.get()

			# delayed 2 seconds
#			time.sleep(2)
			
			# error checking with try, except
			try:
				# stores the FTP site from the list ftpList based on the counter number
				ftp = FTP(ftpList[counter])
				# login to FTP site anonymously
				ftp.login()
				# sets ftp to passive (easier for some ftp sites)
				ftp.set_pasv(True)
				# displays print statement with ftp site based off ftpList and counter
                        	print "[+] listing the root directory for %s" % ftpList[counter]
				# displays the current directory
				ftp.retrlines('LIST')
				# displayed finsihed statement
        	                print "[+] finished lisiting the root directory for %s" % ftpList[counter]
				ftp.quit()
				# quits the ftp site
			except:
				# if any of the above fails print the statement below
				print "[-] error unsuccessful login attempt for %s" % ftpList[counter]

			# delayed 2 seconds
			time.sleep(counter)
			
			# indicates a task is completed from the queue
			self.queue.task_done()

# creates a queue called queue that acts in FIFO
queue = Queue.Queue()

# for loop to be executed 5 times creating 5 different threads
for i in range(5):
	# for debugging purposes 
	print "Inside the Thread creation loop: %d time" % (i + 1)
	# created an instance called ftpThread from WorkerThread passing in the parameter queue
	ftpThread = WorkerThread(queue)
	# sets ftpThread to a Daemon Thread, which means when the program ends these threads stop automatically	
	ftpThread.setDaemon(True)
	# starts the run function in the class WorkerThread, aka starts the Threads activiity 
	ftpThread.start()
	# for debugging purposes shows the creation of each thread 1-5
	print "FTP Thread %d Created!" % (i + 1)

# for loop placing the number 0 - 9 (10 items) into the queue
for j in range(10):
	queue.put(j)

# blocks anything from being added to queue until all items currently in the queue (10 items) are processed
queue.join()

# prints final statement once the program is completed
print "[+] %s execution completed" % sys.argv[0]
