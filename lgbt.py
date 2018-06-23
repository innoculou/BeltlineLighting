#!/usr/bin/python

import time
from dotstar import Adafruit_DotStar

numpixels = 144  # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin = 17
clockpin = 27
strip = Adafruit_DotStar(numpixels, datapin, clockpin)

# Alternate ways of declaring strip:
# strip   = Adafruit_DotStar(numpixels)           # Use SPI (pins 10=MOSI, 11=SCLK)
# strip   = Adafruit_DotStar(numpixels, 32000000) # SPI @ ~32 MHz
# strip   = Adafruit_DotStar()                    # SPI, No pixel buffer
# strip   = Adafruit_DotStar(32000000)            # 32 MHz SPI, no pixel buf

strip.begin()           # Initialize pins for output
strip.setBrightness(64)  # Limit brightness to ~1/4 duty cycle

hexColor = [
    'e70000', 'ed2300', 'f34600', 'f96900',
    'ff8c00', 'ffa500', 'ffbe00', 'ffd600',
    'ffef00', 'bfd408', '80b80f', '409d17',
    '00811f', '007257', '00628f', '0053c7',
    '0044ff', '1e33e1', '3b22c4', '5811a7',
    '760089', '920067', 'ae0045', 'cb0022'
]

change_every = int(numpixels / len(hexColor))


def getRGB(h):
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


every_pixel = []
for i in range(numpixels):
    lenPixels = int(i / change_every)
    every_pixel.append(hexColor[lenPixels])

while True:
    for i in range(len(every_pixel)):
        rgb = getRGB(every_pixel[i])
        strip.setPixelColor(i, rgb[0], rgb[1], rgb[2])
    last_value = every_pixel.pop()
    every_pixel.insert(0, last_value)
    strip.show()                     # Refresh strip
    time.sleep(0.03)
