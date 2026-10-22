import RPi.GPIO as GPIO 
class R2R_DAC: 
    def __init__(self, gpio_bits, dynamic_range, verbose=False): 
        self.gpio_bits = gpio_bits 
        self.dynamic_range = dynamic_range 
        self.verbose = verbose 
        
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0) 

    def deinit(self):
        GPIO.output(self.gpio_bits, 0) 
        GPIO.cleanup()

    def set_number(self, number): 
        for bit, pin in enumerate(reversed(self.gpio_bits)): 
            GPIO.output(pin, (number >> bit) & 1) 
    
    def set_voltage(self, voltage): 
        if not (0.0 <= voltage <= self.dynamic_range): 
            if self.verbose: 
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)") 
                print("Устанавливаем 0.0 В")
            self.set_number(0) 
            return
            
        number = int(voltage / self.dynamic_range * 255) 
        if self.verbose: 
            real_voltage = number * self.dynamic_range / 255 
            print(f"Число на входе ЦАП: {number} (0b{number:08b}), напряжение: {real_voltage:.3f} В") 
        self.set_number(number) 
if __name__ == "__main__": 
    dac = None 
    try: 
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True) 
        
        while True: 
            try: 
                voltage = float(input("Введите напряжение в Вольтах: ")) 
                dac.set_voltage(voltage) 

            except ValueError: 
                print("Вы ввели не число. Попробуйте ещё раз\n") 
    finally: 
        if dac is not None: 
            dac.deinit()
