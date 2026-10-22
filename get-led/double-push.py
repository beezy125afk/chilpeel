import RPi.GPIO as GPIO 
import time


GPIO.setmode(GPIO.BCM) 
leds = [16, 12, 25, 17, 27, 23, 22, 24] 
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
        up = GPIO.input(BUTTON_UP)
        down = GPIO.input(BUTTON_DOWN)

        if up and down: 
            num = 255
            change = True
        elif up:
            num += 1
            change = True 
        elif down:
            num -= 1 
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
