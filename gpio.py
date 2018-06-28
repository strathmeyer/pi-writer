from gpiozero import PWMLED, Button
from itertools import cycle
from signal import pause

import os

# Brightness
screen = PWMLED(18, initial_value=1)
brightness_down_button = Button(17)
brightness_up_button = Button(22)
brightnesses = [0, 0.1, 0.2, 0.5, 1]
brightness_index = -1 % len(brightnesses)

def brightness_down():
  global brightness_index
  brightness_index = (brightness_index - 1) % len(brightnesses)
  screen.value = brightnesses[brightness_index]

brightness_down_button.when_pressed = brightness_down

def brightness_up():
  global brightness_index
  brightness_index = (brightness_index + 1) % len(brightnesses)
  screen.value = brightnesses[brightness_index]

brightness_up_button.when_pressed = brightness_up


# Shutdown
shutdown_button = Button(27, hold_time=4, hold_repeat=False)

def shutdown():
  os.system('sudo shutdown now')

shutdown_button.when_held = shutdown

pause()
