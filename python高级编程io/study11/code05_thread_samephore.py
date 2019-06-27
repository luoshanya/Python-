import threading
import time

# 爬虫线程实例
class Crawl_Spider(threading.Thread):
    def __init__(self, url, same):
        super().__init__()
        self.url = url
        self.same = same

    def run(self) -> None:
        time.sleep(2)
        print('crawl %s is successful' % self.url)
        #需要在这里释放 才可以限制
        self.same.release()

class Thread_Samephore(threading.Thread):
    def __init__(self, same):
        super().__init__()
        self.same = same

    def run(self) -> None:
        for i in range(20):
            # 控制 类似锁 需要解锁
            self.same.acquire()
            crawl = Crawl_Spider('https://www.baidu.com/{}'.format(i), self.same)
            crawl.start()

if __name__ == '__main__':
    # 控制爬虫的数量 里面写
    spider_mun_limit = threading.Semaphore(3)
    thread_same = Thread_Samephore(spider_mun_limit)
    thread_same.start()