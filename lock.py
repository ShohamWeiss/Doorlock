import RPi.GPIO as GPIO
import time



#pin = 8 #Board
pin = 14 #BCM

#GPIO.setmode(GPIO.BOARD)
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

setAngle(135) #locking position
GPIO.cleanup()
#
##~ Update the database
#mariadb_connection = mariadb.connect(user='root', password='hhh', database='doorlock')
#cursor = mariadb_connection.cursor()
#query = "INSERT INTO status (user, position) VALUES" + user + ", 'locked');"
#cursor.execute(query)
