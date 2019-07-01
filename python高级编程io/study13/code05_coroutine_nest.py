import asyncio

async def get_html(sleep_time):
    print('waiting')
    await asyncio.sleep(sleep_time)
    print('waiting')

if __name__ == '__main__':
    task = get_html(1)
    task1 = get_html(2)
    task3 = get_html(3)
    tasks = [task, task1, task3]
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(tasks))

    # 取消任务
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_task = asyncio.Task.all_tasks()
        for task in all_task:
            print('cancel task')
            # 取消任务
            print(task.cancel())
        loop.stop()
        # 取消必须写这一个run_forever
        loop.run_forever()
    finally:
        loop.close()