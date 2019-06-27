import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    # 不写就填写
    re_data = input()
    # 发送
    client.send(re_data.encode('utf8'))
    # 接收 与服务端相反
    data = client.recv(1024)
    print(data.decode('utf8'))