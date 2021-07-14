import RPi.GPIO as GPIO


class Buzzer:
    def __init(self):
        # Buzzer-Pin
        self.buzzer = 8

        #GPIO.setup
        GPIO.setup(self.buzzer, GPIO.OUT)

    def on(self):
        GPIO.output(self.buzzer, GPIO.LOW)

    def off(self):
        GPIO.output(self.buzzer, GPIO.HIGH)
