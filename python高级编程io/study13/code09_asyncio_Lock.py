#使用异步锁
import asyncio
from asyncio import Lock
import aiohttp
cache = {}
lock = Lock()

async def get_stuff(url):
    # 加锁
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff

async def parse_stuff(url):
    stuff = await get_stuff(url)

