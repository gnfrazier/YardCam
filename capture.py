from picamera import PiCamera
import time

def setup():
    camera.start_preview()
    time.sleep(5)
    return True

def shutdown():
    camera.stop_preview()
    return False

def cap(status):
    if not status:
        status = setup()
        camera.capture('/home/pi/Documents/python/cam/capture-10%s.jpg')

    else:
        camera.capture('/home/pi/Documents/python/cam/capture-10%s.jpg')

    print('Photo Taken')
    return status


camera = PiCamera()
status = None
for i in range(5):
    cap(status)
    time.sleep(5)

status = shutdown()

