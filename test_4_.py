from threading import Thread
import threading

import datetime
import numpy as np
import time
import csv
import os
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
pause = False
from google.cloud import storage

path = "/media/pi/GAME DEV/Data/"
# path = "/home/pi/Documents/PYPM2022/testdata/"
file = "Start_"
test = 0

def GCS():
    client = storage.Client.from_service_account_json('/home/pi/Documents/key.json')

    # buck = client.list_buckets()
    name = 'aerosol'
    bucket = client.bucket(name)

    dagens = datetime.datetime.now().strftime('%Y-%m-%d')
    folder = 'Data' + '/' + dagens
    path = '/media/pi/GAME DEV/Data/'

    local = [f for f in os.listdir(path) if os.path.isfile( os.path.join(path,f) ) ]

    remote = [ blob.name for blob in bucket.list_blobs(prefix = folder ) ]
    remote_base = { os.path.basename( blob_name) for blob_name in remote  }


    diff = set(local) - set(remote_base)


    for file in diff:
        
        blob = bucket.blob( folder + '/' + file )
        blob.upload_from_filename(path+file)
# end GCS


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
    global pause
    global first
    
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
#                     latch = True
                    pause = True
#                     draw.text( (64,(64)),"PAUSE", fill = "RED",font=font )
#                     LCD.LCD_ShowImage(image,0,0)
    #                 y_max = 10
#                     y_state = y_state - 1
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

                    
                if GPIO.input(KEY2_PIN) == 1 & latch == False:
                    first = True
                    iterator = 10
                    draw.text( (64,(64)),"NEW FILE", fill = "RED",font=font )
                    LCD.LCD_ShowImage(image,0,0)
                    time.sleep(1)
                    

            y_max = y_range[y_state]
            dist = p.OPC_return_dist(a)
            dist_ = np.array(dist)
            
            lock.acquire()
            if First_run == True or Reset == True:
                data_np = dist_.copy()
                dist_copy = dist.copy()
                dist_copy = dist_copy.tolist()
                dist_copy.insert(0, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') )
#                 append pm
                pm_values = p.returnPM(a)
                pm_values_list = pm_values.tolist()
                dist_copy.append(-1)
                dist_copy.extend(pm_values_list)
                
                dist_list = []
                dist_list.append(dist_copy)
                
                First_run = False
                Reset = False
            else:
                data_np = np.vstack([data_np, dist_])
                dist_copy = dist.copy()
                dist_copy = dist_copy.tolist()
                dist_copy.insert(0, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') )
#                 append pm
                pm_values = p.returnPM(a)
                pm_values_list = pm_values.tolist()
                dist_copy.append(-1)
                dist_copy.extend(pm_values_list)

                dist_list.append(dist_copy)
                
            lock.release()
            
            draw.rectangle([(0,0),(128,128)],fill = "WHITE")
            
            font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size =12)
            font_2 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size =10)
            
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
            pm2_5 = '{:.1f}'.format(pm_values[1])
            pm10 = '{:.1f}'.format(pm_values[2])
            
            draw.text( (35,(25)),'PM2.5: ' + pm2_5 + ' ug/m3', fill = "RED",font=font_2 )
            draw.text( (35,(35)),'PM10: ' + pm10 + ' ug/m3', fill = "RED",font=font_2 )
            if pause == True:
                draw.rectangle([(0,0),(128,128)],fill = "WHITE")
                draw.text( (64,(64)),"PAUSE", fill = "RED",font=font )
                draw.text( (80,(25)),"GCS ->", fill = "RED",font=font )

            LCD.LCD_ShowImage(image,0,0)
    print('Collect clear')
    operation = False

# LCD_animate(LCD, draw, image, a)






# old
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
    global pause
    latch = False
    global first
    first = True
    
    while operation == True:
#         print("iterator:",iterator)
        if ( iterator == 10 and latch == False ) or (shutdown == True and latch == False):
            lock.acquire()
            dist_list_c = dist_list.copy()
            print("mark:",data)
            lock.release()
            latch = True
            x = 0
            iterator = 0
            
            
            if first == True:
                name_append = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
                with open(path+file+ name_append +'.csv','w') as f:
                    writer = csv.writer(f)
                    size_mid_copy = size_mid.copy()
                    size_mid_copy.insert(0,0)
#                     appending pm
                    size_mid_copy.append(-1)
                    size_mid_copy.append(1)
                    size_mid_copy.append(2.5)
                    size_mid_copy.append(10)
                    
                    writer.writerow( size_mid_copy )
                    
                    for z in range(len ( dist_list_c )):
                        row = dist_list_c[z]                        
                        writer.writerow(row)
                        
            if first == False:
                with open(path+file+ name_append+'.csv','a') as f:
                    writer = csv.writer(f)
                    for z in range(len ( dist_list_c )):
                        row = dist_list_c[z]                        
                        writer.writerow(row)


            Reset = True
            first = False
            if shutdown == True:
                operation = False
#             lock.release()
            
        if iterator != 10 and latch == True:
            latch = False
    
    return_data = 0
    print('Report clear')
    return return_data

def timer():
    global operation
    global switch
    global pause
    
    start_time = datetime.datetime.now()
#     print(start_time)

    while operation == True:
        
        if pause == True and GPIO.input(KEY3_PIN) == 0:
            pause = False
            time.sleep(0.5)
        if pause == True and GPIO.input(KEY1_PIN) == 0:
            
            print('start GCS')
            GCS()
#             exec(open('/home/pi/Documents/gcs_upload.py').read())
            print('Complete GCS')
            pause = False
            time.sleep(0.5)
            start_time = datetime.datetime.now()

        if( datetime.datetime.now() - start_time ).seconds == 1:
            start_time = datetime.datetime.now()
            if pause == False:
                switch = True
            


        
#             print(start_time)
    
    return 0

def shutdown():
    global operation
    
    if operation == False:
        
        os.system('shutdown now -h')
    
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

