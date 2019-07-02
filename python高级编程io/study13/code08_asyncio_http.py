import socket
from urllib.parse import urlparse
import asyncio



async def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    #建立socket连接
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    all_lines = []
    try:
        async for i in reader:
            data = i.decode('utf-8')
            all_lines.append(data)
    except:
        print('====')
    html = '\n'.join(all_lines)
    # print(html)
    return html

# 一步步的返回数据 每return一次
async def main():
    tasks = []
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

if __name__ == '__main__':
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # tasks = []
    # for i in range(20):
    #     url = "http://shop.projectsedu.com/goods/{}/".format(i)
    #     # 必须调用函数
    #     # tasks.append(get_url(url))
    #     tasks.append(asyncio.ensure_future(get_url(url)))
    # loop.run_until_complete(asyncio.wait(tasks))
    # for task in tasks:
    #     # 获取return值
    #     print(task.result())
    print(time.time() - start_time)