Keylogger.py is the script that is ran on the device that is getting keylogged. 
Sends contents of keylog file to local server on port 5000.
Flask_server.py is local server displayed on port 5000, allows other users on local network to view logs sent by key logger on http://x.x.x.x:5000 (device hosting flask server).
