#GIL global interpreter lock(cpython)
# python中一个线程对应c语言中的一个线程
# gil使得同一个时刻只有一个线程在cpu上执行字节码， 无法将多个线程映射到多个CPU上执行
from threading import Thread
# gill在遇到io操作时候会主动释放
# 创建一个全局变量
global_data = 0
def global_data_add():
    global global_data
    for i in range(10000000):
        global_data += 1

def global_data_jian():
    global global_data
    for i in range(10000000):
        global_data -= 1

if __name__ == '__main__':
    t1 = Thread(target=global_data_add)
    t2 = Thread(target=global_data_jian)
    t1.start()
    t2.start()
    print(global_data)