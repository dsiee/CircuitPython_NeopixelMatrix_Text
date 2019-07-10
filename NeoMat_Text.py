import board as board
import neopixel as neopixel
import adafruit_framebuf as adafruit_framebuf


class Matrix:
    def __init__(self, pin, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        pin = "board." + pin
        #this is a bad way to define the pin, but it works until a better way comes along 
        #we are turing off the auto write to have smoother animation without the visible filling of pixles
        self.pixels = neopixel.NeoPixel(eval(pin), self.width * self.height, auto_write=False)
        self.buffer = bytearray(round(self.width * self.height / 8))
        self.fb = adafruit_framebuf.FrameBuffer(self.buffer, self.width, self.height,
                                            buf_format=adafruit_framebuf.MVLSB)
                                            
    def neo_print_buffer(self, the_fb):
        #this simples goes through the frame buffer setting each pixel to either the color or off
        for y in range(the_fb.height):
            for x in range(the_fb.width):
                if self.fb.pixel(x, y):
                    self.pixels[y*8+x] = self.color
                else:
                    self.pixels[y*8+x] = [0,0,0] #turn off unused 

        
    def scroll(self, text):
        
        #iterate through every column, characters are 5 wide
        for i in range(len(text)*5+5): 
            #start with a bank frame buffer
            self.fb.fill(0) 
            #each time we refil the frame buffer with the text starting one place futher to the left so that 
            #the text scrolls towards the left (hence the -1)
            self.fb.text(text, -1*i, 0, True)
            self.neo_print_buffer(self.fb)
            self.pixels.show()
        else:
            #when finished turn all the LEDs off as sometimes the last column will be on
            self.fb.fill(0)
            self.neo_print_buffer(self.fb)
            self.pixels.show()
        
