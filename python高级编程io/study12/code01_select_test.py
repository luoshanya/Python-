#requests -> urlib -> socket
import socket
from urllib.parse import urlparse

def parse_url(url):
    # 通过socket来请求html
    url_parse = urlparse(url)
    # 取ip
    host = url_parse.netloc
    path = url_parse.path
    if path == '':
        path = '/'
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    #非阻塞请求 所以第一次连接会出错，所以必须try
    try:
        # 不可以使用8000端口 要使用80
        client.connect((host, 80))
    except BlockingIOError as e:
        pass
    while True:
        try:
            # 设置HTTP请求头
            client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf-8'))
            break
        except OSError as e:
            pass

    #因为不知道返回参数的大小
    data = b''
    while True:
        # 这里也需要try
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break
    # 因为传过来的是字节 需转换
    data = data.decode('utf-8').split('\r\n\r\n')[1]
    print(data)
    # 每次运行完都要关闭资源
    client.close()

if __name__ == '__main__':
    parse_url('https://www.baidu.com')