def start():
    import asyncio
    import websockets
    import car


    keys = {
        "w": False,
        "a": False,
        "s": False,
        "d": False,
        "f": False,
        "ArrowUp": False,
        "ArrowDown": False,
        "ArrowLeft": False,
        "ArrowRight": False
    }


    async def keyHandler(websocket, path):
        while True:
            #Steuerung
            key = await websocket.recv()
            ledstatus = "none"
            print(key)
            try:
                if key[2] == "t":
                    keys[key[0]] = True
                elif key[2] == "f":
                    keys[key[0]] = False
                else:
                    keyArrow(key)
            except:
                print("falsche Taste")
            if carstatus:
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
                if keys["f"]:
                    car.led(ledstatus)
                    if ledstatus == "none":
                        ledstatus = "all"
                    else:
                        ledstatus = "none"
                if keys["ArrowUp"]:
                    car.servo("up")
                elif keys["ArrowDown"]:
                    car.servo("down")
                elif keys["ArrowLeft"]:
                    car.servo("left")
                elif keys["ArrowRight"]:
                    car.servo("right")

    def keyArrow(key):
        if key == "ArrowUp,true":
            keys["ArrowUp"] = True
        elif key == "ArrowUp,false":
            keys["ArrowUp"] = False
        elif key == "ArrowDown,true":
            keys["ArrowDown"] = True
        elif key == "ArrowDown,false":
            keys["ArrowDown"] = False
        elif key == "ArrowLeft,true":
            keys["ArrowLeft"] = True
        elif key == "ArrowLeft,false":
            keys["ArrowLeft"] = False
        elif key == "ArrowRight,true":
            keys["ArrowRight"] = True
        elif key == "ArrowRight,false":
            keys["ArrowRight"] = False

    print("-- Starting 4WD --")
    try:
        car = car.Car()
        carstatus = True
    except:
        print("Auto nicht verfügbar.")
        carstatus = False
    start_server = websockets.serve(keyHandler, "0.0.0.0", 5678)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
