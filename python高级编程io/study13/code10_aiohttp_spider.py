import asyncio
import aiohttp
from pyquery import PyQuery
import aiomysql
import re

stopping = False
start_url = 'http://www.jobbole.com/'
# 通信 可以用管道等
waitting_urls = []
#去重
seen_urls = set()

async def fun(url, session):
    try:
        async with session.get(url) as response:
            print('url status : %s' % response.status)
            if response.status in [200, 201]:
                data = await response.text()
                return data
    except Exception as e:
        print(e)

async def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    # 取所有的url
    for link in pq.items('a'):
        url = link.attr('href')
        # 过滤重复的url
        if url and url.statrwith('http') not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls

async def init_url(url, session):
    html = await fun(start_url, session)
    seen_urls.add(url)
    extract_urls(html)

async def article_handle(url, session, pool):
    #获取文章详情并解析入库
    html = await fun(url, session)
    seen_urls.add(url)
    extract_urls(html)
    # 解析html
    pq = PyQuery(html)
    # 取文章的title
    title = pq('title').text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            insert_sql = "insert into article_test(title) value ('%s')" % title
            # 导入数据库
            await cur.execute(insert_sql)
            print(cur.description)
            (r, ) = await cur.fetchone()
            assert r == 42

async def consumer(pool):
    async with aiohttp.ClientSession as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            # 取第一个
            url = waitting_urls.pop()
            print('start get url: %s' % url)
            # 正则匹配 文章的url
            if re.match('http://*?jobbole.com/\d+/', url):
                if url not in seen_urls:
                    # 调用url
                    asyncio.ensure_future(article_handle(url, session, pool))
                else:
                    if url not in seen_urls:
                        asyncio.ensure_future(init_url(url, session))

async def main(loop):
    # 创建数据库连接池 还有配置参数
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                       user='root', password='', db='mysql',
                                       loop=loop, charset = 'utf8', autocommit=True)
    async with aiohttp.ClientSession as session:


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
