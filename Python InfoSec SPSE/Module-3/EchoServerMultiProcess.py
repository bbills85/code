#!/usr/bin/env python

import socket
import multiprocessing 

def echoServer(client, (ip, port)):
    print "Received connection from %s:%s" % (ip, port)

    # Send data to the socket from the client
    # man recv(2) for flags
    # returns the number of bytes sent
    # socket.send(string[, flags])
    client.send("Welcome to the ECHO server!\n")

    # dummy variable to make while loop true
    data = 'dummy'

    # loop until data is empty
    while len(data):
        # Receive data from the socket
        # Return is pair (string, address)
        # man recv(2) for flags
        # bufsize is the maximum amount of data to be received
        # socket.recv(bufsize[, flags])
        data = client.recv(2048).strip('\n')

        print "Client %s:%s sent: %s" % (ip, port, data)

        # same as above
        client.send("ECHO: " + data + '\n')

    print "Client %s:%s disconnected ...." % (ip, port)

    # closes the client connection, same concept as socket.close()
    client.close()

def main():
    # Create a socket named tcpSocket
    # $ man socket for more information
    # AF_INET = Address Family Internet (default)
    # SOCK_STREAM = Connection oriented TCP protocol (default)
    # protocol number may be omitted (0 is default)
    # s = socket.socket(socket_family, socket_type, protocol = 0)
    # tcpSocket = socket.socket() (this is the same as below)
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # When server crashes, can reuse port immediately
    # $ man setsockopt for more information
    # $ man socket section socket(7) for more information
    # SOL_SOCKET = manipulate options at the sockets API level
    # SO_REUSEADDR = tells the kernel to reuse a local socket in
    #     TIME_WAIT state (without waiting for its natural timeout to expire)
    # s = socket.setsockopt(level, optname, value)
    tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Binds the socket to the address
    # 'address' depends on family aka AF_INET (tuple - address, port)
    # socket.bind(address) 
    tcpSocket.bind(("0.0.0.0", 8000))

    # Listens for connections made to socket
    # backlog specifies the max number of queued connections (min 0/max 5)
    # socket.listen(backlog)
    tcpSocket.listen(1)

    print "Waiting for a Clients ...."

    for i in range(2):
        # Accepts a connection, returns tuple (conn, address)
        # conn = new socket object
        # address = ip/port bound to socket on the other end of the connection
        # socket.accept()
        (client, (ip, port)) = tcpSocket.accept()

        # Create a process with target function echoServer and args as a tuple
        # Process class has all the equivalents of all the methods of
        #     threading.Thread
        # group always is None; exisit for threading.Thread compatibility
        # target is the callable object inviked by the run() method
        # name is the process name
        # args is args in tuple form for target invocation
        # kwargs is a dictionary of keywords arguments for target invocation
        # If a subclass overrides the constructor, must invoke the base class
        #     Process.__init__()
        # multiprocessing.Process(group = None, target = None, name = None,
        #     args = (), kwargs = {})
        connectionProcess = multiprocessing.Process(target = echoServer,\
            args = (client, (ip, port)))

        # Start the process activity; arranges for the object's run() method
        #     to be invoked in a separate proces
        connectionProcess.start()

    # Block calling threadc until the process whose join() method is called
    #     terminates
    # join([timeout])
    connectionProcess.join()

    print "Shutting down the ECHO server ...."

    # Close the socket
    # socket.close()
    tcpSocket.close()

if __name__ == '__main__':
    main()
