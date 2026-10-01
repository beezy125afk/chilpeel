import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM) 
led = 26 
GPIO.setup(led, GPIO.OUT) 
pwm = GPIO.PWM(led, 200) 
duty = 0.0 
pwm.start(duty) 

try: 
    while True: 
        pwm.ChangeDutyCycle(duty) 
        time.sleep(0.05) 
        duty += 1.0 
        if duty > 100.0: 
            duty = 0.0 
except KeyboardInterrupt: 
    pass 
finally: 
    GPIO.cleanup()