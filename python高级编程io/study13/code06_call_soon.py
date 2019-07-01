import asyncio

def callback(sleep_time):
    print('sleep %s success' % sleep_time)

# 停止run_forever
def stop_loop(loop):
    loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 直接使用callback函数
    loop.call_soon(callback, 2)
    # 停止run_forever
    loop.call_soon(stop_loop, loop)
    loop.run_forever()