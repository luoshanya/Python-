class User_name():
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        return MyInterator(self.name)

    def __getitem__(self, item):
        # print(item)
        return self.name[item]

class MyInterator():
    def __init__(self, name):
        self.name = name
        self.index = 0

    def __next__(self):
        try:
            word = self.name[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word



if __name__ == '__main__':
    user = User_name(['a', 'c', 'd'])
    # users = iter(user)
    # while True:
    #     try:
    #         print(next(users))
    #     except StopIteration:
    #         pass
    # users = iter(user)
    for i in user:
        print(i)
