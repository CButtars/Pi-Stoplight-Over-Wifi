import RPi.GPIO as GPIO

ylwPin = 27

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ylwPin, GPIO.OUT) # LED pin set as output

def yellowOn():
	print("INPUT:", GPIO.input(ylwPin))
	if GPIO.input(ylwPin):
		print("Turning off yellow")
		GPIO.output(ylwPin, GPIO.LOW)
		return "None"
	else:
		print("Turning on yellow")
		GPIO.output(ylwPin, GPIO.HIGH)
		return "Green"

def yellowOff():
	GPIO.output(ylwPin, GPIO.LOW)
	return "None"