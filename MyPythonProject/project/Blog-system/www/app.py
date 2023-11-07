import logging;

logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from aiohttp import web


async def index(request):
    headers = {'Content-Type': 'text/html'}
    return web.Response(body=b'<h1>ztj god</h1>',headers=headers)

async def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 9000)
    await site.start()
    logging.info('server started at http://127.0.0.1:9000...')

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()