#!/usr/bin/python

import time
from dotstar import Adafruit_DotStar

colors = ['#e70000', '#e80700', '#ea0d00', '#eb1400', '#ec1b00', '#ed2200', '#ef2900', '#f03100', '#f13800', '#f23f00', '#f44600', '#f54e00', '#f65500', '#f75d00', '#f96500', '#fa6c00', '#fb7400', '#fc7c00', '#fe8400', '#ff8c00', '#ff9100', '#ff9600', '#ff9c00', '#ffa100', '#ffa600', '#ffab00', '#ffb000', '#ffb600', '#ffbb00', '#ffc000', '#ffc500', '#ffcb00', '#ffd000', '#ffd500', '#ffda00', '#ffdf00', '#ffe500', '#ffea00', '#ffef00', '#f7f800', '#e0f200', '#c9eb00', '#b4e400', '#a0de00', '#8cd700', '#7ad100', '#68ca00', '#57c300', '#47bd00', '#38b600', '#2aaf00', '#1da900', '#11a200', '#059c00', '#009505', '#008e0f', '#008817', '#00811f', '#00882b', '#008e39', '#009547', '#009c56', '#00a267', '#00a978', '#00af8b', '#00b69e', '#00bdb3', '#00bec3', '#00b5ca', '#00aad1', '#009fd7', '#0092de', '#0085e4', '#0076eb', '#0066f2', '#0056f8', '#0044ff', '#0034f9', '#0024f3', '#0015ec', '#0007e6', '#0700e0', '#1300da', '#1f00d4', '#2b00cd', '#3500c7', '#3f00c1', '#4800bb', '#5000b4', '#5800ae', '#5f00a8', '#6500a2', '#6a009c', '#6f0095', '#73008f', '#760089', '#56008e', '#330093', '#0e0098', '#00199d', '#0044a2', '#0070a7', '#00a0ac', '#00b190', '#00b665', '#00ba38', '#00bf09', '#29c400', '#5ec900', '#95ce00', '#ced300', '#d8a600', '#dd7100', '#e23a00'] 
factor = 2  # multiple of number of colors
numColors = len(colors)
numPixels = numColors * factor 

# Here's how to control the strip from any two GPIO pins:
datapin = 17
clockpin = 27
strip = Adafruit_DotStar(numPixels, datapin, clockpin)

# Alternate ways of declaring strip:
# strip   = Adafruit_DotStar(numpixels)           # Use SPI (pins 10=MOSI, 11=SCLK)
# strip   = Adafruit_DotStar(numpixels, 32000000) # SPI @ ~32 MHz
# strip   = Adafruit_DotStar()                    # SPI, No pixel buffer
# strip   = Adafruit_DotStar(32000000)            # 32 MHz SPI, no pixel buf

strip.begin()           # Initialize pins for output
strip.setBrightness(64)  # Limit brightness to ~1/4 duty cycle

change_every = int(numPixels / numColors)

def getRGB(h):
    cs = h.lstrip('#')
    return tuple(int(cs[i:i+2], 16) for i in (0, 2, 4))


every_pixel = []
for i in range(numPixels):
    pixel = int(i / change_every)
    every_pixel.append(colors[pixel])
print numColors

while True:
    for i in range(len(every_pixel)):
        rgb = getRGB(every_pixel[i-1])
        strip.setPixelColor(i, rgb[0], rgb[1], rgb[2])
    last_value = every_pixel.pop()
    every_pixel.insert(0, last_value)
    strip.show()                     # Refresh strip
    time.sleep(0.13)
