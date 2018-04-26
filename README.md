# YardCam

### PiCamera for my backyard

I have a backyard. I have a window. I have a [RaspberryPi Zero](https://thepihut.com/collections/raspberry-pi/products/raspberry-pi-zero-w). Add a [ZeroView](https://thepihut.com/products/zeroview) Pi mount and [PiCamera](https://thepihut.com/collections/raspberry-pi-camera/products/raspberry-pi-camera-module).

### Requirements:

Python 3.4 or higher, Requests, Arrow, PiCamera.

[Wunderground.com API key.](https://www.wunderground.com/weather/api)

config.ini Update with your latitude and longitude and a free [Wunderground.com API key.](https://www.wunderground.com/weather/api) Altitude is not required. Adding your Wunderground timezone will reduce API calls but is not required.

### Installation

Create a new directory.  
A fresh python env is highly recommended.  
git clone <https://github.com/gnfrazier/YardCam.git>
Update config.ini with api key and location information.

-   [Get your Wunderground API key](https://www.wunderground.com/weather/api/d/pricing.html)
    -   Free tier allows 500 calls per day, YardCam uses 2-4 calls per day.
-   Latitude and Longitude provide most accurate results
-   Postcode (zip code) uses the primary weather station from Wunderground

From command prompt in the directory you created type:  
python3 capture.py  

For best results use a cron job to start at reboot.

### Program Flow

Capture.py uses delay.py to calculate the current local sunrise and sunset times retrieved from wunderground.com. A preset offset time begins capture before or after sunrise/set. Capture.py waits until the time then takes the number of photos noted in the capture loop. Photos will be named with the date and time of day. 
