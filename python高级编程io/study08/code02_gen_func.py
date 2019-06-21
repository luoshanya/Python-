def yield_data():
    # 这里不同return 后面还是可以添加yield
    yield 1
    yield 1

def return_data():
    return 1

#斐波拉契 0 1 1 2 3 5..三种方法实现
def fei_ddq_data(data):
    if data == 0:
        return data
    elif data <= 2 and data > 0:
        return 1
    else:
        return fei_ddq_data(data - 1) + fei_ddq_data(data - 2)

def fei_gen_data(index):
    list_data = []
    if index == 0:
        return 0
    elif index <= 2 and index > 0:
        return 1
    else:
        a, b, c = 1, 0, 0
        while c <= index:
            list_data.append(b)
            a, b = b, a + b
            c += 1
        return list_data[index - 1]

def yield_fei_data(index):
    if index == 0:
        yield index
    elif index <= 2 and index > 0:
        yield 1
    else:
        a, b, c = 1, 0, 0
        while c <= index:
            yield b
            a, b = b, a + b
            c += 1

if __name__ == "__main__":
    # return 与yield的区别
    # print(yield_data())
    # print(return_data())

    # print(fei_ddq_data(60))
    # print(fei_gen_data(80))
    data = 2
    print([i for i in yield_fei_data(data)])
    # print([i for i in yield_fei_data(data)][data-1])