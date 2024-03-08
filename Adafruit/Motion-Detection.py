from time import sleep
import board
import adafruit_lis3dh
import busio
import neopixel

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
lis3dh.range = adafruit_lis3dh.RANGE_8_G
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)

# x is left-right
# y is backward-forward
# z is down-up

n = 0.05
while True:
    pixels.fill((0,0,0))
    x1, y1, z1 = lis3dh.acceleration
    print((x1, y1, z1))
    sleep(0.5)
    x2, y2, z2 = lis3dh.acceleration
    x3 = x2 - x1
    y3 = y2 - y1
    z3 = z2 - z1
    if x3 > n:
        pixels[0] = (225, 0, 0)
    elif x3 < n:
        pixels[0] = (0, 225, 0)
    if y3 > n:
        pixels[1] = (225, 0, 0)
    elif y3 < n:
        pixels[1] = (0, 225, 0)
    if x3 > n:
        pixels[2] = (225, 0, 0)
    elif x3 < n:
        pixels[2] = (0, 225, 0)
