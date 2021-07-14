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
        self.servo_x = 6.5
        self.servo_y = 7.5
        self.servo_z = 6
        self.servo_start()

    def servo_start(self):
        self.servo1.start(self.servo_z)
        self.servo2.start(self.servo_y)
        self.servo3.start(self.servo_x)
        self.servo_move()

    def servo_move(self):
        self.servo1.ChangeDutyCycle(self.servo_z)
        self.servo2.ChangeDutyCycle(self.servo_y)
        self.servo3.ChangeDutyCycle(self.servo_x)
        time.sleep(0.25)
        self.servo1.ChangeDutyCycle(0)
        self.servo2.ChangeDutyCycle(0)
        self.servo3.ChangeDutyCycle(0)

    def servo(self, arg):
        if arg == "up":
            self.servo_x += 0.5
            if self.servo_x > 11:
                self.servo_x = 11
        elif arg == "down":
            self.servo_x -= 0.5
            if self.servo_x < 4:
                self.servo_x = 4
        elif arg == "left":
            self.servo_y += 1
            self.servo_z += 1
            if self.servo_y > 12.5:
                self.servo_y = 12.5
            if self.servo_z > 11:
                self.servo_z = 11
        elif arg == "right":
            self.servo_y -= 1
            self.servo_z -= 1
            if self.servo_y < 3.5:
                self.servo_y = 3.5
            if self.servo_z < 2:
                self.servo_z = 2
        self.servo_move()
