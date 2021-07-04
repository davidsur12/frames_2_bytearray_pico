from machine import Pin, I2C 
from ssd1306 import SSD1306_I2C
import framebuf
import os
from time import sleep


i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

def str_list_to_int_list(str_list ):
    n = 0
    while n < len(str_list):
       
        str_list[n] = int(str_list[n] )
        n += 1
    return(str_list)

def main():
    
    i=1;
    with open("bitearray3.txt"  , "r") as tf:
        lines1 = (tf.read().split(','))
        
    with open("bitearray4.txt"  , "r") as tf:
        lines2 = (tf.read().split(','))
        
    with open("bitearray5.txt"  , "r") as tf:
        lines3 = (tf.read().split(','))
        
        
   
       
    str_list_to_int_list(lines1)
    str_list_to_int_list(lines2)
    str_list_to_int_list(lines3)
    
    
    
    
    listaa1=bytearray(lines1)
    listaa2=bytearray(lines2)
    listaa3=bytearray(lines3)
   
   
    
    
    
    
    fb1=framebuf.FrameBuffer(listaa1 , 128 , 64  , framebuf.MONO_HLSB);
    fb2=framebuf.FrameBuffer(listaa2 , 128 , 64  , framebuf.MONO_HLSB);
    fb3=framebuf.FrameBuffer(listaa3 , 128 , 64  , framebuf.MONO_HLSB);
   
    
    
    
    while True:
        oled.fill(0);
        oled.blit(fb1 , 0 , 0)
        oled.show()
        
        oled.fill(0);
        oled.blit(fb2 , 0 , 0)
        oled.show()
        
        oled.fill(0);
        oled.blit(fb3 , 0 , 0)
        oled.show()
        #sleep(100)
        
           
                
if __name__== '__main__':
    main(); 
