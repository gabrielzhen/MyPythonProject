import socket
c=socket.socket()
c.connect(('localhost',11111))

print(c.recv(1024).decode())
c.close()