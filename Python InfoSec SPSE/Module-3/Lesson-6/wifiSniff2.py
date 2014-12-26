#!/usr/bin/python

import random, os
from threading import *
from scapy.all import *
import signal

def ctrlc_handler(signum, frm):
	sys.exit()

screenLock = Semaphore(value=1)

unique = []

def wifi(pkt, channel):
#	print "before"
        os.system("iwconfig wlan0 channel %d" % channel)
#	print "after"
	print channel
        if pkt.haslayer(Dot11Beacon):
                #print pkt.summary()
                #print pkt.show()
                #print pkt.addr3
                addr = pkt.addr3
                if addr not in unique:
			screenLock.acquire()
                        unique.append(pkt.addr3)
                        print pkt.addr3 + ' ' + pkt.info
			screenLock.release()

def channel(p):
#	print p.summary()
	channel = random.randrange(1, 15)
	print channel
	t = Thread(target=wifi, args=(p, channel))
	t.setDaemon(True)
	t.start()
'''        t = Thread(target=wifi, args=(p, channel))
        t.setDaemon(True)
        t.start()'''

signal.signal(signal.SIGINT, ctrlc_handler)
sniff(iface = "wlan0", prn = channel)
