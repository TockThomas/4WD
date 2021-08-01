import RPi.GPIO as GPIO
import time


class Servo:
    def __init__(self):
        # Servo-Pins
        self.servoPIN1 = 23
        self.servoPIN2 = 11
        self.servoPIN3 = 9

        #GPIO-setup
        GPIO.setup(self.servoPIN1, GPIO.OUT)
        GPIO.setup(self.servoPIN2, GPIO.OUT)
        GPIO.setup(self.servoPIN3, GPIO.OUT)
        self.servo1 = GPIO.PWM(self.servoPIN1, 50)
        self.servo2 = GPIO.PWM(self.servoPIN2, 50)
        self.servo3 = GPIO.PWM(self.servoPIN3, 50)
        self.x = 6.5
        self.y = 7.5
        self.z = 6
        self.start()

    def start(self):
        self.servo1.start(self.z)
        self.servo2.start(self.y)
        self.servo3.start(self.x)
        self.servo_move()

    def move(self, pRotation="all"):
        if pRotation == "all" or pRotation == "left" or pRotation == "right":
            self.servo1.ChangeDutyCycle(self.z)
            self.servo2.ChangeDutyCycle(self.y)
        if pRotation == "all" or pRotation == "up" or pRotation == "down":
            self.servo3.ChangeDutyCycle(self.x)
        time.sleep(0.25)
        if pRotation == "all" or pRotation == "left" or pRotation == "right":
            self.servo1.ChangeDutyCycle(0)
            self.servo2.ChangeDutyCycle(0)
        if pRotation == "all" or pRotation == "up" or pRotation == "down":
            self.servo3.ChangeDutyCycle(0)

    def servo(self, arg):
        print("servo")
        if arg == "up":
            self.x += 0.5
            if self.x > 11:
                self.x = 11
        elif arg == "down":
            self.x -= 0.5
            if self.x < 4:
                self.x = 4
        elif arg == "left":
            self.y += 1
            self.z += 1
            if self.y > 12.5:
                self.y = 12.5
            if self.z > 11:
                self.z = 11
        elif arg == "right":
            self.y -= 1
            self.z -= 1
            if self.y < 3.5:
                self.y = 3.5
            if self.z < 2:
                self.z = 2
        self.move(arg)

    def reset(self):
        self.x = 6.5
        self.y = 7.5
        self.z = 6
        self.servo1.ChangeDutyCycle(self.z)
        self.servo2.ChangeDutyCycle(self.y)
        self.servo2.ChangeDutyCycle(self.x)
        time.sleep(0.25)
        self.servo1.ChangeDutyCycle(0)
        self.servo2.ChangeDutyCycle(0)
        self.servo3.ChangeDutyCycle(0)
