#!/usr/bin/python3

import capture
from picamera import PiCamera
import time


def image_cap_loop(camera, status=None):
    """Set image parameters, capture image, set wait time, repeat"""

    resolution = (854, 480)
    camera.rotation = 90
    latest = capture.cap(camera, resolution, status)
    status = latest[0]
    size = capture.image_size(latest[1])
    capture.copy_latest(latest[1])
    day = 150000  # image size when light is good
    if size > day:
        wait = 60
    else:
        wait = 600
        status = capture.shutdown(camera)
    print('Next capture begins in {} seconds.'.format(wait))
    time.sleep(wait)

    # status = capture.shutdown(camera)
    image_cap_loop(camera, status)

    return latest


def main():

    camera = PiCamera()
    image_cap_loop(camera)
    print("Images captured")


if __name__ == '__main__':
    main()
