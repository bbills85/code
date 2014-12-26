#!/usr/bin/python

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawSocket.bind(("eth0", socket.htons(0x0800)))

eth_hdr = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x06')

arp_hdr = struct.pack("!2s2s1s1s2s6s4s6s4s", '\x00\x01', '\x08\x00', '\x06', '\x04', '\x00\x01', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x01\x01\x01\x01', '\xaa\xaa\xaa\xaa\xaa\xaa', '\x02\x02\x02\x02')

packet = eth_hdr + arp_hdr

rawSocket.send(packet)

rawSocket.close()
