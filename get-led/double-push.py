import RPi.GPIO as GPIO 
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) 
leds = [16, 5, 25, 17, 27, 23, 22, 24] 
GPIO.setup(leds, GPIO.OUT) 
GPIO.output(leds, GPIO.LOW) 
BUTTON_UP = 9 
BUTTON_DOWN = 10 
GPIO.setup(BUTTON_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(BUTTON_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
num = 0 
sleep_time = 0.2 
def dec2bin(value): 
    return [int(element) for element in bin(value)[2:].zfill(8)] 

try: 
    while True: 
        change = False 
        if GPIO.input(BUTTON_UP): 
            num = num + 1 
            change = True 
        elif GPIO.input(BUTTON_DOWN):
            num = num - 1 
            change = True 
            
        if change: 
            if num > 255 or num < 0: 
                num = 0 
            print(num, dec2bin(num)) 
            time.sleep(sleep_time) 

            
        GPIO.output(leds, dec2bin(num)) 
        time.sleep(0.01) 
except KeyboardInterrupt: 
    pass 
finally: 
    GPIO.cleanup()