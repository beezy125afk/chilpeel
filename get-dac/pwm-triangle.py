import pwm_dac as pd

import signal_generator as sg
import time

amplitude = 1.5
signal_frequency = 12
sampling_frequency = 2000
dac = None
try:
    dac = pd.PWM_DAC(12, 500, 3.290, True)

    start_time = time.time()
   
    while True:
        current_time = time.time() - start_time
        normalized_amp = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
        voltage = (normalized_amp * amplitude)
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    if dac is not None:
        dac.deinit()