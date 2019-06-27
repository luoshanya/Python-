import socket
import threading

# 初始化 配置
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen(5)

def  socket_server(sock, addr):
    while True:
        # 接收
        data = sock.recv(1024)
        print(data.decode('utf8'))
        re_data = input()
        # 发送
        sock.send(re_data.encode('utf8'))
    # server.close()
    # sock.close()
while True:
    sock, addr = server.accept()
    clinet_thread = threading.Thread(target=socket_server, args=(sock, addr))
    clinet_thread.start()
# 获取从客户端发送的数据
# 一次获取1k的数据
