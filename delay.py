"""Calcs delay for tracking sunrise and sunset.
Requires local file of loc.py with Wunderground API key"""

import loc
import requests
import arrow


def now(timezone=None):

    if not timezone:
        get_timezone()

    time = arrow.now(timezone)

    return time


def get_timezone():
    data = get_wund('yesterday')
    timezone = data['history']['date']['tzname']

    return timezone


def get_local():
    lat = loc.lat()
    lon = loc.lon()
    wun = loc.wun()
    alt = loc.alt()

    return (lat, lon, alt, wun)


def get_wund(call='astronomy'):
    local = get_local()

    url = 'http://api.wunderground.com/api/' + local[3] + '/' + \
        call + '/q/' + local[0] + ',' + local[1] + '.json'

    rdata = requests.get(url)
    data = rdata.json()
    return data


def sunrise(data=None):

    if not data:
        data = get_wund('astronomy')
    # data.keys() returns keys
    sunrise = (data['sun_phase']['sunrise'])  # returns dict of sunrise time

    return sunrise


def event_time(event):
    time = now()
    ehour = int(event['hour'])
    emin = int(event['minute'])
    etime = time.replace(hour=ehour, minute=emin)
    if etime < time:
        etime = etime.replace(days=1)
    return etime


def sunset(data=None):

    if not data:
        data = get_wund('astronomy')
    # data.keys() returns keys
    sunset = (data['sun_phase']['sunset'])  # returns dict of sunset time
    sunset = event_time(sunset)

    return sunset


def main():

    rdata = rise(lat, lon, alt, wun)

    return rdata

if __name__ == '__main__':
    main()
