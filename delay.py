#!/usr/bin/python3

"""Calcs delay for tracking sunrise and sunset.
Requires local file of loc.py with Wunderground API key"""

import loc
import requests
import arrow


def now(timezone=None):
    """Returns local time"""

    if not timezone:
        get_timezone()

    time = arrow.now(timezone)

    return time


def get_timezone():
    """get timezone from loc or from wunderground"""

    timezone = loc.tz()
    if not timezone:

        data = get_wund('yesterday')
        timezone = data['history']['date']['tzname']

    return timezone


def get_local():
    """Inputs for location data"""
    # TODO convert to data file instead of function

    lat = loc.lat()
    lon = loc.lon()
    wun = loc.wun()
    alt = loc.alt()

    return (lat, lon, alt, wun)


def get_wund(call='astronomy'):
    """Makes call to wunderground API returns parsed JSON"""

    local = get_local()

    url = 'http://api.wunderground.com/api/' + local[3] + '/' + \
        call + '/q/' + local[0] + ',' + local[1] + '.json'

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
