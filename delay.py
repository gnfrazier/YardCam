"""Calcs delay for tracking sunrise and sunset.
Requires local file of loc.py with Wunderground API key"""

import loc
import requests
import arrow


def now():
    time = arrow.utcnow().to('US/Eastern')

    return time


def get_local():
    lat = loc.lat()
    lon = loc.lon()
    wun = loc.wun()
    alt = loc.alt()

    return (lat, lon, alt, wun)


def get_astro():
    local = get_local()

    url = 'http://api.wunderground.com/api/' + local[3] + \
        '/astronomy/q/' + local[0] + ',' + local[1] + '.json'

    rdata = requests.get(url)
    data = rdata.json()
    return data


def sunrise(data=None):

    if not data:
        data = get_astro()
    # data.keys() returns keys
    sunrise = (data['sun_phase']['sunrise'])  # returns dict of sunrise time

    return sunrise


def sunset(data=None):

    if not data:
        data = get_astro()
    # data.keys() returns keys
    sunset = (data['sun_phase']['sunset'])  # returns dict of sunrise time

    return sunset


def main():

    rdata = rise(lat, lon, alt, wun)

    return rdata

if __name__ == '__main__':
    main()
