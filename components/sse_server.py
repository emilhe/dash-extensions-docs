import asyncio

from dash_extensions.streaming import sse_message
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from sse_model import MyModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


async def stream_content(content: str):
    for character in content:
        await asyncio.sleep(0.1)  # add delay to simulate streaming response
        yield sse_message(character)  # stream one character at a time
    yield sse_message()  # signal stream end


@app.post("/steam")
async def main(model: MyModel):
    return StreamingResponse(
        stream_content(model.content), media_type="text/event-stream"
    )


# Add CORS middleware to allow cross-origin requests (necessary for streaming).
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=5000)
