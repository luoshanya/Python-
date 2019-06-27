#两种方法来使用多线程编程
import time
import threading

# def main_thread():
#     print('第一个线程')
#     time.sleep(2)
#     print('第二个线程')
#
# def main_thread_01():
#     print('第三个线程')
#     time.sleep(4)
#     print('第四个线程')
#
# if __name__ == '__main__':
#     # 传参使用args =
#     t1 = threading.Thread(target=main_thread)
#     t2 = threading.Thread(target=main_thread_01)
#     old_time = time.time()
#     t1.start()
#     t2.start()
#     # 等待线程跑完才往下走join()
#     t1.join()
#     t2.join()
#     print('time {}'.format(time.time() - old_time))
#

# 第二个方法 继承threading
class GetThread(threading.Thread):
    # 调用父类
    def __init__(self, name):
        return super().__init__(name=name)

    def run(self):
        print('第一个线程')
        time.sleep(2)
        print('第二个线程')

class GetThread_01(threading.Thread):
    # 调用父类
    def __init__(self, name):
        return super().__init__(name=name)

    # 线程一定需要把函数名改为run 不然直接调用父类不会运行函数
    def run(self):
        print('第三个线程')
        time.sleep(4)
        print('第四个线程')

if __name__ == '__main__':
    t1 = GetThread('猪')
    t2 = GetThread_01('呀')
    old_time = time.time()
    t1.start()
    t2.start()
    # 等待线程跑完才往下走join()
    t1.join()
    t2.join()
    print('time {}'.format(time.time() - old_time))