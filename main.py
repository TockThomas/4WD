import asyncio
import websockets
import car


async def keyHandler(websocket, path):
    while True:
        key = await websocket.recv()
        print(key)
        #if key == "a":
            #bobby.left()
        #elif key == "w":
            #bobby.run()

print("Starting 4WD")
bobby = car
start_server = websockets.serve(keyHandler, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()