import RPi.GPIO as GPIO

class ssegment:
	
	def __init__(self, ap, bp, cp, dp, ep, fp, gp, pwrp):
		# Assigns pins to instace vairables
		self.a = ap
		self.b = bp
		self.c = cp
		self.d = dp
		self.e = ep
		self.f = fp
		self.g = gp
		self.pwr = pwrp

		# Sets pins to output mode
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.a, GPIO.OUT)
		GPIO.setup(self.b, GPIO.OUT)
		GPIO.setup(self.c, GPIO.OUT)
		GPIO.setup(self.d, GPIO.OUT)
		GPIO.setup(self.e, GPIO.OUT)
		GPIO.setup(self.f, GPIO.OUT)
		GPIO.setup(self.g, GPIO.OUT)
		GPIO.setup(self.pwr, GPIO.OUT)
		
		# Turns on all pins
		GPIO.output(self.a, GPIO.HIGH)
		GPIO.output(self.b, GPIO.HIGH)
		GPIO.output(self.c, GPIO.HIGH)
		GPIO.output(self.d, GPIO.HIGH)
		GPIO.output(self.e, GPIO.HIGH)
		GPIO.output(self.f, GPIO.HIGH)
		GPIO.output(self.g, GPIO.HIGH)
		GPIO.output(self.pwr, GPIO.HIGH)
    
	def __del__(self):
		# Turns off all pins and cleans up GPIO
		GPIO.output(self.a, GPIO.LOW)
		GPIO.output(self.b, GPIO.LOW)
		GPIO.output(self.c, GPIO.LOW)
		GPIO.output(self.d, GPIO.LOW)
		GPIO.output(self.e, GPIO.LOW)
		GPIO.output(self.f, GPIO.LOW)
		GPIO.output(self.g, GPIO.LOW)
		GPIO.output(self.pwr, GPIO.LOW)
       	
		GPIO.cleanup()

	def display(self, n):
		
		# Assigns each number its coresponding segment representation 
		bitmap = {
			0: 0b00111111,
			1: 0b00000110,
			2: 0b01011011,
			3: 0b01001111,
			4: 0b01100110,
			5: 0b01101101, 
			6: 0b01111101,
			7: 0b00000111,
			8: 0b01111111,
			9: 0b01100111 
		}

		# Assigns segments to positions 
		charMap = {
			'a': 0b00000001,
			'b': 0b00000010,
			'c': 0b00000100,
			'd': 0b00001000,
			'e': 0b00010000,
			'f': 0b00100000,
			'g': 0b01000000
		}

		# Assigns pins to segments 
		pinMap = {
			'a': self.a,
			'b': self.b,
			'c': self.c,
			'd': self.d,
			'e': self.e,
			'f': self.f,
			'g': self.g
		}

		value = bitmap[n]

		GPIO.output(list(pinMap.values()), GPIO.HIGH)

		for i, e in charMap.items():
			if value & e == e:
				GPIO.output(pinMap[i], GPIO.LOW)

	def reset(self):
		GPIO.output(list(self.a, self.b, self.c, self.d, self.e, self.g, self.h, self.pwr), GPIO.HIGH)
