import time

print("choose your option")
print("Add New Order entre:-  1 ")
print("Change  Order entre:-  2")
print("Viwe All Orders entre:- 3")
option=int(input("Entre Your Option:- "))



if option ==1:
  name= input("entre your name ")
  order=input("entre your Full Order ")
  date=time.strftime("%d,%m,%y")
  print("\nName:-",name,"\nYour Order:-", order,"\nOrder Date",date)

  with open("order.txt","+a") as f:
     
       f.write("\n\nOrder")
       f.write("\nOrder Date:- ")
       f.write(date)
       f.write("\nName:- ")
       f.write(name)
       f.write("\nOrder:- ")
       f.write(order)
       f.close 
elif option ==3:
    with open("order.txt","r") as s:
        viwe=s.read()
        print(viwe)
