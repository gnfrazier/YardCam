#!/usr/bin/python3

from picamera import PiCamera
import time
import arrow
import os
import delay


def setup(camera):
    """Starts preview, sets resolution, sleep allows time for sensor warming"""

    camera.start_preview()
    camera.resolution = (1640, 1232)
    time.sleep(3)
    return camera


def shutdown(camera):
    """Stops camera preview"""

    camera.stop_preview()
    return False


def path():
    """Checks for capture directory, creates if needed"""

    current = os.getcwd()
    destination = current + '/captures'
    if os.path.isdir(destination):
        print('Photos will be placed in {} directory.'.format(destination))
    else:
        os.mkdir(destination)
        print('Created directory {} for image captures.'.format(destination))

    return destination


def image_name():
    """Parses capture time into image name"""

    currtime = delay.now().format('YYYY-MM-DD-HH-mm-ss')
    name = 'img-' + currtime + '.jpg'
    destination = path()
    pathname = destination + '/' + name

    return pathname


def cap(camera, status=None):
    """Checks for setup, then captures photo"""

    if not status:
        status = setup(camera)

    imagename = image_name()
    camera.capture(imagename)
    print('Photo Taken {}.'.format(imagename))
    return status


def capx(status):
    """use for testing only"""

    imagename = image_name()
    print('TEST: Photo Taken {}.'.format(imagename))

    return True


def image_cap_loop(camera):
    """Loop get next event, then wait, capture, repeat"""

    wait = delay.next_capture()
    waithours = wait / 60 / 60
    print('Next capture begins in {} hours.'.format(waithours))
    time.sleep(wait)
    images = 18
    status = None

    for i in range(images):
        status = cap(camera, status)
        time.sleep(300)

    status = shutdown(camera)
    image_cap_loop(camera)


def main():

    camera = PiCamera()
    image_cap_loop(camera)
    print("Images captured")

if __name__ == '__main__':
    main()
