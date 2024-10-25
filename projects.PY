
#-------------------------------------------------Project-1, how printer works-----------------------------------
"""
pages= int(input("Entre how many copys:- "))
idx=1

while idx<= pages:
    print("printing your page ",idx)
    idx+=1
"""
#------------------------------------------------------------project-2 Calandre----------------------------------------
# entre year and enter month and get your calendare 
"""
import calendar
yy=int(input("Entre year "))
mm=int(input("entre month "))
print(calendar.month(yy,mm))
"""

#---------------------------------------------project-3 time count downe---------------------------------------
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
#-------------------------------------------------project-4 qr code genrator-------------------------------------------------
"""
import qrcode
url=input("entre your link:-")
img=qrcode.make(url)
img.save("qrcode.png")
"""

#-------------------------project-5 simple 2 numbre calculatr----------------------------------------------------------------------

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
# ----------------project-6 A system look time And greating you good morning, good afternoon, good evening, good night
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
#swape 2 varibles
"""
x=int(input("entre your numbre"))
y=int(input("entre your numbre"))

z=x-y
x=x-z

print(x,y)

#second methord
x=5
y=2

x,y=x+y,y+x
print(x,y)

#change value togeder
x=5
y=2

x,y=y,x
print(x,y)

# chacke nubre positive, nagative or zero

x=int(input("entre your numbre "))

if x>0:
    print(" this numbre is positiv +",x)
elif x<0:
    print(" this numbre is Nagetiv",x)
else:
    print(" this numbre is ",x)

# numbre is odd or even
x=int(input("entre your numbre "))

if x%2==0:
    print(" this numbre is even",x)
else:
    print(" this numbre is odd ",x)

# leep year or not 

x=int(input("entre your year "))

if x%4==0 and x%100 !=0:
    print(' it is a leep year')

else:
    print("it is not a leep year ")
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
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
num=int(input("entre youre numbres "))

for i in range(num+1):
    for j in range(i):
        print(i, end=" ")
    print()
"""
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
num=int(input("entre youre numbres "))

for i in range(num+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
"""
"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

num=int(input("entre youre numbres "))
count=5
for i in range(num+1):
    
    for j in range(1,count+1):
        print(j, end=" ")  
    print()
    count-=1
"""

"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

num=int(input("entre youre numbres "))
count=1
for i in range(num+1):
    for j in range(1,i+1):
        print(count, end=" ")
        count+=1
    print()
"""

"""import keyword
key=keyword.kwlist
x= str(key)
with open('keyword.txt','w') as f:
    f.write(x)
"""

#=========================================================Hotel Manu Project============================================
"""

print("Welcome To Ahmad Resturant")

menu = {
    "Pizza":40,
    "Pasta":50,
    "Burger":60,
    "Momo":70,
    "Coffee":80,
}
#------------print Manu----------
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nMomo: Rs70\nCoffee: Rs80\n")

#------------------Order Total----------------
Total_Order=0

#------------------Get Order----------------
item= input("please Enter Your Order ")

if item in menu:
    Total_Order += menu[item]
    print("Your Order ", item ," Is Added in Your Order")
else:
    print("Order Item Not Found Please Order Again ")


#------------------Get Second Order----------------
getMor = input("Do You Want Anything more (Y/N ) ")

if getMor =="y" or getMor == "Y":

    item_2= input("please Enter Your Order ")

    if item_2 in menu:
        Total_Order += menu[item_2]
        print("Your Order ",item_2, " Is Added in Your Order")
        print("Please Wait Your Order Is Comming Soon\n", "You Have To Pay Rs ", Total_Order)
    else:
        print("Order Item Not Found Please Order Again ")


else:
    print("Please Wait Your Order Is Comming Soon\n", "You Have To Pay ", Total_Order)

"""

