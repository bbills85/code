#!/usr/bin/python

import socket
import struct
import binascii
from sys import argv

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

while True:
	pkt = rawSocket.recvfrom(2048)

	tcpHeader = pkt[0][34:54]

	tcp_hdr = struct.unpack("!HHLLBBHHH", tcpHeader)

	if str(tcp_hdr[0]) == argv[1] or str(tcp_hdr[1]) == argv[1]:
		print "\n\nTCP Header Parsed:\n\n"
		print "\tSource Port: " + str(tcp_hdr[0])
		print "\tDestination Port: " + str(tcp_hdr[1])
		print "\tSequence Number: " + str(tcp_hdr[2])
		print "\tAcknowledgment Number: " + str(tcp_hdr[3])
		print "\tData Offset: " + str(tcp_hdr[4])
		print "\tFlags: " + str(tcp_hdr[5])
		print "\tWindow: " + str(tcp_hdr[6])
		print "\tChecksum: " + str(tcp_hdr[7])
		print "\tUrgent Pointer: " + str(tcp_hdr[8])
	else:
		print " .... " + str(tcp_hdr[0])
