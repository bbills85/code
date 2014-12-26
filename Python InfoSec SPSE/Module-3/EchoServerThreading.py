#!/usr/bin/env python

import socket
import threading

class echoServer(threading.Thread):

    def __init__(self, client, (ip, port)):
        threading.Thread.__init__(self)
        self.client = client
        self.ip = ip
        self.port = port

    def run(self):
        print "Received connection from %s:%s" % (self.ip, self.port)
        self.client.send("Welcome to the ECHO server!\n")

        data = 'dummy'

        while len(data):
            data = self.client.recv(2048).strip('\n')
            print "Client %s:%s sent: %s" % (self.ip, self.port, data)
            self.client.send("ECHO: " + data + '\n')

        print "Client %s:%s disconnected ...." % (self.ip, self.port)   
        self.client.close()

def main():

    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    tcpSocket.bind(("0.0.0.0", 8000))

    for i in range(2):
        print "Waiting for a Client ...."
        tcpSocket.listen(2)
        (client, (ip, port)) = tcpSocket.accept()

        connectionThread = echoServer(client, (ip, port))
        connectionThread.setDaemon(True)
        connectionThread.start()
#need to use queue for join, this works well for a single thread?
    connectionThread.join()

    print "Shutting down the ECHO server ...."
    tcpSocket.close()

if __name__ == '__main__':
    main()
