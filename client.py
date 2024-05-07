import asyncio
import websockets

async def receive_messages():
    uri = "ws://localhost:8000/ws"  # Change the URI if your FastAPI server is running on a different address

    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received message from server: {message}")
            await websocket.send('this is from client side')

asyncio.run(receive_messages())