import RPi.GPIO as GPIO


class Tire:
    def __init__(self):
        #Tire-Pins
        self.IN1 = 20  # Linke Reifenseite nach vorne
        self.IN2 = 21  # Linke Reifenseite nach hinten
        self.IN3 = 19  # Rechte Reifenseite nach vorne
        self.IN4 = 26  # Rechte Reifenseite nach hinten
        self.ENA = 16
        self.ENB = 13

        #GPIO-setup
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        GPIO.output(self.ENA, GPIO.HIGH)
        GPIO.output(self.ENB, GPIO.HIGH)
        self.ENA_PWM = GPIO.PWM(self.ENA, 2000)
        self.ENB_PWM = GPIO.PWM(self.ENB, 2000)
        self.ENA_PWM.start(0)
        self.ENB_PWM.start(0)
        self.speed = 20

    def forward(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(self.speed)
        self.ENB_PWM.ChangeDutyCycle(self.speed)

    def forwardLeft(self):
        ENA = 1 * self.speed / 20
        ENB = 30 * self.speed / 20
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(ENA)
        self.ENB_PWM.ChangeDutyCycle(ENB)

    def forwardRight(self):
        ENA = 30 * self.speed / 20
        ENB = 1 * self.speed / 20
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA_PWM.ChangeDutyCycle(ENA)
        self.ENB_PWM.ChangeDutyCycle(ENB)

    def backwardRight(self):
        ENA = 30 * self.speed / 20
        ENB = 1 * self.speed / 20
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.ENA_PWM.ChangeDutyCycle(ENA)
        self.ENB_PWM.ChangeDutyCycle(ENB)

    def backwardLeft(self):
        ENA = 1 * self.speed / 20
        ENB = 30 * self.speed / 20
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.ENA_PWM.ChangeDutyCycle(ENA)
        self.ENB_PWM.ChangeDutyCycle(ENB)

    def backward(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.ENA_PWM.ChangeDutyCycle(self.speed)
        self.ENB_PWM.ChangeDutyCycle(self.speed)

    def stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
