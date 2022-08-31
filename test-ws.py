import websocket

ws = websocket.create_connection("ws://127.0.0.1:8080/ws")


ws.send("Hello world")

print(ws.recv())