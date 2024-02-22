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

#a= "my name is asif ahmad "
#print(a[-22:-1]) #INDEXING
#print(a[0:22])

#A= input("ENTER YOUR NAME ")
#print(len(A))
#a= "my $ name $ is $ asif $ ahmad $ "
#print(a.count("$")) #count function

"""mark=int(input("enter you marks "))

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
#list

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

#DISCNARY

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
#print(info["name"])
#print(type(info["name"]))
#info["name"] = "Anam" #replace name value
#info["surname"]="Ahmad" #ading a new key(surname) and value(Ahmad)
#print(info.keys()) # for print all keys
#keys=info.keys() # for print all keys 
#print(keys)
#print(info.value()) for print all values
#print(info) 
#print(info["score"])# showing error if have error
#print(info.get("score"))# showing none value if have error
#print(info["score"] ["math"])
#print(info.keys())# converting disc into list
#print(info.keys("score" ))
#print(info.items())#
#new_disc = {"city":"pakur"}# add new disc into old disc
#info.update(new_disc)
#print(info)

"""

"""info = {
   "table":["a piece of furniture ", "list of fact and figures"]
  }

print(info.items())

set={"python","c","c++","java","python","javascript","java","c","c++","java"}
print(type(len(set)))

"""

"""
x=1
while x<=100:
    print(x)
    x+=1

x=100
while x>=1:
    print(x)
    x=x-1

x=3
n=1
while n<=10:
    print("3* ",n," = ",x*n)
    n+=1
"""

