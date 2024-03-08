import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(40, GPIO.IN)

led = 5
switch = 40
switchState = 0
count = 0

while True:
    print("Count: ", count)
    GPIO.output(led, GPIO.input(switch))
    switchState = GPIO.input(switch)
    if switchState != 0:
       count += 1
       while switchState != 0:
           switchState = GPIO.input(switch)
           if switchState != 1:
               continue
