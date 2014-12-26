#!/usr/bin/python

import socket
import select

# creates an AF_INET (IPv4), STREAM socket (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[+] socket created", s.getsockname()

# enable reusing socket addresses
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# binds the socket to this address
# 0.0.0.0 so server is visible to the entire world
s.bind(('0.0.0.0', 8000))
# could not get this to work
#s.bind((socket.gethostname(), 8000))

# allows 5 connections
s.listen(5)

buffer = []

# select returns a tuble of three lists unless three variables declared
# do not need write or execute, so they are just empty lists
while True:
	read, write, execute = select.select([s] + buffer, [], [])
	print "[+] socket value in read: ", read

	for iter in read:
		if iter is s:
			# return conn (connection) and the tuble address (ip, port)
			conn, address = s.accept()
			# print a connect statement on the server
			print "[+] client connected from", address
			# print a welcome message on the client
			conn.send("Welcome to " + socket.gethostname() + "!!!!\n")
			
			buffer.append(conn)
			print read
			print "For Loop Buffer: ", buffer
		else:
			data = conn.recv(2048)
			if data.strip() == 'quit':
				buffer.remove(iter)
				# close the client
				conn.close()
			else:
				conn.send(data)

# close the socket
s.close()
