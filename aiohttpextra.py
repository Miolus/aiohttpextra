import aiohttp

async def start_server(app, address='localhost', port=80):
    runner = aiohttp.web.AppRunner(app)
    runners.append(runner)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, address, port)
    print('An app is starting...')
    await site.start()