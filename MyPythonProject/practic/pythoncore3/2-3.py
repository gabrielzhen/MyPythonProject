#!/usr/bin/env python
from socket import *
from time import ctime

host='localhost'
port=18888
bufsiz=1024
addr=(host,port)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(addr)

while True:
    data=input('>')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data=tcpCliSock.recv(bufsiz)
    if not data:
        break
    print(data)

tcpCliSock.close()