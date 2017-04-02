import capture
from picamera import PiCamera



def image_cap_loop(camera):
    """Loop get next event, then wait, capture, repeat"""

    wait = delay.next_capture()
    waithours = wait / 60 / 60
    print('Next capture begins in {} hours.'.format(waithours))
    time.sleep(wait)
    images = 18
    status = None
    resolution = (854, 480)

    for i in range(images):
        status = camera.cap(camera, status)
        time.sleep(120)

    status = shutdown(camera)
    image_cap_loop(camera)


def main():

    camera = PiCamera()
    image_cap_loop(camera)
    print("Images captured")




if __name__ == '__main__':
        main()
