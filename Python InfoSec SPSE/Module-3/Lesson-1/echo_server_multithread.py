#!/usr/bin/python

import socket
import threading

class serverThread(threading.Thread):

	def __init__(self, conn, address):
		threading.Thread.__init__(self)
		self.conn = conn
		self.address = address

	def run(self):
		data = 'dummy'

		while len(data):
		        data = self.conn.recv(2048)
			print repr(data)
			if data.strip() == 'quit':
				print '\n[-] client IP: ' + str(self.address[0]) + ' closing connection ....'
				self.conn.close()
				
				# how does it know to close this socket when it is not passed to the class???		
				print '[-] client IP: ' + str(self.address[0]) + ' shutting down server ....'
				tcpSocket.close()

				print '[-] ' + str(threading.currentThread()) + ' terminated ....'
				print '[+] threads remaining: ' + str(threading.enumerate())
				
				# kept recieving an error unless I added this break
				break
			else:
		        	print 'Thread: ' + str(threading.currentThread())
				print '\tClient Hostname: ' + str(socket.gethostname())
				print '\tClient IP: ' + str(self.address[0])
				print '\tClient Port: ' + str(self.address[1])
				print '\tSent:', data

			        self.conn.send(data)


i = 0

print "[+] booting multithreaded echo server"

while True:
	tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	tcpSocket.bind(('0.0.0.0', 8000))

	tcpSocket.listen(i)

	(conn, address) = tcpSocket.accept()

	multiEcho = serverThread(conn, address)
	multiEcho.setDaemon(True)
	multiEcho.start()

	i += 1
