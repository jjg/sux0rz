from pyfirmata import Arduino, util
from flask import Flask, render_template

board = Arduino('/dev/ttyACM0')
motor_1 = board.get_pin('d:11:s')
motor_2 = board.get_pin('d:10:s')

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/m1/<string:speed>')
def motor_1_speed(speed):
        speed = int(speed)
	rate = ((speed + 100) * 180) / 200
	motor_1.write(rate)
	return 'Motor 1 set to %d' % rate 

@app.route('/m2/<string:speed>')
def motor_2_speed(speed):
        speed = int(speed)
	rate = ((speed + 100) * 180) / 200
	motor_2.write(rate)
	return 'Motor 2 set to %d' % rate 
