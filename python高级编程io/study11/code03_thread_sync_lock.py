import threading
from threading import Lock

data = 0
# 线程锁
lock = Lock()
def add():
    global data
    global lock
    for i in range(1000000):
        lock.acquire()
        data += 1
        lock.release()

def desc():
    global data
    global lock
    for i in range(1000000):
        lock.acquire()
        data -= 1
        lock.release()

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=desc)
t1.start()
t2.start()
t1.join()
t1.join()
print(data)
# 锁是会死锁的  资源竞争是一种情况