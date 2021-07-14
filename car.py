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
        self.tire = Tire
        self.led = Led
        self.servo = Servo
        self.buzzer = Buzzer

    def run(self, speed=20):
        self.tire.run(speed)

    def left(self, speed=20):
        self.tire.left(speed)

    def right(self,speed=20):
        self.tire.right(speed)

    def back_right(self, speed=20):
        self.tire.back_right(speed)

    def back_left(self, speed=20):
        self.tire.back_left(speed)

    def back(self, speed=20):
        self.tire.back(speed)

    def brake(self, speed=20):
        self.tire.brake(speed)

    def led(self):
        self.led.led()

    def servo(self, arg):
        self.servo.servo(arg)

    def buzzerOn(self):
        self.buzzer.on()

    def buzzerOff(self):
        Buzzer.off()
