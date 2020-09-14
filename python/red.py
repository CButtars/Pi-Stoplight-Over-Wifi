import RPi.GPIO as GPIO

redPin = 22

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(redPin, GPIO.OUT) # LED pin set as output

def redOn():
	
	if GPIO.input(redPin):
		print("Turning off red")
		GPIO.output(redPin, GPIO.LOW)
		return "None"
	else:
		print("Turning on red")
		GPIO.output(redPin, GPIO.HIGH)
		return "Green"

def redOff():
	GPIO.output(redPin, GPIO.LOW)
	return "None"