import RPi.GPIO as GPIO
import time

#~ pin = 12 #Board
pin = 14 #BCM

#~ GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm=GPIO.PWM(pin,50)
pwm.start(0)

def setAngle(angle):
	realAngle = angle*(11-2.7)/180 + 2.7
	GPIO.output(pin,True)
	pwm.ChangeDutyCycle(realAngle)
	time.sleep(1)
	GPIO.output(pin,False)
	pwm.ChangeDutyCycle(0)

setAngle(45) #unlocking position
GPIO.cleanup()
print("unlocked")
