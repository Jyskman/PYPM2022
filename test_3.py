def LCD_animate(LCD, draw, image, a):
    run = 5
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
        
        draw.text( (x_base-9,(128-y_base+7)),".4", fill = "RED",font=font )
        draw.text( (x_base + (len(dist)-1 )*4-6,(128-y_base+7)),"38", fill = "RED",font=font )
        draw.text( (x_base + 11*4 -2,(128-y_base+7)),"9", fill = "RED",font=font )
        draw.text( (x_base + 18*4 - 5,(128-y_base+7)),"23", fill = "RED",font=font )
        draw.text( (x_base + 3*4 - 5,(128-y_base+7)),"1.2", fill = "RED",font=font )
        
#         draw.text( (x_base-12,(128-y_base+0)),"0", fill = "RED",font=font )
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

        draw.line([(x_base + (len(dist)-1 )*4,(128-y_base+line_offset_y)+2 ),(x_base + (len(dist)-1 )*4,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
        draw.line([(x_base + 11*4,(128-y_base+line_offset_y)+2 ),(x_base + + 11*4,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
        draw.line([(x_base + 18*4,(128-y_base+line_offset_y)+2 ),(x_base + 18*4,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)
        draw.line([(x_base + 3*4,(128-y_base+line_offset_y)+2 ),(x_base + 3*4,(128-y_base+line_offset_y)+4)], fill = "RED",width = 2)

        for x in range(len(dist)):
         
            if dist[x] < 100:
                y_val = dist[x] / (0.01*y_max)
                draw.line([((x+x_base+x*3),(128)-y_base),((x+x_base)+x*3,(128-y_val)-y_base)], fill = "BLUE",width = 1)
                draw.line([((x+x_base+x*3+1),(128)-y_base),((x+x_base)+x*3+1,(128-y_val)-y_base)], fill = "BLUE",width = 1)
                
        LCD.LCD_ShowImage(image,0,0)


LCD_animate(LCD, draw, image, a)