from gpiozero import PWMLED, Button
from itertools import cycle
from signal import pause

import os

# Brightness
screen = PWMLED(18, initial_value=1)
brightness_button = Button(17)
options = cycle([0, 0.1, 0.2, 0.5, 1])

def next_brightness():
  screen.value = next(options)

brightness_button.when_pressed = next_brightness


# Shutdown
shutdown_button = Button(27, hold_time=5, hold_repeat=False)

def shutdown():
  os.system('sudo shutdown now')

shutdown_button.when_held = shutdown

pause()
