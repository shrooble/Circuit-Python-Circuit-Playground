import board
import digitalio
import time
from time import sleep

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    sleep(0.1)
    led.value = False
    sleep(0.1)
