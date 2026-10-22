import RPi.GPIO as GPIO 
class PWM_DAC: 
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False): 
        self.gpio_pin = gpio_pin 
        self.pwm_frequency = pwm_frequency 
        self.dynamic_range = dynamic_range 
        self.verbose = verbose 
        
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial=0)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency) 
        self.pwm.start(0) 
    def deinit(self): 
        self.pwm.stop() 
        GPIO.output(self.gpio_pin, 0) 
        GPIO.cleanup() 
        
    def set_voltage(self, voltage): 
        if not (0.0 <= voltage <= self.dynamic_range): 
            if self.verbose: 
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)") 
                print("Устанавливаем 0.0 В") 
                self.pwm.ChangeDutyCycle(0) 
                return 
        duty_cycle = voltage / self.dynamic_range * 100 
        if self.verbose: print(f"Коэффициент заполнения ШИМ: {duty_cycle:.2f}%, напряжение: {voltage:.3f} B")

        self.pwm.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__": 
    dac = None 
    try: 
        dac = PWM_DAC(12, 500, 3.290, True) 
        while True: 
            try: 
                voltage = float(input("Введите напряжение в Вольтах: ")) 
                dac.set_voltage(voltage) 
            except ValueError: 
                print("Вы ввели не число. Попробуйте ещё раз\n") 
    finally: 
        if dac is not None: 
            dac.deinit()