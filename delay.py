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
    """Wunderground call to get local timezone"""

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
    """Returns dict of sunrise time"""

    if not data:
        data = get_wund('astronomy')
    # data.keys() returns keys
    sunrise = (data['sun_phase']['sunrise'])  # returns dict of sunrise time

    return sunrise


def sunset(data=None):
    """Returns dict of sunset time"""

    if not data:
        data = get_wund('astronomy')
    # data.keys() returns keys
    sunset = (data['sun_phase']['sunset'])  # returns dict of sunset time
    sunset = event_time(sunset)

    return sunset


def event_time(event):
    """Transform event dict to time object"""

    time = now()
    ehour = int(event['hour'])
    emin = int(event['minute'])
    etime = time.replace(hour=ehour, minute=emin)
    if etime < time:
        etime = etime.replace(days=1)
    return etime


def main():

    rdata = rise(lat, lon, alt, wun)

    return rdata

if __name__ == '__main__':
    main()
