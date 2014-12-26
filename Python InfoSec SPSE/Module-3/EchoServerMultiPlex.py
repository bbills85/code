#!/usr/bin/env python

import socket
import select

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

    data = 'dummy'

    blah = []

    while True:
        r, w, e = select.select([tcpSocket] + blah, [], [])

        for x in r:
            if x is tcpSocket:
                # Accepts a connection, returns tuple (conn, address)
                # conn = new socket object
                # address = ip/port bound to socket on the other end of the connection
                # socket.accept()
                (client, (ip, port)) = tcpSocket.accept()

                print "[+] connected received from {0}:{1}".format(ip, port)

                blah.append(client)

                client.send("Welcome to {}'s ECHO server!\n".format(socket.gethostname()))

            else:
                data = x.recv(2048)
                if data == "exit\n":
                    print "[-] {0}:{1} disconnected ....".format(ip, port)
                    client.send("Goodbye!\n")
                    x.close()
                    blah.remove(x)
                else:
                    print "{0}:{1} sent: {2}".format(ip, port, data.strip())
                    client.send("You just sent " + data.strip() + "!\n")

    print "[-] Shutting down the ECHO server ...."

    # Close the socket
    # socket.close()
    tcpSocket.close()

if __name__ == '__main__':
    main()
