#!/usr/bin/python3

"""Calcs delay for tracking sunrise and sunset.
Requires local file of config.ini with Wunderground API key"""

import requests
import arrow
import configparser

# TODO: Change to TOML instead of .ini
cfg = configparser.ConfigParser()
cfg.read('/home/pi/Documents/python/YardCam/config.ini')

local = {}


def now(timezone=None):
    """Returns local time"""

    if not timezone:
        get_timezone()

    time = arrow.now(timezone)

    return time


def get_timezone():
    """Get timezone from config.ini or from wunderground"""

    timezone = cfg['location']['timezone']
    if not timezone:

        data = get_wund('yesterday')
        timezone = data['history']['date']['tzname']

    return timezone


def get_local():
    """Inputs for location data"""

    local['lat'] = cfg['location']['latitude']
    local['lon'] = cfg['location']['longitude']
    local['wun'] = cfg['keys']['wunderground']
    local['alt'] = cfg['location']['altitude']

    return True  # (lat, lon, alt, wun)


def get_wund(call='astronomy'):
    """Makes call to wunderground API returns parsed JSON"""

    get_local()

    url = 'http://api.wunderground.com/api/' + local['wun'] + '/' + \
        call + '/q/' + local['lat'] + ',' + local['lon'] + '.json'

    rdata = requests.get(url)
    data = rdata.json()
    return data


def sunrise(data=None):
    """Returns seconds until sunrise capture time"""

    if not data:
        data = get_wund('astronomy')
    # data.keys() returns keys
    sunrise = (data['sun_phase']['sunrise'])  # returns dict of sunrise time
    etime = event_time(sunrise)
    timetoevent = calc_delay(etime)
    # start capturing an hour after sunrise
    delay = timetoevent + 3600

    return delay


def sunset(data=None):
    """Returns seconds until sunset capture time"""

    if not data:
        data = get_wund('astronomy')
    # data.keys() returns keys
    sunset = (data['sun_phase']['sunset'])  # returns dict of sunset time
    etime = event_time(sunset)
    timetoevent = calc_delay(etime)
    # start capturing an hour before sunset
    delay = timetoevent - 3600

    return delay


def event_time(event):
    """Transform event dict to time object"""

    time = now()
    ehour = int(event['hour'])
    emin = int(event['minute'])
    etime = time.replace(hour=ehour, minute=emin)
    if etime < time:
        etime = etime.replace(days=1)
    return etime


def calc_delay(etime):
    """Return time  in seconds until next event"""

    currenttime = now()
    delta = etime.timestamp - currenttime.timestamp
    return delta


def next_capture():
    """Returns delay seconds to capture time"""

    data = get_wund('astronomy')
    risedelay = sunrise(data)
    setdelay = sunset(data)

    delay = min([risedelay, setdelay])

    return delay


def main():

    delay = next_capture()

    return delay


if __name__ == '__main__':
    main()
