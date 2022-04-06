import asyncio
import json
import random
import uvicorn
from sse_starlette import EventSourceResponse
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

middleware = Middleware(CORSMiddleware, allow_origins=["*"], allow_headers=["*"])
server = Starlette(middleware=[middleware])

async def random_data():
    while True:
        await asyncio.sleep(1)
        yield json.dumps([random.random() for _ in range(10)])

@server.route("/random_data")
async def sse(request):
    generator = random_data()
    return EventSourceResponse(generator)

if __name__ == "__main__":
    uvicorn.run(server, port=5000)