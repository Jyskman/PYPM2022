from threading import Thread
import threading

import datetime
import numpy as np
import time
import csv
data = []
data_np = []
iterator = 0
operation = True
Reset = False
lock = threading.Lock()
shutdown = False
switch = False
dist_list = []
current_time =[]

path = "/home/pi/Documents/PYPM2022/testdata/"
file = "test.csv"
test = 0


def LCD_animate(LCD, draw, image, a):
    global iterator
    global data
    global data_np
    First_run = True
    global Reset
    global iterator
    global operation
    global shutdown
    global switch 
    global dist_list
    
    run = 30
    x_base = 27
    y_base = 20
    
    y_max = 100
    line_offset_y = 3
    latch = False
    
    x_max = len(size_mid)
    x_max_factor = 3
    bar_factor = 1
    x_correction = 0
    x_state = 0
    y_state = 0
    y_range = [10,40,100,200,400]
    while operation == True:
        if switch == True:
    #         run = run - 1
            iterator = iterator + 1
            switch = False
            latch = False
            
            for x in range(20):
                time.sleep(0.05)
                if GPIO.input(KEY_UP_PIN) == 1 & latch == False:
                    latch = True
    #                 y_max = 100
                    y_state = y_state + 1
                    if y_state > len(y_range)-1:
                        y_state = 0
                if GPIO.input(KEY_DOWN_PIN) == 1 & latch == False:
                    latch = True
                    y_state = y_state - 1
                    if y_state < 0:
                        y_state = len(y_range) -1
    #                 y_max = 40
                if GPIO.input(KEY3_PIN) == 0 & latch == False:
                    latch = True
    #                 y_max = 10
                    y_state = y_state - 1
                if GPIO.input(KEY_LEFT_PIN) == 1 & latch == False:
                    latch = True
                    x_state = x_state + 1
                    if x_state > 3:
                        x_state = 0
                if GPIO.input(KEY_RIGHT_PIN) == 1 & latch == False:
                    latch = True
                    x_state = x_state - 1
                    if x_state < 0:
                        x_state = 3
                if GPIO.input(KEY1_PIN) == 1 & latch == False:
                    shutdown = True

            y_max = y_range[y_state]
            dist = p.OPC_return_dist(a)
            dist_ = np.array(dist)
            
            lock.acquire()
            if First_run == True or Reset == True:
                data_np = dist_.copy()
                dist_copy = dist.copy()
                dist_copy = dist_copy.tolist()
                dist_copy.insert(0, datetime.datetime.now() )
                dist_list = []
                dist_list.append(dist_copy)
                
                First_run = False
                Reset = False
            else:
                data_np = np.vstack([data_np, dist_])
                dist_copy = dist.copy()
                dist_copy = dist_copy.tolist()
                dist_copy.insert(0, datetime.datetime.now() )
                dist_list.append(dist_copy)
                
            lock.release()
            
            draw.rectangle([(0,0),(128,128)],fill = "WHITE")
            
            font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size =12)
            
            if x_state == 0:
                x_max = 24
                x_max = len(size_mid)
                x_max_factor = 3
                bar_factor = 1
                x_correction = 0
            if x_state == 1:
                x_max = 18
                x_max_factor = 4 
                bar_factor = 3
                x_correction = 2
            if x_state == 2:
                x_max = 13
                x_max_factor = 6 
                bar_factor = 4
                x_correction = 2
            if x_state == 3:
                x_max = 7
                x_max_factor = 12 
                bar_factor = 8
                x_correction = 4

            
            if x_max == 24:
                draw.text( (x_base-9,(128-y_base+7)),".4", fill = "RED",font=font )
                draw.text( (x_base + (len(dist)-1 )*4-6,(128-y_base+7)),"38", fill = "RED",font=font )
                draw.text( (x_base + 11*4 -2,(128-y_base+7)),"9", fill = "RED",font=font )
                draw.text( (x_base + 18*4 - 5,(128-y_base+7)),"23", fill = "RED",font=font )
                draw.text( (x_base + 3*4 - 5,(128-y_base+7)),"1.2", fill = "RED",font=font )
                
                draw.line([(x_base + (len(dist)-1 )*4,(128-y_base+line_offset_y)+2 ),(x_base + (len(dist)-1 )*4,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
                draw.line([(x_base + 11*4,(128-y_base+line_offset_y)+2 ),(x_base + + 11*4,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
                draw.line([(x_base + 18*4,(128-y_base+line_offset_y)+2 ),(x_base + 18*4,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
                draw.line([(x_base + 3*4,(128-y_base+line_offset_y)+2 ),(x_base + 3*4,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)        
            if x_max == 18:            
                draw.text( (x_base-4,(128-y_base+7)),".4", fill = "RED",font=font )
                draw.text( ((x_max-1)+x_base+(x_max-1)*x_max_factor-4,(128-y_base+7)),"21", fill = "RED",font=font )
                draw.text( ((12)+x_base+(12)*x_max_factor-3,(128-y_base+7)),"11", fill = "RED",font=font )
                draw.text( ((6)+x_base+(6)*x_max_factor-5,(128-y_base+7)),"2.7", fill = "RED",font=font )
                
                draw.line([(x_correction+(x_max-1)+x_base+(x_max-1)*x_max_factor,(128-y_base+line_offset_y)+2 ),(x_correction+(x_max-1)+x_base+(x_max-1)*x_max_factor,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
                draw.line([(x_correction+(12)+x_base+(12)*x_max_factor,(128-y_base+line_offset_y)+2 ),(x_correction+(12)+x_base+(12)*x_max_factor,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
                draw.line([(x_correction+(6)+x_base+(6)*x_max_factor,(128-y_base+line_offset_y)+2 ),(x_correction+(6)+x_base+(6)*x_max_factor,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
            if x_max == 13:            
                draw.text( (x_base-2,(128-y_base+7)),".4", fill = "RED",font=font )
                draw.text( ((x_max-1)+x_base+(x_max-1)*x_max_factor-4,(128-y_base+7)),"11", fill = "RED",font=font )
                draw.text( (x_base+(3)*x_max_factor-2,(128-y_base+7)),"1.2", fill = "RED",font=font )
                draw.text( (3+x_base+(6)*x_max_factor-1,(128-y_base+7)),"2.7", fill = "RED",font=font )
                
                draw.line([(x_correction+(x_max-1)+x_base+(x_max-1)*x_max_factor,(128-y_base+line_offset_y)+2 ),(x_correction+(x_max-1)+x_base+(x_max-1)*x_max_factor,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2) 
                draw.line([(x_correction+(3)+x_base+(3)*x_max_factor,(128-y_base+line_offset_y)+2 ),(x_correction+(3)+x_base+(3)*x_max_factor,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
                draw.line([(x_correction+(6)+x_base+(6)*x_max_factor,(128-y_base+line_offset_y)+2 ),(x_correction+(6)+x_base+(6)*x_max_factor,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
            if x_max == 7:            
                draw.text( (x_base-2,(128-y_base+7)),".4", fill = "RED",font=font )
                draw.text( (x_base+(3)*x_max_factor,(128-y_base+7)),"1.2", fill = "RED",font=font )
                draw.text( (3+x_base+(6)*x_max_factor,(128-y_base+7)),"2.7", fill = "RED",font=font )
                
                draw.line([(x_correction+(x_max-1)+x_base+(x_max-1)*x_max_factor,(128-y_base+line_offset_y)+2 ),(x_correction+(x_max-1)+x_base+(x_max-1)*x_max_factor,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2) 
                draw.line([(x_correction+(3)+x_base+(3)*x_max_factor,(128-y_base+line_offset_y)+2 ),(x_correction+(3)+x_base+(3)*x_max_factor,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
    #         draw.text( (x_base-12,(128-y_base+0)),"0", fill = "RED",font=font )
            draw.text( (x_base-27,y_base-15),str(y_max), fill = "RED",font=font )
            
            draw.line([(x_base-2,(128)-y_base+line_offset_y),(x_base+3*len(dist)+len(dist),(128)-y_base+line_offset_y)], fill = "RED",width = 2)
            draw.line([(x_base-2,((128)-y_base)),(x_base-2,((128)-y_base) - 100)], fill = "RED",width = 2)
    #         tickmarks y
            draw.line([(x_base-2,((128)-y_base- 75)),(x_base-4,((128)-y_base) - 75)], fill = "RED",width = 2)
            draw.line([(x_base-2,((128)-y_base- 50)),(x_base-4,((128)-y_base) - 50)], fill = "RED",width = 2)
            draw.line([(x_base-2,((128)-y_base- 25)),(x_base-4,((128)-y_base) - 25)], fill = "RED",width = 2)
            draw.line([(x_base-2,((128)-y_base- 0)),(x_base-4,((128)-y_base) - 0)], fill = "RED",width = 2)
            draw.line([(x_base-2,((128)-y_base- 100)),(x_base-4,((128)-y_base) - 100)], fill = "RED",width = 2)
    #         tickmarks x


    #         for x in range(len(dist)):

            for x in range(x_max):

                if dist[x] < 100:
                    y_val = dist[x] / (0.01*y_max)
                    draw.line([((x_correction+x+x_base+x*x_max_factor),(128)-y_base),((x_correction+x+x_base)+x*x_max_factor,(128-y_val)-y_base)], fill = "BLUE",width = 1)
                    draw.line([((x_correction+x+x_base+x*x_max_factor+1),(128)-y_base),((x_correction+x+x_base)+x*x_max_factor+1,(128-y_val)-y_base)], fill = "BLUE",width = 1*bar_factor)
                    
            LCD.LCD_ShowImage(image,0,0)
    print('Collect clear')
    operation = False

# LCD_animate(LCD, draw, image, a)







def report_data():
    
    global iterator
    global operation
    global data
    global data_np
    global lock
    global x
    global Reset
    global shutdown
    latch = False
    first = True
    
    while operation == True:
#         print("iterator:",iterator)
        if ( iterator == 10 and latch == False ) or (shutdown == True and latch == False):
            lock.acquire()
            print("mark:",data)
            latch = True
            x = 0
            iterator = 0
            
            
            if first == True:
                with open(path+file,'w') as f:
                    writer = csv.writer(f)
                    writer.writerow( np.array(size_mid) )
                    
                    for z in range(0,data_np.shape[0],1):
                        row = data_np[z]                        
                        writer.writerow(row)
                        
            if first == False:
                with open(path+file,'a') as f:
                    writer = csv.writer(f)
                    for z in range(0,data_np.shape[0],1):
                        row = data_np[z]                        
                        writer.writerow(row)


            Reset = True
            first = False
            if shutdown == True:
                operation = False
            lock.release()
            
        if iterator != 10 and latch == True:
            latch = False
    
    return_data = 0
    print('Report clear')
    return return_data

def report_data_list():
    
    global iterator
    global operation
    global data
    global data_np
    global lock
    global x
    global Reset
    global shutdown
    global dist_list
    latch = False
    first = True
    
    while operation == True:
#         print("iterator:",iterator)
        if ( iterator == 10 and latch == False ) or (shutdown == True and latch == False):
            lock.acquire()
            print("mark:",data)
            latch = True
            x = 0
            iterator = 0
            
            
            if first == True:
                with open(path+file,'w') as f:
                    writer = csv.writer(f)
                    size_mid_copy = size_mid.copy()
                    size_mid_copy.insert(0,0)
                    writer.writerow( size_mid_copy )
                    
                    for z in range(len ( dist_list )):
                        row = dist_list[z]                        
                        writer.writerow(row)
                        
            if first == False:
                with open(path+file,'a') as f:
                    writer = csv.writer(f)
                    for z in range(len ( dist_list )):
                        row = dist_list[z]                        
                        writer.writerow(row)


            Reset = True
            first = False
            if shutdown == True:
                operation = False
            lock.release()
            
        if iterator != 10 and latch == True:
            latch = False
    
    return_data = 0
    print('Report clear')
    return return_data

def timer():
    global operation
    global switch
    
    start_time = datetime.datetime.now()
#     print(start_time)

    while operation == True:
        if( datetime.datetime.now() - start_time ).seconds == 1:
            start_time = datetime.datetime.now()
            switch = True
#             print(start_time)
    
    return 0



# thread_3 = Thread(target=append_data)
thread_3 = Thread(target=timer)
thread_2 = Thread(target=report_data_list)
thread_1 = Thread(target=LCD_animate, args = ( LCD, draw, image, a ) )

thread_1.start()
thread_2.start()
thread_3.start()
# thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

