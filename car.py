try:
    import RPi.GPIO as GPIO
    import Car.Tire as Tire
    import Car.Led as Led
    import Car.Servo as Servo
    import Car.Buzzer as Buzzer
except:
    print("Raspberry Pi nicht erkannt")


class Car:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.tire = Tire.Tire()
        self.led = Led.Led()
        self.servo = Servo.Servo()
        self.buzzer = Buzzer.Buzzer()

    def driveForward(self):
        self.tire.forward()

    def driveForwardLeft(self):
        self.tire.forwardLeft()

    def driveForwardRight(self):
        self.tire.forwardRight()

    def driveBackwardRight(self):
        self.tire.backwardRight()

    def driveBackwardLeft(self):
        self.tire.backwardLeft()

    def driveBackward(self):
        self.tire.backward()

    def driveStop(self):
        self.tire.stop()

    def changeLed(self):
        self.led.changeLed()

    def servoMove(self, arg):
        self.servo.servo(arg)

    def servoReset(self):
        self.servo.reset()

    def buzzerOn(self):
        self.buzzer.on()

    def buzzerOff(self):
        self.buzzer.off()

    def shutdown(self):
        GPIO.cleanup()
