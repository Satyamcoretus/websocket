import asyncio
from websockets.server import serve

async def echo(websocket):
    print(websocket)
    async for message in websocket:
        response = f'This is what server respond ,HELLO, and this is what you respond ->\n{message}'
        await websocket.send(response)


async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())