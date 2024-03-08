from time import sleep
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.01)

n = 0.5
x = y = z = a = 0
while True:
    pixels[x] = (255, 0, 0)
    pixels[y + 1] = (0, 255, 255)
    pixels[z + 3] = (0, 255, 0)
    pixels[a + 4] = (0, 255, 0)
    sleep(n)
    pixels.fill((0, 0, 0))
    sleep(n)
    x += 1
    y +=1
    z += 1
    a +=1
    if x == 10:
        x = 0
    if y == 9:
        y = -1
    if z == 7:
        z = -3
    if a == 6:
        a = -4
