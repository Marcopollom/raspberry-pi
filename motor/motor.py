import RPi.GPIO as GPIO

class motor:

    def __init__(self, F, B):
        self.pinFwd = F
        self.pinBwd = B

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinFwd, GPIO.OUT)
        GPIO.setup(self.pinBwd, GPIO.OUT)


    def __del__(self):
        GPIO.cleanup()

    def forward(self):
        GPIO.output(self.pinFwd, GPIO.HIGH)
        GPIO.output(self.pinBwd, GPIO.LOW)

    def backward(self):
        GPIO.output(self.pinFwd, GPIO.LOW)
        GPIO.output(self.pinBwd, GPIO.HIGH) 

    def stop(self):
        GPIO.output(self.pinFwd, GPIO.LOW)
        GPIO.output(self.pinBwd, GPIO.LOW)


