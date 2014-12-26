#!/usr/bin/python

import socket
import struct
import binascii

# /usr/include/linux/if_ether.h for last parameter 0800 = IP
# must be root to create raw_sockets...can do this but do it in another example
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

pkt = rawSocket.recvfrom(2048)

print "\n\nEntire Packet:\n\n", pkt

ethernetHeader = pkt[0][0:14]

#print ethernetHeader

eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)

print "\n\nEnternet Header Cleaned up:\n\n", eth_hdr

print "\nSource MAC: " + binascii.hexlify(eth_hdr[0])
print "Destination MAC: " + binascii.hexlify(eth_hdr[1])
print "Ethernet Type: " + binascii.hexlify(eth_hdr[2])

ipHeader = pkt[0][14:34]

#print ipHeader

ip_hdr = struct.unpack("!12s4s4s", ipHeader)

print "\n\nIP Header Cleaned up:\n\n", ip_hdr

print "\nSource IP Address: " + socket.inet_ntoa(ip_hdr[1])
print "Destination IP Address: " + socket.inet_ntoa(ip_hdr[2])

tcpHeader = pkt[0][34:54]

tcp_hdr = struct.unpack("!HH16s", tcpHeader)

print "\n\nTCP Header Cleaned up:\n\n", tcp_hdr

print "\nSource Port: " + str(tcp_hdr[0])
print "Destination Port: " + str(tcp_hdr[1])
