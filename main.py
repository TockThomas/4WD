import asyncio
import websockets
import car


async def time(websocket, path):
    while True:
        key = await websocket.recv().lowercase()
        print(key)
        #if key == "a":
            #bobby.left()
        #elif key == "w":
            #bobby.run()

print("Starting 4WD")
bobby = car
start_server = websockets.serve(time, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()