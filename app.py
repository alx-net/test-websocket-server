import argparse
import uuid
from sanic import Sanic

# Init Sanic Server
app = Sanic("my_awesome_server")

#app.config.FORWARDED_SECRET = "v7wco86cMarphBUH"

# Configure websocket
app.config.WEBSOCKET_MAX_SIZE = 2 ** 32
app.config.WEBSOCKET_MAX_QUEUE = 2**32
app.config.WEBSOCKET_READ_LIMIT = 2 ** 32
app.config.WEBSOCKET_WRITE_LIMIT = 2 ** 16
app.config.WEBSOCKET_PING_INTERVAL = None
app.config.WEBSOCKET_PING_TIMEOUT = None


UUID = str(uuid.uuid4())

@app.websocket("/ws")
async def connect(request, ws):
    global UUID
    try:
        while True:
            msg = await ws.recv()
            await ws.send(f"UUID: {UUID}, MSG: {msg}")
    finally:
            await ws.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int)
    args = parser.parse_args()

    app.run(host="0.0.0.0",debug=False, port=args.port, workers=2,  access_log=False)