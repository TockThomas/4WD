import asyncio
import websockets
import car

keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}


async def keyHandler(websocket, path):
    while True:
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
            car.run()
        elif keys["a"]:
            car.left()
        elif keys["d"]:
            car.right()
        elif keys["s"]:
            car.back()
        else:
            car.brake()


print("Starting 4WD")
car = car.Car()
start_server = websockets.serve(keyHandler, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
