from picamera import PiCamera
from time import sleep

camera= PiCamera()
camera.resolution = camera.MAX_RESOLUTION

#camera.start_preview()
#sleep(2)

while True:
    camera.capture('/var/www/html/img/livePic.jpg')
    #Bearbeitung des Bildes, Raender schneiden etc.
    sleep(5)

#camera.stop_preview()