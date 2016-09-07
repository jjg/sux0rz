# Requirements

*  mjpg_streamer
*  pyfirmata

# Running the server

If you want the video feeed to work, mjpg_streamer needs to be running:

    ./mjpg_streamer -i "./input_raspicam.so -fps 15" -o "./output_http.so" 

The code is hard-coded to the hostname `sux0rz.local`, you may need to change this until I figure out a good way to make it dynamic.

Next you need to set a few environment variables:

*  `export FLASK_APP=brainz.py`
*  `export FLASK_DEBUG=1`

Then start flask:

`flask run --host=<your local IP address>`

The app will start-up and you should be able to load the controller by pointing a browser at 

	http://<your local IP address>:5000/

# Reference
*  Setting up the video stream: https://github.com/foosel/OctoPrint/wiki/Setup-on-a-Raspberry-Pi-running-Raspbian
