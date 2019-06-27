#线程安全 使用队列 queue
import time
import threading
from queue import Queue

# 设置一个全局变量，来抓取url
url_list = []
def crawl_detail(queue):
    # global url_list
    # 队列取值使用get()方法 如果队列为空 那么就会进行阻塞状态 一直等待
    while True:
        #取队列的最后一个数据
        url = queue.get()
        print(url)
        print('第一个线程')
        time.sleep(2)
        print('第二个线程')

def crawl_url(queue):
    # global url_list
    while True:
        print('第三个线程')
        time.sleep(1)
        for i in range(20):
            # 向队列插数据使用put
            queue.put('https://www.baidu.com/%s' % i)
        print('第四个线程')

if __name__ == '__main__':
    # 创建队列 设置最大值
    crawl_url_queue = Queue(maxsize=1000)
    for i in range(5):
        # 共享变量queue队列实现  线程通信方式
        # 线程args传列表需要加()和后面的,不然报错
        t1 = threading.Thread(target=crawl_detail, args=(crawl_url_queue,))
        t2 = threading.Thread(target=crawl_url,  args=(crawl_url_queue,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    # 队列退出 不写这两个方法这个队列不会退出
    # 队列使用put时不可以使用task_done方法
    crawl_url_queue.task_done()
    crawl_url_queue.join()
    print(url_list)
