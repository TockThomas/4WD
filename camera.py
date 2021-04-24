import asyncio
import websockets
import cv2

capture = cv2.VideoCapture(0)


async def keyHandler(websocket, path):
    while True:
        ret, frame = capture.read()
        ret, buffer = cv2.imencode(".jpg", frame)
        await websocket.send(buffer.tobytes())


print("Starting 4WD")
start_server = websockets.serve(keyHandler, "localhost", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
