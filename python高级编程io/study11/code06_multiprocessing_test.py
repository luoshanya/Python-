import multiprocessing

# 多进程
def test():
    for  i in range(20):
        print('第%s个进程' % i)

if __name__ == '__main__':
    # 多进程
    # test_data = multiprocessing.Process(target=test)
    # test_data.start()
    # test_data.join()
    #线程池  multiprocessing.cpu_count()cpu最大数量
    test_pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # 传函数 需要多一步
    result = test_pool.apply_async(test)
    # 这个方法必须要写close()
    test_pool.close()
    test_pool.join()
    print(result.get())
