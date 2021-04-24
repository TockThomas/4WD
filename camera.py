import asyncio
import websockets
import cv2

capture = cv2.VideoCapture(0)


async def keyHandler(websocket, path):
    while True:
        ret, image = capture.read()
        websocket.send(image)


print("Starting 4WD")
start_server = websockets.serve(keyHandler, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
