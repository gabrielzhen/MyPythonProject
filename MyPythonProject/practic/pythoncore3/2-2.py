from socket import *
from time import ctime
host='localhost'
port=18888
bufsize=1024
addr=(host,port)

tcpSerSocket=socket(AF_INET,SOCK_STREAM)
tcpSerSocket.bind(addr)
tcpSerSocket.listen(9)
try:
    while True:
        print('waitting for connection...')
        tcpCliSock,caddr=tcpSerSocket.accept()
        print('...connected from:',caddr)
        while True:
            data=tcpCliSock.recv(bufsize)
            if not data:
                break
            aa='%s...%s'%(ctime(),data)
            tcpCliSock.send(aa.encode())
        tcpCliSock.close()
except KeyboardInterrupt:
    tcpSerSocket.close()