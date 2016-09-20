import socket
from pyfirmata import Arduino, util
from flask import Flask, render_template

board = False

try:
    board = Arduino('/dev/ttyACM0')
except:
    board = False
    print 'No board attached, running in debug mode.'

if board:
    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    motor_1 = board.get_pin('d:11:s')
    motor_2 = board.get_pin('d:10:s')

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html', server_ip=socket.getfqdn())

@app.route('/m1/<string:speed>')
def motor_1_speed(speed):
        speed = int(speed)
	rate = ((speed + 100) * 180) / 200
        if board:
	    motor_1.write(rate)
	return 'Motor 1 set to %d' % rate 

@app.route('/m2/<string:speed>')
def motor_2_speed(speed):
        speed = int(speed)
	rate = ((speed + 100) * 180) / 200
        if board:
	    motor_2.write(rate)
	return 'Motor 2 set to %d' % rate 
