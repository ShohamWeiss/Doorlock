from picamera import PiCamera
import numpy as np
import time, datetime, os, shutil

# $ pip install picamera
# $ raspistill -o cam.jpg # test camera is working

def screenshot():
    if not os.path.isdir('./pic'):
        os.makedirs('pic')
        
    WIDTH = 640   
    HEIGHT = 480
    camera = PiCamera()
    camera.resolution = (WIDTH,HEIGHT)
    camera.vflip= True
    time.sleep(0.1) # camera warmup

    # save headshot of all invaders
    timestamp = str(datetime.datetime.now()).replace(' ', '_').replace(':', '_').replace('.', '_').replace('-', '_')
    img_name = './pic/invader_'+timestamp+'.jpg'
    camera.capture(img_name)
    
    # update the most recent invader image
    shutil.copyfile(img_name, '/var/www/html/invader.jpg')
    
    camera.close()
    
if __name__ == '__main__':
    screenshot()
