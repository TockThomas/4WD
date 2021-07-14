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
        self.ledstatus = False

    def led(self):
        self.ledstatus = not self.ledstatus
        if self.ledstatus:
            GPIO.output(self.LED_R, GPIO.HIGH)
            GPIO.output(self.LED_G, GPIO.HIGH)
            GPIO.output(self.LED_B, GPIO.HIGH)
        else:
            GPIO.output(self.LED_R, GPIO.LOW)
            GPIO.output(self.LED_G, GPIO.LOW)
            GPIO.output(self.LED_B, GPIO.LOW)
