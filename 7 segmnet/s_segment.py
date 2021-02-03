import RPi.GPIO as GPIO

class ssegment:

    def __init__(self, ap, bp, cp, dp, ep, fp, gp, pwrp):
	self.a = ap
	self.b = bp
	self.c = cp
	self.d = dp
	self.e = ep
	self.f = fp
	self.g = gp
	self.pwr = pwrp

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(self.a, GPIO.OUT)
	GPIO.setup(self.b, GPIO.OUT)
	GPIO.setup(self.c, GPIO.OUT)
	GPIO.setup(self.d, GPIO.OUT)
	GPIO.setup(self.e, GPIO.OUT)
	GPIO.setup(self.f, GPIO.OUT)
	GPIO.setup(self.g, GPIO.OUT)
	GPIO.setup(self.pwr, GPIO.OUT)
	
	GPIO.output(self.a, GPIO.HIGH)
	GPIO.output(self.b, GPIO.HIGH)
	GPIO.output(self.c, GPIO.HIGH)
	GPIO.output(self.d, GPIO.HIGH)
	GPIO.output(self.e, GPIO.HIGH)
	GPIO.output(self.f, GPIO.HIGH)
	GPIO.output(self.g, GPIO.HIGH)
	GPIO.output(self.pwr, GPIO.HIGH)
    
    def __del__(self):
	GPIO.output(self.a, GPIO.LOW)
	GPIO.output(self.b, GPIO.LOW)
	GPIO.output(self.c, GPIO.LOW)
	GPIO.output(self.d, GPIO.LOW)
	GPIO.output(self.e, GPIO.LOW)
	GPIO.output(self.f, GPIO.LOW)
	GPIO.output(self.g, GPIO.LOW)
	GPIO.output(self.pwr, GPIO.LOW)
       	GPIO.cleanup()


