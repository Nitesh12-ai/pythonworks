from time import * 
import random as r 

def mistake(partest,usertest):
    error = 0 
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1 
        except: 
            error = error + 1 
    return error




def speed_timer(time_s,time_e,userinput):  
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

test = [" Here Nitesh Nitesh want to know that what will you do by only studying", "would you like to answer the main question then hit again:"]
test1 = r.choice(test)
print("!!!!!!!! Typing Speed !!!!!!!!!!")
print(test1)
print() # for spacing 
print() # for spacing
time_1 = time()
testinput = input("Enter the above given para: ")
time_2 = time()

print("Speed: " , speed_timer(time_1,time_2,testinput),"w/sec")
print("Error:", mistake(test1,testinput))
        
    