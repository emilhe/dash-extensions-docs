import time

from dash_extensions.streaming import sse_message
from flask import Response, request


# TODO: Maybe make this in a smarter way?
def register_routes(server):
    # sse.py
    @server.post("/stream")
    def stream():
        message = request.data.decode("utf-8")

        def eventStream():
            for char in message:
                time.sleep(0.1)
                yield sse_message(char)
            yield sse_message()

        return Response(eventStream(), mimetype="text/event-stream")
