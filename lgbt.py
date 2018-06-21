#!/usr/bin/python

import time
from dotstar import Adafruit_DotStar

numpixels = 72 # Number of LEDs in strip

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

#rgb = [[231, 0, 0],[243, 70, 0],[255, 140, 0],[255, 190, 0],[255, 239, 0],[128, 184, 15],[0, 129, 31],[0, 98, 143],[0, 68, 255],[255, 0, 131], [59, 34, 196], [174, 0, 69]]
hexx = ['e70000', 'f34600', 'ff8c00', 'ffbe00', 'ffef00', '80b80f', '00811f', '00628f', '0044ff', '3b22c4', '760089', 'ae0045']
change_every = int(numpixels / len(hexx))

def getRGB(h):
    return tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))

every_pixel = []
for i in range(numpixels):
    xx = int(i / change_every)
    #every_pixel.append([rgb[xx][0], rgb[xx][1], rgb[xx][2]])
    every_pixel.append(hexx[xx])

while True:
    for i in range(len(every_pixel)):
        rgb = getRGB(every_pixel[i])
        strip.setPixelColor(i, rgb[0], rgb[1], rgb[2])
    last_value = every_pixel.pop()
    every_pixel.insert(0, last_value)
    strip.show()                     # Refresh strip
    time.sleep(0.03)

