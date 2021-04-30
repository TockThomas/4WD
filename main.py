import asyncio
import websockets
import car
import camera
import threading

keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}


async def sendFrame(websocket, camera):
    print("Thread für Bildübertragung erstellt.")
    while True:
        await websocket.send(camera.frame())

async def keyHandler(websocket, path):
    print(websocket)
    await cameraThread.start()
    while True:
        #Steuerung
        key = await websocket.recv()
        print(key)
        try:
            if key[2] == "t":
                keys[key[0]] = True
            elif key[2] == "f":
                keys[key[0]] = False
        except:
            print("falsche Taste")
        if keys["w"]:
            if keys["a"]:
                car.left()
            elif keys["d"]:
                car.right()
            else:
                car.run()
        elif keys["s"]:
            if keys["a"]:
                car.back_left()
            elif keys["d"]:
                car.back_right()
            else:
                car.back()
        else:
            car.brake()


print("Starting 4WD")
car = car.Car()
cameraObj = camera.Camera()
start_server = websockets.serve(keyHandler, "0.0.0.0", 5678)
cameraThread = threading.Thread(target=sendFrame, args=(websockets, cameraObj))
cameraThread.daemon = True

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
