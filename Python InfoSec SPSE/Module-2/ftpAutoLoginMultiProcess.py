#!/usr/bin/python

import optparse
import multiprocessing
import Queue
import time
from ftplib import FTP

class ftpLogin(multiprocessing.Process):
    """class that instantiates a thread"""
    def __init__(self, ftpQueue, threadID):
        # call the parent class init???????????????
        multiprocessing.Process.__init__(self)
        # store the passed in variables into the class variables
        self.ftpQueue = ftpQueue
        self.threadID = threadID

    def run(self):
        """function that attempts to login to an ftp site"""
        # keeps the thread running until the Queue is empty
        while not self.ftpQueue.empty():
            # get the ftp link into variable from the Queue
            ftpSite = self.ftpQueue.get()
            # erorr check login to ftp site
            try:
                print "Thread: %d attempting to log into: %s"\
                    % (self.threadID, ftpSite)
                # connect to ftp site
#                ftp = FTP(ftpSite)
                # attempt login
#                ftp.login()
                print "Thread %d successfully logged into: %s"\
                     % (self.threadID, ftpSite)
#                ftp.set_pasv(True)
#                ftp.retrlines('LIST')
                time.sleep(3)
            except:
                print "[-] error could not connect: %s" %ftpSite
            # tell the Queue the process was completed (links to *join())
            self.ftpQueue.task_done()

def readFile(fileName):
    """function used to read the input from a file"""
    # create a list variable
    websiteHolder = []
    # open the file in read mode
    inFile = open(fileName)
    # read each line, strip the \n and store it in a list
    for line in inFile.readlines():
        websiteHolder.append(line.strip())
    # return the list
    return websiteHolder

def main():
    """function used to parse and error check user input.  Creates Threads
    and sets up the Queue"""
    # display usage error
    parser = optparse.OptionParser('%prog -f <filename>')
    # adds help for -f input and input name/type
    parser.add_option('-f', dest = 'fileName', type = 'string',\
        help = 'enter the file with ftp sites')
    # unpack the user input; options is a dict args is a list
    # (args contains whatever is written after the option)
    (options, args) = parser.parse_args()
    # stores option into variable (e.g. fileName : test.txt)
    fileName = options.fileName

# used for debugging purpsoes
#    print options
#    print args

    # used to error check user input
    if fileName == None:
        parser.print_help()
        exit(0)
    # call function readFile and return to ftpSites
    ftpSites = readFile(fileName)

# used for debugging purposes
#    print ftpSites

    # create a Queue
    ftpQueue = Queue.Queue()
    # store all the items in the file into the Queue
    for site in ftpSites:
        ftpQueue.put(site)

    print "[+] beginning execution ..."

    multiWorker = multiprocessing.Pool(5)
    p.map(ftpLogin, 
    ftpQueue.join()

    print "[+] execution complete ..."

if __name__ == '__main__':
    main()
