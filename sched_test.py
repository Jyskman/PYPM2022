import sched
import time
import datetime
s = sched.scheduler(time.time, time.sleep)
import csv

path = "/home/pi/Documents/PYPM2022/testdata/"
file = "test2.csv"

base = []

base.append([1,1,1,1])
base[0].insert(0, datetime.datetime.now() )

base.append([2,2,2,2])
base[1].insert(0, datetime.datetime.now() )

# t =  datetime.datetime.now()
# row[0] = t

with open(path+file,'w') as f:
    writer = csv.writer(f)
    for x in range( len(base) ):
        print(x)
#     row = data_np[z]                        
        writer.writerow( base[x] )



 



# def active(sc):
#     print( datetime.datetime.now())
#     
#     sc.enter(1,1,active,(sc,))
#     
#     
# s.enter(1,1,active, (s,))
# s.run()



# start_time = datetime.datetime.now()
# print(start_time)
# 
# while True:
#     if( datetime.datetime.now() - start_time ).seconds == 1:
#         start_time = datetime.datetime.now()
#         print(start_time)

#             if first == True:
#                 with open(path+file,'w') as f:
#                     writer = csv.writer(f)
#                     writer.writerow( np.array(size_mid) )
#                     
#                     for z in range(0,data_np.shape[0],1):
#                         row = data_np[z]                        
#                         writer.writerow(row)
#                         
#             if first == False:
#                 with open(path+file,'a') as f:
#                     writer = csv.writer(f)
#                     for z in range(0,data_np.shape[0],1):
#                         row = data_np[z]                        
#                         writer.writerow(row)