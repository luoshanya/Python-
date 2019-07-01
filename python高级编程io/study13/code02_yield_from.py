from itertools import chain

# my_list = [1, 2, 3, 4]
# my_dict = {
#     'hello' : '朱',
#     'hello2' : '科',
#     'hi' : '霖'
# }
#
# # yield from 后面加iterable对象
# def gen_for(*args, **kwargs):
#     for i in args:
#         yield from i#省略下面的步骤
#         # for value in i:
#         #     yield value
#
# for value in gen_for(my_list, my_dict, range(10)):
#     print(value)

# 分清楚yield 和yield
def yield_test(iterable):
    yield iterable

def yield_from(iterable):
    yield from iterable

for value in yield_test(range(10)):
    print(type(value))

for value in yield_from(range(10)):
    print(type(value))