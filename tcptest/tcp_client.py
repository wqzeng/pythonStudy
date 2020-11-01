# @author :xpzhuang
# @date : 2020/11/1

import socket

host='127.0.0.1'
port=8080

c=socket.socket()
c.connect((host,port))
send_data=input('请输入要发送的数据：')
c.send(send_data.encode())
recv_data=c.recv(1024).decode()
print('接收到的数据为：',recv_data)
c.close()