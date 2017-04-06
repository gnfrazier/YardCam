import capture
from picamera import PiCamera
import time
import delay


def image_cap_loop(camera, status=None):
    """Set image parameters, capture image, set wait time, repeat"""

    resolution = (1640, 1232)
    # wait = delay.next_capture()  # Delay time in seconds from delay.py
    wait = 60
    waithours = wait / 60 / 60  # Convert seconds to hours
    print('Next capture begins in {} hours.'.format(waithours))
    time.sleep(wait)
    images = 18

    for i in range(images):
        latest = capture.cap(camera, resolution, status)
        status = latest[0]
        capture.copy_latest(latest[1])
        time.sleep(300)

    status = camera.shutdown(camera)
    image_cap_loop(camera, status)
    return latest


def main():

    camera = PiCamera()
    image_cap_loop(camera)
    print("Images captured")


if __name__ == '__main__':
    main()
