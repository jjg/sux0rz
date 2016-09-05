from pyfirmata import Arduino, util
from flask import Flask, render_template

board = Arduino('/dev/ttyACM0')
motor_1 = board.get_pin('d:10:p')
motor_2 = board.get_pin('d:11:p')

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/hello')
def hello_world():
	motor_1.write(.1)
	motor_2.write(.1)
	return 'Hello, World!'

@app.route('/m1/<int:speed>')
def motor_1_speed(speed):
	rate = float(speed) / 100
	motor_1.write(rate)
	return 'Motor 1 set to %d' % speed

@app.route('/m2/<int:speed>')
def motor_2_speed(speed):
	rate = float(speed) / 100
	motor_2.write(rate)
	return 'Motor 2 set to %d' % speed
