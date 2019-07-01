#python为了将语义变得更加明确，就引入了async和await关键词英语定义原生的协程
async def download(url):
    return 'hello'

# async def download_url(url):
#     html = await download(url)
#     return html

async def download_url(url):
    html = await test(url)
    return html
 
# 使用types装饰器来
import types

@types.coroutine
def test(url):
    yield 'abc'

if __name__ == '__main__':
    download_data = download('http://www.baidu.com')
    try:
        download_data.send(None)
    except StopIteration as e:
        print(e)