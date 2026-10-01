import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
led = 26 
GPIO.setup(led, GPIO.OUT)
svet = 6 
GPIO.setup(svet, GPIO.IN)
while True: 
    input1 = GPIO.input(svet) 
    GPIO.output(led, not input1)
    time.sleep(0.2)