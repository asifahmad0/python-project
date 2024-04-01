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

#for change 
elif option ==2:
    print("\nchoose your option")
    print("Change Name entre:-  1 ")
    print("Change  Order entre:-  2")
    print("quiet entre:-  3")
    optionForchange=int(input("Entre Your Option:- "))
    
    if optionForchange ==1:
        oldName=input("Entre Your Old Name:- ")
        newName=input("Entre Your Old Name:- ")
        with open("order.txt","r") as f:
          data=f.read()
          new_Ndata = data.replace(oldName,newName)
        with open("order.txt","w") as f:
          f.write(new_Ndata)

    elif optionForchange ==2:
        oldOrder=input("Entre Your Old Order:- ")
        newOrder=input("Entre Your Old Order:- ")
        with open("order.txt","r") as f:
          data=f.read()
          new_Odata = data.replace(oldOrder,newOrder)
        with open("order.txt","w") as f:
          f.write(new_Odata)
    elif optionForchange==3:
       quit



# for view all orders
elif option ==3:
    with open("order.txt","r") as s:
        viwe=s.read()
        print(viwe)
