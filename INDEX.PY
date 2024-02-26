#a=int(input("enter your first number "))
#b=int(input("enter your second number "))

#c= a>=b
#print option 1 
#print(c)

#print option 2
"""
print(a>=b)
"""
#print option 3
"""
if(a>=b):{
print("True")
}
else:{
    print("False")
}"""
"""
a= "my name is asif ahmad "
print(a[-22:-1]) #INDEXING
print(a[0:22])

A= input("ENTER YOUR NAME ")
print(len(A))
a= "my $ name $ is $ asif $ ahmad $ "
print(a.count("$")) #count function

"""
#if else code..........................................
"""
mark=int(input("enter you marks "))

if(mark>=90):
    if(mark>=101):
       grade ="not a real mark"
    else:   
       grade="A"

elif(mark>=80 and mark<90):
    grade ="B"

elif(mark>=70 and mark<80):
    grade ="c" 
else:
    grade="sorry you are failed"

print(grade)
"""
"""
a= int(input("enter your number: "))
rem= a%2

if(rem == 0):
    ans = "evan"
else:
    ans ="odd"    
print(ans)"""

"""
a= int(input("enter your number: "))
b= int(input("enter your number: "))
c= int(input("enter your number: "))

if(a>b and a>c):
    print("A is greatest number: ", a)
elif(b>a and b>c):
     print("B is greatest number: ", b)    
else:
    print("c is greatest number: ", c)   
print("A: ",a, "B: ",b, "C: ",c )
"""

#list code..........................................

#marks=[32,35,52,45,55,95,12,40] # this is list can modify
#marks=(32,35,52,45,55,95,12,40) # this is tuple can't modify
#print(marks[5]) #for print index 5 marks
#marks.append(57) # for adding 1 more numbre
#print(len(marks)) #lenth of varible 
#print(type(marks)) #type of varible
#marks [5]="85" #change 95 to 
#marks.insert(3,13)# for adding 1 more numbre on given index numbre
#print(marks[5]) # print new marks
#print(marks[0:9]) #for print index all marks
#marks.sort() #to assending to desending
#marks.sort(reverse=True) #to reverse order assending to desending
#print(marks.sort()) #for print to assending to desending
#marks.remove(45)
#marks.pop(3)
"""
marks=[]
m1=input("enter your marks")
m2=input("enter your marks")
m3=input("enter your marks")
marks.append(m1)
marks.append(m2)
marks.append(m3)
print(marks)
"""

"""
get1=["m,a,a,m"]
#get2=["a,p,p,l,e"]
#get3=[1,2,3,2,1]
#get4=[1,2,3,4,5]

copy_get1=get1.copy()
if(copy_get1==get1):
    print("this is palamndrom")
else:
    print("this is not a palamndrom")    
"""
"""
tup=("A,B,C,A,C,D,A,B,A")
Tup =tup.count("A")
print(Tup)"""

#DISCNARY..........................................
"""
info ={
    "name":"asif ahmad",
    "roll":206010220929,
    "subjact":["Scince","math","english","hindi"], #listing on discnery
    "score":{#discnery ke andar disknery caled nesting
        "science":75,
        "math":85,
        "english":55,
        "hindi": 45
    }
}
print(info["score"])# showing error if have error
print(info.get["score"])# showing none value if have error
print(info["score"] ["math"])
print(list(info.keys()))# converting disc into list
print(info.items())#
new_disc = {city:pakur}# add new disc into old disc
info.update(new_disc)
print(info)
#print(info["name"])
#print(type(info["name"]))
#info["name"] = "Anam" #replace name value
#info["surname"]="Ahmad" #ading a new key(surname) and value(Ahmad)
#print(info.keys()) # for print all keys
#keys=info.keys() # for print all keys 
#print(keys)
#print(info.value()) for print all values
print(info) 
"""
# sets..........................................

#info = set()# empaty sets
#info.add("ASIF AHMAD")
#info.add(7)
#info.add(4)
#info.add(4)
#info.add(6)
#info.remove(4)
#info.clear()#for empaty the set
#info.pop()#for remove a randome value
#print(info)

