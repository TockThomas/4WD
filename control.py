def start():
    try:
        import asyncio
        import websockets
        import car
        import time


        keys = {
            "w": False,
            "a": False,
            "s": False,
            "d": False,
            "f": False,
            "e": False,
            "r": False,
            "ArrowUp": False,
            "ArrowDown": False,
            "ArrowLeft": False,
            "ArrowRight": False
        }


        async def keyHandler(websocket, path):
            while True:
                #Steuerung
                key = await websocket.recv()
                eventKey(key)
                if carstatus:
                    try:
                        carHandler()
                    except:
                        carError()
                else:
                    print(key)


        def eventKey(key):
            try:
                if key[2] == "t":
                    keys[key[0]] = True
                elif key[2] == "f":
                    keys[key[0]] = False
                else:
                    keyArrow(key)
            except:
                print("falsche Taste")
                pass

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

        def carHandler():
            if keys["w"]:
                if keys["a"]:
                    car.driveForwardLeft()
                elif keys["d"]:
                    car.driveForwardRight()
                else:
                    car.driveForward()
            elif keys["s"]:
                if keys["a"]:
                    car.driveBackwardLeft()
                elif keys["d"]:
                    car.driveBackwardRight()
                else:
                    car.driveBackward()
            else:
                car.driveStop()
            if keys["e"]:
                car.buzzerOn()
            else:
                car.buzzerOff()
            if keys["f"]:
                car.changeLed()
                keys["f"] = False
            elif keys["ArrowUp"]:
                car.servoMove("up")
                keys["ArrowUp"] = False
            elif keys["ArrowDown"]:
                car.servoMove("down")
                keys["ArrowDown"] = False
            elif keys["ArrowLeft"]:
                car.servoMove("left")
                keys["ArrowLeft"] = False
            elif keys["ArrowRight"]:
                car.servoMove("right")
                keys["ArrowRight"] = False
            elif keys["r"]:
                car.servoReset()
                keys["r"] = False

        def carError():
            car.driveStop()
            car.servoReset()
            car.changeLed() #red
            car.buzzerOn()
            time.sleep(2)
            car.changeLed() #off
            car.buzzerOff()
            car.shutdown


        print("-- Starting 4WD --")
        car = car.Car()
        carstatus = True
        """try:
            car = car.Car()
            carstatus = True
        except:
            print("Auto nicht verfügbar.")
            carstatus = False
            pass"""
        start_server = websockets.serve(keyHandler, "0.0.0.0", 5678)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        carError()
