import RPi.GPIO as GPIO


class Led:
    def __init__(self):
        # LED-Pins
        self.LED_R = 22
        self.LED_G = 27
        self.LED_B = 24

        #GPIO-setup
        GPIO.setup(self.LED_R, GPIO.OUT)
        GPIO.setup(self.LED_G, GPIO.OUT)
        GPIO.setup(self.LED_B, GPIO.OUT)
        GPIO.output(self.LED_R, GPIO.LOW)
        GPIO.output(self.LED_G, GPIO.LOW)
        GPIO.output(self.LED_B, GPIO.LOW)

        self.leds = {
            "red": False,
            "green": False,
            "blue": False
        }

    def changeLed(self, pLed):
        self.leds[pLed[0]] = pLed[1]
        if self.leds["red"]:
            GPIO.output(self.LED_R, GPIO.HIGH)
        else:
            GPIO.output(self.LED_R, GPIO.LOW)
        if self.leds["green"]:
            GPIO.output(self.LED_G, GPIO.HIGH)
        else:
            GPIO.output(self.LED_G, GPIO.LOW)
        if self.leds["blue"]:
            GPIO.output(self.LED_B, GPIO.HIGH)
        else:
            GPIO.output(self.LED_B, GPIO.LOW)