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
strip.setBrightness(192) # Limit brightness to ~1/4 duty cycle

# green, red, blue
h = raw_input('Enter hex: ').lstrip('#')
j = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
print j
for i in range(numpixels):
    strip.setPixelColor(i, j[0], j[1], j[2])

strip.show()                     # Refresh strip
