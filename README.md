# YardCam
###PiCamera for my backyard

I have a backyard. I have a window. I have a RaspberryPi Zero. Add a ZeroView Pi mount and PiCamera.

###Requirements:
Python 3.4 or higher, Requests, Configparser, Arrow, PiCamera.

Wunderground.com API key.

Edit config.ini to match your specific location and your wunderground.com API key . Latitude and longitude are required, zip code conversion is not supported. Adding your timezone in the same format as wunderground will reduce API calls but is not required.

###Installation
Create a new directory.  
A fresh python env is highly recommended.  
Unzip files.  
Edit config.ini with your API key and lat/long
From command prompt in the directory you created type:  
python3 capture.py  

###Program Flow
Capture.py uses delay.py to calculate the current local sunrise and sunset times retrieved from wunderground.com. A preset offset time begins capture before or after sunrise/set. Capture.py waits until the time then takes the number of photos noted in the capture loop. Photos will be named with the date and time of day. 

