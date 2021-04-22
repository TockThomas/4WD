import RPi.GPIO as GPIO
import time


class Car:
    # Tire-Pins
    IN1 = 20  # Linke Reifenseite nach vorne
    IN2 = 21  # Linke Reifenseite nach hinten
    IN3 = 19  # Rechte Reifenseite nach vorne
    IN4 = 26  # Rechte Reifenseite nach hinten
    ENA = 16
    ENB = 13
    # LED-Pins
    LED_R = 22
    LED_G = 27
    LED_B = 24
    # Servo-Pins
    servoPIN1 = 23
    servoPIN2 = 11
    servoPIN3 = 9
    # Buzzer-Pin
    buzzer = 8
    # GPIO-setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(servoPIN1, GPIO.OUT)
    GPIO.setup(servoPIN2, GPIO.OUT)
    GPIO.setup(servoPIN3, GPIO.OUT)
    GPIO.setup(buzzer, GPIO.OUT)
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)
    ENA_PWM = GPIO.PWM(ENA, 2000)
    ENB_PWM = GPIO.PWM(ENB, 2000)
    servo1 = GPIO.PWM(servoPIN1, 50)
    servo2 = GPIO.PWM(servoPIN2, 50)
    servo3 = GPIO.PWM(servoPIN3, 50)
    ENA_PWM.start(0)
    ENB_PWM.start(0)

    def run(self, speed=20):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(speed)
        self.ENB_PWM.ChangeDutyCycle(speed)

    def left(self, speed=20):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(speed)
        self.ENB_PWM.ChangeDutyCycle(speed)

    def right(self, speed=20):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(speed)
        self.ENB_PWM.ChangeDutyCycle(speed)

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
