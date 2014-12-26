#!/usr/bin/python

from scapy.all import *

def postHTTP(pkt):
#	print pkt.summary()

	if pkt.haslayer(Raw):
		print pkt.getlayer(Raw).load

#		a = pkt.getlayer(Raw).load
#		a = a.split(' ')
#		print a

#		if a[0] == 'GET':
#			print pkt.getlayer(Raw).load

#		print pkt.show()
		
sniff(iface = "eth0", filter = "tcp port 80", count = 30, prn = postHTTP)
