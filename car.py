try:
    import RPi.GPIO as GPIO
    import Car.Tire as Tire
    import Car.Led as Led
    import Car.Servo as Servo
except:
    print("Raspberry Pi nicht erkannt")
import time


class Car:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.tire = Tire.Tire()
        self.led = Led.Led()
        self.servo = Servo.Servo()

    def run(self, speed=20):
        self.tire.run(speed)

    def left(self, speed=20):
        self.tire.left(speed)

    def right(self, speed=20):
        self.tire.right(speed)

    def back_right(self, speed=20):
        self.tire.back_right(speed)

    def back_left(self, speed=20):
        self.tire.back_left(speed)

    def back(self, speed=20):
        self.tire.back(speed)

    def brake(self):
        self.tire.brake()

    def ledSwitch(self):
        self.led.led()

    def servoMove(self, arg):
        self.servo.servo(arg)
