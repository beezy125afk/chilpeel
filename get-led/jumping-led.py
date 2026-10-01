import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM) 

leds = [16, 12, 25, 17, 27, 23, 22, 24] 
GPIO.setup(leds, GPIO.OUT) 
GPIO.output(leds, 0) 

light_time = 0.2 


try: 
    while True: 
        for led in leds: 
            GPIO.output(led, 1) 
            time.sleep(light_time) 
            GPIO.output(led, 0)

        for led in reversed(leds[1:-1]): 
            GPIO.output(led, 1) 
            time.sleep(light_time) 
            GPIO.output(led, 0) 
except KeyboardInterrupt: 
    pass 
finally: 
    GPIO.cleanup()