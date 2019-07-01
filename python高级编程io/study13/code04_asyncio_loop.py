#事件循环+回调（驱动生成器）+epoll(IO多路复用)
#asyncio是python用于解决异步io编程的一整套解决方案
#tornado、gevent、twisted（scrapy， django channels）
#torando(实现web服务器)， django+flask(uwsgi, gunicorn+nginx)
#tornado可以直接部署， nginx+tornado

import asyncio
import time
# 专门解决函数不能调用方法
from functools import partial

async def loop_test(url):
    print('start get url')
    # 必须要加await 不可以写time.sleep()不然不可以并发
    await asyncio.sleep(2)
    print('end get url')
    return 'hello'

# 如何加一个callback
def callback(url, future):
    print(url)
    print('callback')

if __name__ == '__main__':
    start_time = time.time()
    # 协程运行必须要进行事件循环 才可以使用
    loop = asyncio.get_event_loop()
    # 多任务 一个可迭代的对象 这样代表会循环十次
    # task = [loop_test('http://www.baidu.com') for i in range(100) ]
    # 多任务
    # loop.run_until_complete(asyncio.wait(task))#asyncio.wait里面放一个可迭代对象
    # print(time.time() - start_time)

    # 获取return值
    # future对象
    # get_future = asyncio.ensure_future(loop_test('http://www.baidu.com'))
    # loop.run_until_complete(get_future)#可以放future对象
    # print(get_future.result())

    #或者使用task
    # get_task = loop.create_task(loop_test('http://www.baidu.com'))
    # # 如何加一个callback
    # get_task.add_done_callback(partial(callback, 'http://www.baidu.com'))#这里只能放函数名 不能加()
    # loop.run_until_complete(get_task)
    # print(get_task.result())

    #gather和wait的区别
    #gather和high-level
    group1 = [loop_test('http://www.baidu.com') for i in range(10)]
    group2 = [loop_test('http://www.baidu.com') for i in range(10)]
    loop.run_until_complete(asyncio.gather(*group1, *group2))
    print(time.time() - start_time)
