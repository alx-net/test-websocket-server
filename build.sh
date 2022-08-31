docker build -t test-websocket-server .
docker run --rm -p 8082:8082 --name test-websocket-server test-websocket-server