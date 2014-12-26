#!/usr/bin/python

import optparse
import threading
import time
from ftplib import FTP

threadLock = threading.Lock()

class ftpLogin(threading.Thread):
    """class that instantiates a thread"""
    def __init__(self, ftpSites, threadID):
        # call the parent class init???????????????
        threading.Thread.__init__(self)
        # store the passed in variables into the class variables
        self.ftpSites = ftpSites
        self.threadID = threadID

    def run(self):
        """function that attempts to login to an ftp site"""
#        while not len(self.ftpSites) == 0:
        while len(self.ftpSites) > 0:
            time.sleep(5)
            threadLock.acquire()
            # erorr check login to ftp site
            try:
                ftpSite = self.ftpSites.pop()
                print "Thread: %d attempting to log into: %s"\
                    % (self.threadID, ftpSite)
                # connect to ftp site
                ftp = FTP(ftpSite)
                # attempt login
                ftp.login()
                print "Thread %d successfully logged into: %s"\
                     % (self.threadID, ftpSite)
                ftp.set_pasv(True)
                ftp.retrlines('LIST')
# used for debuggind purposes       
#                print "Thread: %d has size %d" % (self.threadID, len(self.ftpSites))
                threadLock.release()
                time.sleep(5)
            except:
                print "[-] error could not connect: %s" %ftpSite
                threadLock.release()

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

    print "[+] beginning execution ..."
    # for loop creating 5 Threads
    for i in range(5):
        print "[+] Creating Thread: %d ..." % i
        # calls the class ftpLogin sending the Queue and number range
        workerThread = ftpLogin(ftpSites, i)
        # do not set Daemon to True; 
        # program does not terminate when main ends
#        workerThread.setDaemon(True)
        # start thread
        workerThread.start()
        print "[+] Thread %d created ..." % i

    print "[+] execution complete ..."

if __name__ == '__main__':
    main()
