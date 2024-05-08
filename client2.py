import websockets
from websockets.sync.client import connect
import asyncio

async def hello():
    async with websockets.connect(uri="ws://127.0.0.1:8765",) as websocket:
        while True :
            message = input("Enter a message: ")
            await websocket.send(message)
            msg= await websocket.recv()
            print(f"Received: {msg}")


asyncio.get_event_loop().run_until_complete(hello())