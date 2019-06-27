import threading
from threading import Condition,Lock

class  XiaoAi_Robot(threading.Thread):
    def __init__(self, con):
        super().__init__(name='小爱')
        # self.lock = lock
        self.con = con

    def run(self) -> None:
        with self.con:
            # self.lock.acquire()
            self.con.wait()
            print('%s : 在吗?' % self.name)
            self.con.notify()
            # self.lock.release()
            self.con.wait()
            print('%s : 那你困吗？' % self.name)
            self.con.notify()

class TM_Robot(threading.Thread):
    def __init__(self, con):
        super().__init__(name='天猫精灵')
        self.con = con

    def run(self) -> None:
        # with加锁操作
        with self.con:
            self.con.notify()
            self.con.wait()
            print('%s : 在呀!' % self.name)

            self.con.notify()
            self.con.wait()
            print('%s : 不困，咋滴？' % self.name)


if __name__ == '__main__':
    lock = Lock()
    # 使用condition方法 必须使用with方法 注意打印输出框 如果一直存在那么就是wait和notify用反了
    con = Condition()
    t1 = XiaoAi_Robot(con)
    t2 = TM_Robot(con)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
