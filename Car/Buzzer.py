import RPi.GPIO as GPIO


class Buzzer:
    def __init(self):
        # Buzzer-Pin
        self.buzzer = 8

        #GPIO.setup
        GPIO.setup(self.buzzer, GPIO.OUT)
        self.status = False

    def buzzer(self):
        self.status = not self.status
        if self.status:
            GPIO.output(self.buzzer, GPIO.LOW)
        else:
            GPIO.output(self.buzzer, GPIO.HIGH)
