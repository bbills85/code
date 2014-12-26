#!/usr/bin/python

import os, signal, time
import threading
from scapy.all import *

unique = []

class wifiSniff(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		
	def run(self):
		print "[+] initializing wifi sniffer ...."
		time.sleep(2)
		sniff(iface = "wlan0", prn = wifi)
			
def channel_hop():

	i = 1

	time.sleep(1)

	while True:
		if i is 15:
			i = 1
		else:
			channel = i
			print "[+] checking channel %d ...." % channel
			os.system("iwconfig wlan0 channel %d" % i)
			i += 1
			time.sleep(5)
		
def wifi(pkt):

	if pkt.haslayer(Dot11Beacon):

		addr = pkt.addr3
			
		if addr not in unique:
			unique.append(pkt.addr3)
			print '\t\tBSSID: ' + str(pkt.addr3).upper()
			if str(pkt.info) is '':
				print "\t\tSSID:    ***HIDDEN***"
			else:
				print '\t\tSSID: ' + pkt.info

def ctrlc_handler(signum, frm):

	print "[-] shutting down wifi sniffer ...."
	sys.exit()

signal.signal(signal.SIGINT, ctrlc_handler)

thread1 = wifiSniff()
thread1.setDaemon(True)
thread1.start()

channel_hop()

while True:
	pass

