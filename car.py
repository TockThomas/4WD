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
        # GPIO-setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def run(self, speed=20):
        Tire.run(speed)

    def left(self, speed=20):
        Tire.left(speed)

    def right(self,speed=20):
        Tire.right(speed)

    def back_right(self, speed=20):
        Tire.back_right(speed)

    def back_left(self, speed=20):
        Tire.back_left(speed)

    def back(self, speed=20):
        Tire.back(speed)

    def brake(self, speed=20):
        Tire.brake(speed)

    def led(self):
        Led.led()

    def servo(self, arg):
        Servo.servo(arg)

    def buzzerOn(self):
        Buzzer.on()

    def buzzerOff(self):
        Buzzer.off()
