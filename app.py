from flask import Flask, render_template, request, redirect

import sys
sys.path.append('python')
import time

import green
import yellow
import red

stop = False

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('index.html')

@app.route('/green', methods=["POST"])
def greenToggle():
	if request.method == "POST":
		yellow.yellowOff()
		red.redOff()
		green.greenOn()
	print("Redirect to /")
	return redirect('/', code=302)

@app.route('/yellow', methods=["POST"])
def yellowToggle():
	if request.method == "POST":
		green.greenOff()
		red.redOff()
		yellow.yellowOn()
	print("Redirect to /")
	return redirect('/', code=302)

@app.route('/red', methods=["POST"])
def redToggle():
	if request.method == "POST":
		green.greenOff()
		yellow.yellowOff()
		red.redOn()
	print("Redirect to /")
	return redirect('/', code=302)

@app.route('/cycle', methods=["POST"])
def cycleToggle():
	global stop
	if request.method == "POST":
		stop = not stop
		while stop:
			green.greenOn()
			time.sleep(5)
			green.greenOff()
			yellow.yellowOn()
			time.sleep(1)
			yellow.yellowOff()
			red.redOn()
			time.sleep(5)
			red.redOff()
		green.greenOff()
		yellow.yellowOff()
		red.redOff()
	print("Redirect to /")
	return redirect('/', code=302)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
