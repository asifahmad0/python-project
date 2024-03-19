
#-------------------------------------------------Project-1, how printer works-----------------------------------
"""
pages= int(input("Entre how many copys:- "))
idx=1

while idx<= pages:
    print("printing your page ",idx)
    idx+=1
"""
#------------------------------------------------------------Calandre----------------------------------------
# entre year and enter month and get your calendare 
"""
import calendar
yy=int(input("Entre year "))
mm=int(input("entre month "))
print(calendar.month(yy,mm))
"""

#---------------------------------------------time count downe---------------------------------------
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


#---------------------------------------------------------star patern ---------------------------------------------
"""
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

#--------------------------------------------------------star patern--------------------------------------------------
"""
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
#-------------------------------------------------qr code genrator-------------------------------------------------
"""
import qrcode
url=input("entre your link:-")
img=qrcode.make(url)
img.save("qrcode.png")
"""

#-------------------------simple 2 numbre calculatr----------------------------------------------------------------------

"""
num1= int(input("entre your first numbre "))
num2 = int(input("entre your second numbre "))
print("Entre Opton \nAdditional-1 \nMinuse-2 \nMultiply-3 \nDevide-4")
sym= input("enter your Option ")


if (sym == "1"):
    sum = num1 + num2
    print(sum)

elif (sym == "2"):
    sum = num1 - num2
    print(sum)

elif (sym == "3"):
    sum = num1 * num2
    print(sum)

elif (sym == "4"):
    sum = num1 / num2
    print(sum)
else:
    print("Your Entred Invalid Option")
"""
# A system look time And greating you good morning, good afternoon, good evening, good night------------------------------------
"""
import time
i= time.strftime("%H")
print(i)

if(i>="1" and i<"12" ):
    print(" Good Morning")

elif(i>="12" and i<="15" ):
    print(" Good After Noon")

elif(i>"15" and i<="19" ):
    print(" Good Evening")

elif(i>"19" and i<="23" ):
    print(" Good Night")
"""
