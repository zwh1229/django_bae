import socket

server = socket.socket()
server.bind(('192.168.1.237',8090))
server.listen(5)

while 1:
    conn,addr = server.accept()
    data = conn.recv(1024)  #是一个满足http协议的数据
    print(data)
    request_path = data.decode('utf-8').split('\r\n')
    print(request_path)
    d  =request_path[0].split(' ')
    print(d)


    #大概就是一个流程 有请求 有处理 有响应