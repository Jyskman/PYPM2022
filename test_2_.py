from matplotlib import animation

import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation 
from pypm2 import _pypm2 as p

import LCD_1in44
import LCD_Config

from PIL import Image,ImageDraw,ImageFont,ImageColor


import RPi.GPIO as GPIO
KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13
KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

#init GPIO
GPIO.setmode(GPIO.BCM) 
# GPIO.cleanup()
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up


def LCD_config():
    LCD = LCD_1in44.LCD()

    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
    draw = ImageDraw.Draw(image)

    return LCD, image, draw



# from matplotlib.animation import FuncAnimation

# import seaborn as sns

def start():
    a = p.OPC_create()
    p.ISS_config(a)
    time.sleep(1)
    
    return a

# a = p.OPC_create()
# p.ISS_config(a)
# time.sleep(1)

def fan_test(a):

    p.OPC_fan_off(a)
    time.sleep(5)
    p.OPC_fan_off(a)
    time.sleep(1)
    p.OPC_fan_on(a)




def plot_config():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax1_2 = fig.add_subplot(1,2,2)
    return fig, axl, axl_2

def size_width(a):

    size = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
    dist = []

    size_return = p.OPC_return_ch(a)
#     size_list = size_return.tolist()
    size_list = list(size_return)

    size_mid = []
    size_width = []

    for x in range(len(size_list)-1):
        mid = (size_list[x]+size_list[x+1])/2
        size_mid.append(mid)
        current_width = size_list[x+1] - size_list[x]
        size_width.append(current_width)
    return size_mid, size_width, size_list



def animate_(LCD, a):
    
    dist = p.OPC_return_dist(a)  
    ax1.clear()
    ax1_2.clear()
#     ax1.plot(x[i],y[i])
    ax1.bar(size_mid,dist, width = size_width)
    ax1_2.bar(size_mid,dist)

    draw.rectangle([(0,0),(128,128)],fill = "WHITE")
    for x in range(len(dist)):
        
        if dist[x] > 0:
        
            draw.line([((x+10+x*3),(128)-20),((x+10)+x*3,(128-dist[x])-20)], fill = "BLUE",width = 1)
            draw.line([((x+10+x*3+1),(128)-20),((x+10)+x*3+1,(128-dist[x])-20)], fill = "BLUE",width = 1)
    LCD.LCD_ShowImage(image,0,0)

def LCD_animate(LCD, draw, image, a):
    run = 20
    x_base = 27
    y_base = 20
    
    y_max = 100
    line_offset_y = 3
    latch = False
    
    while run > 1:
        run = run - 1
        
        latch = False
        for x in range(20):
            time.sleep(0.05)
            if GPIO.input(KEY1_PIN) == 0 & latch == False:
                latch = True
                y_max = 50
            if GPIO.input(KEY2_PIN) == 0 & latch == False:
                latch = True
                y_max = 10
                

        dist = p.OPC_return_dist(a)     
        draw.rectangle([(0,0),(128,128)],fill = "WHITE")
        
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size =12)
        
        draw.text( (x_base-3,(128-y_base+6)),"0.4", fill = "RED",font=font )
        draw.text( (x_base-12,(128-y_base+0)),"0", fill = "RED",font=font )
        draw.text( (x_base-27,y_base-15),str(y_max), fill = "RED",font=font )
        
        draw.line([(x_base-2,(128)-y_base+line_offset_y),(x_base+3*len(dist)+len(dist),(128)-y_base+line_offset_y)], fill = "RED",width = 2)
        draw.line([(x_base-2,((128)-y_base)),(x_base-2,((128)-y_base) - 100)], fill = "RED",width = 2)
#         tickmarks
        draw.line([(x_base-2,((128)-y_base- 75)),(x_base-4,((128)-y_base) - 75)], fill = "RED",width = 2)
        draw.line([(x_base-2,((128)-y_base- 50)),(x_base-4,((128)-y_base) - 50)], fill = "RED",width = 2)
        draw.line([(x_base-2,((128)-y_base- 25)),(x_base-4,((128)-y_base) - 25)], fill = "RED",width = 2)
        draw.line([(x_base-2,((128)-y_base- 0)),(x_base-4,((128)-y_base) - 0)], fill = "RED",width = 2)
        draw.line([(x_base-2,((128)-y_base- 100)),(x_base-4,((128)-y_base) - 100)], fill = "RED",width = 2)
#         tickmarks x
        draw.line([(x_base + 0,(128-y_base+line_offset_y)+2 ),(x_base + 0,(128-y_base+line_offset_y)+2)], fill = "RED",width = 2)


        for x in range(len(dist)):
         
            if dist[x] > 0:
                y_val = dist[x] / (0.01*y_max)
                draw.line([((x+x_base+x*3),(128)-y_base),((x+x_base)+x*3,(128-y_val)-y_base)], fill = "BLUE",width = 1)
                draw.line([((x+x_base+x*3+1),(128)-y_base),((x+x_base)+x*3+1,(128-y_val)-y_base)], fill = "BLUE",width = 1)
                
        LCD.LCD_ShowImage(image,0,0)


def run_animation():

    ani = animation.FuncAnimation(fig,animate_,interval=1000)
    plt.show()

def LCD_clear(LCD):
    LCD.LCD_Clear()

a = start()
time.sleep(1)
size_mid, size_width, size_list = size_width(a)
LCD, image, draw = LCD_config()


# exec(open("test_3.py").read())