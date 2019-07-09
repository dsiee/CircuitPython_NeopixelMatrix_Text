# CircuitPython_NeopixelMatrix_Text
A CircuitPython Library that allows scrolling text to be displayed on a neopixel matrix (or other ws2812). Tested on CircuitPython 4 with a 8x8 ws2812 matrix. 


This requires the neopixel and adafruit_framebuf libraries to also be installed.

To use:
1.  import NeoMat_Text.
2.  initalise e.g:
mat = NeoMat_Test.Matrix(pin, width, height, color)
3. pass it text to the .scroll function e.g:
mat.scroll("Banana")

The text currently scrolls as fast as it can (about .5s per frame on an nrf52840 running circuitpython 4.0.1)

See examples for a usable example.
