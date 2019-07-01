def func():
    try:
        html = yield 'html'
        print(html)
    except Exception as e:
        pass
    yield 1
    yield 2
    return 'end'


if __name__ == '__main__':
    fun = func()
    # gen = next(fun)
    # gen_send = fun.send(None)
    # fun.close()
    print(next(fun))
    fun.throw(Exception, 'download,error')
