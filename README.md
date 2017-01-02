# YardCam
###PiCamera for my backyard

I have a backyard. I have a window. I have a RaspberryPi Zero. Add a ZeroView Pi mount and PiCamera.

###Requirements:
Python 3.4 or higher, Requests, Arrow, PiCamera.

Wunderground.com API key.

loc.py Update with your latitude and longitude and a free Wunderground.com API key. Altitude is not required. Adding your Wunderground timezone will reduce API calls but is not required.

###Installation
Create a new directory.  
A fresh python env is highly recommended.  
Unzip files.  
From command prompt in the directory you created type:  
python3 capture.py  

###Program Flow
Capture.py uses delay.py to calculate the current local sunrise and sunset times retrieved from wunderground.com. A preset offset time begins capture before or after sunrise/set. Capture.py waits until the time then takes the number of photos noted in the capture loop. Photos will be named with the date and time of day. 

