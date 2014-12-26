#!/usr/bin/python

import socket
import thread

def multiThread(client, address):
	while True:
		data = client.recv(2048)
		if data:
			client.send(data)
		else:
			client.close()
			return

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('0.0.0.0', 8000))
serverSocket.listen(5)

while True:
	client, address = serverSocket.accept()
	print "[+] creating a new thread ...."
	thread.start_new_thread(multiThread, (client, address))
