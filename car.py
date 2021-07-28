try:
    import RPi.GPIO as GPIO
    import Car.Tire as Tire
except:
    print("Raspberry Pi nicht erkannt")
import time


class Car:
    def __init__(self):
        self.tire = Tire.Tire()

    def run(self, speed=20):
        Tire.run(speed)

    def left(self, speed=20):
        Tire.left(speed)

    def right(self, speed=20):
        Tire.right(speed)

    def back_right(self, speed=20):
        Tire.back_right(speed)

    def back_left(self, speed=20):
        Tire.back_left(speed)

    def back(self, speed=20):
        Tire.back(speed)

    def brake(self):
        Tire.brake()