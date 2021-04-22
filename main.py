import asyncio
import datetime
import random
import websockets
import car


async def time(websocket, path):
    while True:
        key = await websocket.recv()
        bobby.run()

bobby = car
start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()