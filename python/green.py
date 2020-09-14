import RPi.GPIO as GPIO

grnPin = 17

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(grnPin, GPIO.OUT) # LED pin set as output

def greenOn():
	
	if GPIO.input(grnPin):
		print("Turning off green")
		GPIO.output(grnPin, GPIO.LOW)
		return "None"
	else:
		print("Turning on green")
		GPIO.output(grnPin, GPIO.HIGH)
		return "Green"

def greenOff():
	GPIO.output(grnPin, GPIO.LOW)
	return "None"