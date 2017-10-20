#!/usr/bin/python

import time
from dotstar import Adafruit_DotStar

numpixels = 230 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin   = 17
clockpin  = 27
strip     = Adafruit_DotStar(numpixels, datapin, clockpin)

# Alternate ways of declaring strip:
# strip   = Adafruit_DotStar(numpixels)           # Use SPI (pins 10=MOSI, 11=SCLK)
# strip   = Adafruit_DotStar(numpixels, 32000000) # SPI @ ~32 MHz
# strip   = Adafruit_DotStar()                    # SPI, No pixel buffer
# strip   = Adafruit_DotStar(32000000)            # 32 MHz SPI, no pixel buf

# Append "order='gbr'" to declaration for proper colors w/older DotStar strips)

strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

rgb = [[255, 0, 0],[255, 84, 0],[255, 233, 0],[182, 255, 0],[106, 255, 0],[0, 255, 89],[0, 242, 255],[0, 4, 255],[170, 0, 255],[255, 0, 131]]
change_every = int(numpixels / len(rgb))

every_pixel = []
for i in range(numpixels):
    every_pixel.append([rgb[int(i / change_every)][1], rgb[int(i / change_every)][2], rgb[int(i / change_every)][0]])

while True:
    for i in range(len(every_pixel)):
        strip.setPixelColor(i, every_pixel[i][0], every_pixel[i][1], every_pixel[i][2])
    last_value = every_pixel.pop()
    every_pixel.insert(0, last_value)
    strip.show()                     # Refresh strip
    time.sleep(0.03)
