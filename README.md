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
python3 yardcam.py  

###Program Flow  
Yardcam.py is an event loop, it  uses delay.py to calculate the current local sunrise and sunset times retrieved from wunderground.com. A preset offset time begins capture before or after sunrise/set. The event loop waits then triggers Capture.py. Photos will be named with the date and time of day. A single copy of latest is created on every capture.  

# FlyCam  
  
Created for constant timelapse photography, like catching a butterfly hatching.  
  
###Program Flow
Flycam.py is a more simple image capture loop. It uses image size to calculate when it is dark in the capture area, compressing the time of black or nearly black images.  


