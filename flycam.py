import capture
from picamera import PiCamera
import time


def image_cap_loop(camera):
    """Set image parameters, capture image, set wait time, repeat"""

    images = 18
    status = None
    resolution = (854, 480)

    latest = capture.cap(camera, resolution, status)
    status = latest[0]
    size = capture.image_size(latest[1])
    day = 1000  # image size when light is good
    if size > day:
        wait = 60
    else:
        wait = 600
        status = capture.shutdown(camera)
    print('Next capture begins in {} seconds.'.format(wait))
    time.sleep(wait)

    # status = capture.shutdown(camera)
    image_cap_loop(camera)


def main():

    camera = PiCamera()
    image_cap_loop(camera)
    print("Images captured")


if __name__ == '__main__':
    main()
