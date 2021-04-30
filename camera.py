import cv2
import asyncio
import websockets


class Camera:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        print("Kamera ist hochgefahren.")

    def frame(self):
        ret, frame = self.capture.read()
        ret, buffer = cv2.imencode(".jpg", frame)
        return buffer.tobytes()

async def cameraHandler(websocket, path):
    print("Kamera-übertragung aktiviert")
    while True:
        await websocket.send(cameraObj.frame())

print("Starting 4WD")
cameraObj = Camera()
start_server = websockets.serve(cameraHandler, "0.0.0.0", 5679)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()