#!/usr/bin/python

import Queue
import threading

def workerThread():
    if q.qsize != 0:
        print "doing work with thread %d" %

q = Queue.Queue()

for i in range(5):
    print "Making thread %d" % i
    worker = workerThread(

print q.qsize()
