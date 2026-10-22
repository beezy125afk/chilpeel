import RPi.GPIO as GPIO

dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT, initial=0)

dynamic_range = 3.162

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 B")
        return 0
    
    return int(voltage / dynamic_range * 255)
    
def number_to_dac(number):
    for bit, pin in enumerate(dac_bits):
        GPIO.output(pin, (number >> bit) & 1)
try:
    while True: 
        try: 
             voltage = float(input("Введите напряжение в Вольтах: ")) 
             number = voltage_to_number(voltage) 
             number_to_dac(number) 
             
        except ValueError: 
                print("Вы ввели не число. Попробуйте ещё раз\n")

finally: 
    GPIO.output(dac_bits, 0) 
    GPIO.cleanup()