"""
# get score and record in empaty diractory and show 
# mathorde 1
score={ }
marks=input("enter your maraks ")
key1=input("enter your subject ")
marks1=input("enter your maraks ")
key2=input("enter your subject ")
marks2=input("enter your maraks ")

score[key]=marks
score[key1]=marks1
score[key2]=marks2
"""

"""
# mathorde 2
score={ }
p=input("enter your phy score ")
score.update({"physics":p})

m=input("enter your math score ")
score.update({"Math":m})

c=input("enter your chme score ")
score.update({"Chmestry":c})

print(score)
"""
"""
score= set()
x= input("enter your value ")
score.add(x)
print(score)
print(type(score))
"""
#while loop..........................................

# print the table of 3 using while loop
"""
x=3
n=1
while n<=10:
    print("3 * ",n," = ",x*n)
    n=n+1

# printing the number 1 to 100 using while loop
 
x=1
while x<=100:
    print(x)
    x=x+1    
"""  
# printing the number 1 to 100 using while loop
"""
x=100
while x>=1:
    print(x)
    x=x-1      

x= int(input("enter your numbre "))
n=1
while n<=10:
    print(x," *",n," = ",x*n)
    n=n+1
"""
"""
num=[1,4,9,16,25,64,81,100]
idx=0
while idx < len(num):
    print(num[idx])
    idx+=1
"""
"""
num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("entre your search "))
i=0
while i < len(num):
    if(num[i] == x):
        print("found at index ",i)
        break # stope in this code
    else:
        print("finding...")

    i+=1
"""
"""
 #ode numbre print
i =1
while i<= 10:
    if(i%2 == 0):
      i +=1
      continue #skip
    print(i)
    i+=1

    #even numbre print
i =1
while i<= 10:
    if(i%2 != 0):
      i +=1
      continue 
    print(i)
    i+=1    
"""
#for loop ..........................................
"""
l=[1,4,16,25,36,49,64,81,100]
i=int(input("enter the value: "))
idx=0

for v in l:
    if i == v: 
      print("value found: ",v," have on index: ",idx)
      break
    else:
       print("searching...") 
       idx+=1 
"""
#range..............................................
#s=range(5)
#print(range(5))
#print(s[1])
#print(s[2])
#print(s[3])
#print(s[4])
#for i in s #range(10):
 #   print(i)
#for i in range(1,101):#range(start, stop, step)
 #   print(i) 

#for i in range(100,0,-1):#range(start, stop, step)
#   print(i) 
"""
t=int(input("enter your table: "))
idx=1
for i in range(t,t*11,t):#range(start, stop, step)
 print(t,"*",idx," = ",i) 
 idx+=1
"""
#sum of first n numbre
#using  while loop
"""
n= int(input("enter your numbre: "))
sum=0
i = 1
while i<=n:
    sum+=i
    i+=1
    
print("total sum of first",n," numbres is: ",sum)
"""
#using for loof
"""
n= int(input("enter your numbre: "))
sum=0
for i in range(1, n+1):
    sum+=i

print("total sum of first",n," numbres is: ",sum)
"""
"""
n= int(input("enter your numbre: "))
sum=1
for i in range(1, n+1):
    sum*=i

print("total factorial of first",n," numbres is: ",sum)
"""

#range..............................................
"""
def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum


#call the funtion
cal_sum(2,5)

cal_sum(7,5)

cal_sum(8,9)
 """

"""
list=["ironman","spidreman","thor","hulk","eantman"  ]

def add_list(value):
    for x in value:
        print(x, end=", ")
    
add_list(list)
 """

# Money converting App Convert USD Into INR
"""
i=int(input("entre amount: "))
def money(usd):
    inr=usd*83
    print(usd," USD is ",inr," INR")
    return 0

money(i)
"""
# Recursion
"""
def show (n):
    if ( n == 0):
        print("hello ists don ")
        return
    print(n)
    show(n-1)

show(3)
"""
"""
def cal_sum (n):
    if ( n == 0):
        print("hello ists don ")
        return 0
    #print(n)
    return cal_sum(n-1) + n

sum=cal_sum(5)
print(sum)
"""










