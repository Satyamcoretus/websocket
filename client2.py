import websockets
from websockets.sync.client import connect
import asyncio

async def hello():
    async with websockets.connect(uri="ws://127.0.0.1:8765") as websocket:

        message = input("Enter a message: ")
        await websocket.send(message)
        while True:
            msg= await websocket.recv()
            print(f"Received: {msg}")
            continue

asyncio.get_event_loop().run_until_complete(hello())