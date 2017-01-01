"""Calcs delay for tracking sunrise and sunset"""

import loc
import requests


def rise(lat, lon, alt, wun):

    url = 'http://api.wunderground.com/api/' + wun + \
        '/astronomy/q/' + lat + ',' + lon + '.json'

    rdata = requests.get(url)
    data = data.json()
    # data.keys() returns keys
    sunrise = (data['sun_phase']['sunrise'])  # returns dict of sunrise time

    return data


def main():
    lat = loc.lat()
    lon = loc.lon()
    wun = loc.wun()
    alt = loc.alt()
    rdata = rise(lat, lon, alt, wun)

    return rdata

if __name__ == '__main__':
    main()
