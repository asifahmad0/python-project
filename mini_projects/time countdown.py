#time count downe
"""
import time

def countdown(seco):
    while seco:
        mins, sec =divmod(seco,60)
        timeformat= "{:02d}:{:02d}".format(mins, sec) #00:00:00
        print(timeformat)
        time.sleep(1)
        seco= seco-1
    print("time Up. your systep was crashed")

seconde= int(input("entre your time in sec:- "))
countdown(seconde)
"""

"""
#star patern 

* 
 *  * 
 *  *  * 
 *  *  *  * 
 *  *  *  *  * 

num=int(input("entre youre numbres "))
count=1
for i in range(0,num):
    print(" * "*count)
    count+=1
 """
"""
#star patern 
 *  *  *  *  * 
 *  *  *  * 
 *  *  * 
 *  * 
 *

num=int(input("entre youre numbres "))
count=5
for i in range(0,num):
    print(" * "*count)
    count-=1
 """

#Project-1, how printer works
"""
pages= int(input("Entre how many copys:- "))
idx=1

while idx<= pages:
    print("printing your page ",idx)
    idx+=1
"""