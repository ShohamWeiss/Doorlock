import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from rfid_lock import lock,unlock
import time
from screenshot import *

bell_pin = 36

reader = SimpleMFRC522()
correct_id = 802814104887 #Tag ID
GPIO.setup(8, GPIO.OUT)
GPIO.setup(bell_pin, GPIO.OUT)
try:
        screenshot()
        rfid,text = reader.read()
        print(rfid)
        if correct_id == rfid:
                # Unlock       
                # Wait for 10 seconds
                # Lock
                print("correct")
                unlock()
                time.sleep(5)
                lock()
        else:
                print("Wrong")
                GPIO.output(bell_pin,GPIO.HIGH)
                time.sleep(3)
                GPIO.output(bell_pin,GPIO.LOW)
except:
        print("some error")
finally:
        GPIO.cleanup()
