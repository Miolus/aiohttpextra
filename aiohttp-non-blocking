import aiohttp

runners = []

async def start_server(app, address='localhost', port=80):
    runner = aiohttp.web.AppRunner(app)
    runners.append(runner)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, address, port)
    print(f'An new aiohttp app is starting and listening on {address}:{port}')
    await site.start()
