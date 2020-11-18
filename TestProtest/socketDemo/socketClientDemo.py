
import socket

 

p = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

p.connect(('127.0.0.1',8080))

while 1:

    msg = input('please input')

    # 防止输入空消息

    if not msg:

        continue

    p.send(msg.encode('utf-8'))  # 收发消息一定要二进制，记得编码
    

p.close()
