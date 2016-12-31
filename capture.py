#!/usr/bin/python3

from picamera import PiCamera
import time


def setup():
    camera.start_preview()
    camera.resolution = (1640, 1232)
    time.sleep(3)
    return True


def shutdown():
    camera.stop_preview()
    return False


def cap(status):
    if not status:
        status = setup()
        camera.capture(
            '/home/pi/Pictures/capture-10{counter:03d}.jpg')

    else:
        camera.capture(

            '/home/pi/Pictures/capture-10{counter:03d}.jpg')

    print('Photo Taken')
    return status


def capx(status):
    print('Photo Taken')
    return True


def main():

    camera = PiCamera()
    status = setup()
    images = 120
    if status:
        for filename in camera.capture_continuous('rise{counter:03d}.jpg'):

            time.sleep(60)
            images = images - 1
            if images == 0:
                break
    status = shutdown()

if __name__ == '__main__':
    main()
