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


#框架的概念   就是有助于减轻网页开发时共通性活动的工作（重复的），比如数据库访问接口
