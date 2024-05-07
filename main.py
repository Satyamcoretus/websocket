from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_text('hello client')
        data = await websocket.receive_text()
        if data == 'exit':
            websocket.close()

