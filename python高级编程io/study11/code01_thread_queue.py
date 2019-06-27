import time
import threading

# 设置一个全局变量，来抓取url
url_list = []
def crawl_detail(url_list):
    # global url_list
    while True:
        if len(url_list):
            url = url_list.pop()
            print('第一个线程')
            time.sleep(2)
            print('第二个线程')

def crawl_url(url_list):
    print(url_list)
    # global url_list
    while True:
        print('第三个线程')
        for i in range(20):
            url_list.append('https://www.baidu.com/%s' % i)
        print('第四个线程')

if __name__ == '__main__':
    for i in range(5):
        # 线程args传列表需要加()和后面的,不然报错
        t1 = threading.Thread(target=crawl_detail, args=(url_list,))
        t2 = threading.Thread(target=crawl_url,  args=(url_list,))
        t1.start()
        t2.start()
    print(url_list)
