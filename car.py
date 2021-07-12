try:
    import RPi.GPIO as GPIO
except:
    print("Raspberry Pi nicht erkannt")
import time


class Car:
    def __init__(self):
        # Tire-Pins
        self.IN1 = 20  # Linke Reifenseite nach vorne
        self.IN2 = 21  # Linke Reifenseite nach hinten
        self.IN3 = 19  # Rechte Reifenseite nach vorne
        self.IN4 = 26  # Rechte Reifenseite nach hinten
        self.ENA = 16
        self.ENB = 13
        # LED-Pins
        self.LED_R = 22
        self.LED_G = 27
        self.LED_B = 24
        # Servo-Pins
        self.servoPIN1 = 23
        self.servoPIN2 = 11
        self.servoPIN3 = 9
        # Buzzer-Pin
        buzzer = 8
        # GPIO-setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        GPIO.setup(self.LED_R, GPIO.OUT)
        GPIO.setup(self.LED_G, GPIO.OUT)
        GPIO.setup(self.LED_B, GPIO.OUT)
        GPIO.setup(self.servoPIN1, GPIO.OUT)
        GPIO.setup(self.servoPIN2, GPIO.OUT)
        GPIO.setup(self.servoPIN3, GPIO.OUT)
        GPIO.setup(buzzer, GPIO.OUT)
        GPIO.output(self.ENA, GPIO.HIGH)
        GPIO.output(self.ENB, GPIO.HIGH)
        self.ENA_PWM = GPIO.PWM(self.ENA, 2000)
        self.ENB_PWM = GPIO.PWM(self.ENB, 2000)
        self.servo1 = GPIO.PWM(self.servoPIN1, 50)
        self.servo2 = GPIO.PWM(self.servoPIN2, 50)
        self.servo3 = GPIO.PWM(self.servoPIN3, 50)
        self.servo_x = 6.5
        self.servo_y = 7.5
        self.servo_z = 6
        self.servo1.start(self.servo_x)
        self.servo2.start(self.servo_y)
        self.servo3.start(self.servo_z)
        self.ENA_PWM.start(0)
        self.ENB_PWM.start(0)
        self.colorstatus = "none"

    def run(self, speed=20):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(speed)
        self.ENB_PWM.ChangeDutyCycle(speed)

    def left(self, speed=20):
        self.ENA = 1 * speed / 20
        self.ENB = 30 * speed / 20
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(self.ENA)
        self.ENB_PWM.ChangeDutyCycle(self.ENB)

    def right(self, speed=20):
        self.ENA = 30 * speed / 20
        self.ENB = 1 * speed / 20
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(self.ENA)
        self.ENB_PWM.ChangeDutyCycle(self.ENB)

    def back_right(self, speed=20):
        self.ENA = 30 * speed / 20
        self.ENB = 1 * speed / 20
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.ENA_PWM.ChangeDutyCycle(self.ENA)
        self.ENB_PWM.ChangeDutyCycle(self.ENB)

    def back_left(self, speed=20):
        self.ENA = 1 * speed / 20
        self.ENB = 30 * speed / 20
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.ENA_PWM.ChangeDutyCycle(self.ENA)
        self.ENB_PWM.ChangeDutyCycle(self.ENB)

    def back(self, speed=20):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.ENA_PWM.ChangeDutyCycle(speed)
        self.ENB_PWM.ChangeDutyCycle(speed)

    def brake(self, speed=20):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(speed)
        self.ENB_PWM.ChangeDutyCycle(speed)

    def led(self, color="all"):
        if color == "none":
            GPIO.output(self.LED_R, GPIO.LOW)
            GPIO.output(self.LED_G, GPIO.LOW)
            GPIO.output(self.LED_B, GPIO.LOW)
        elif color == "all":
            GPIO.output(self.LED_R, GPIO.HIGH)
            GPIO.output(self.LED_G, GPIO.HIGH)
            GPIO.output(self.LED_B, GPIO.HIGH)

    def servo_move(self, x, y, z):
        self.servo1.ChangeDutyCycle(x)
        self.servo2.ChangeDutyCycle(y)
        self.servo3.ChangeDutyCycle(z)
        time.sleep(0.2)

    def servo(self, arg):
        if arg == "up":
            self.servo_z += 0.5
            if self.servo_z > 11:
                self.servo_z = 11
        elif arg == "down":
            self.servo_z -= 0.5
            if self.servo_z < 4:
                self.servo_z = 4
        elif arg == "left":
            self.servo_x += 1
            self.servo_y += 1
            if self.servo_x > 12.5:
                self.servo_x = 12.5
            if self.servo_y > 11:
                self.servo_y = 11
        elif arg == "right":
            self.servo_x -= 1
            self.servo_y -= 1
            if self.servo_x < 3.5:
                self.servo_x = 3.5
            if self.servo_y < 2:
                self.servo_y = 2
        self.servo_move(self.servo_x, self.servo_y, self.servo_z)
        print(self.servo_x, self.servo_y, self.servo_z)