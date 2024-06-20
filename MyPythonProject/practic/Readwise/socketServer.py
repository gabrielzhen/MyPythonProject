import socket,select

##创建socket对象
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',11111))
server_socket.listen(5)
inputs=[server_socket]

while inputs:
    rs,_,_=select.select(inputs,[],[])
    for r in rs:
        if r is server_socket:
            client_socket,=server_socket.accept()
            inputs.append(client_socket)
        else:
            msg=r.recv(1024)
            if not msg:
                inputs.remove(r)
            else:
                for ss in inputs:
                    if ss is not server_socket:
                        ss.send(msg)
