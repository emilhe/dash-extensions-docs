import asyncio
import json
import random
from quart import websocket, Quart

app = Quart(__name__)

@app.websocket("/random_data")
async def random_data():
    while True:
        output = json.dumps([random.random() for _ in range(10)])
        await websocket.send(output)
        await asyncio.sleep(1)

if __name__ == "__main__":
    app.run(port=5000)