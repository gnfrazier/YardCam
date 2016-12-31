#!/usr/bin/python3

from picamera import PiCamera
import time


def setup():
    camera.start_preview()
    camera.resolution = (3280, 2464)
    time.sleep(5)
    return True


def shutdown():
    camera.stop_preview()
    return False


def cap(status):
    if not status:
        status = setup()
        camera.capture(
            '/home/pi/Documents/Pictures/capture-10{counter:03d}.jpg')

    else:
        camera.capture(
            '/home/pi/Documents/Picturesb/capture-10{counter:03d}.jpg')

    print('Photo Taken')
    return status


def capx(status):
    print('Photo Taken')
    return True


def main():

    camera = PiCamera()
    status = None

    status = shutdown()

if __name__ == '__main__':
    main()
