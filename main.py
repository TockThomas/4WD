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
            bobby.run()
        elif keys["a"]:
            bobby.left()
        elif keys["d"]:
            bobby.right()
        elif keys["s"]:
            bobby.back()
        else:
            bobby.brake()


print("Starting 4WD")
bobby = car
start_server = websockets.serve(keyHandler, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
