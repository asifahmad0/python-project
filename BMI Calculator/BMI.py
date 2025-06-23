from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#contaner
bgcls = "#cfd1da"
BotomBoxColor = "lightblue"
bgcls2="white"
cls="#008000"


root = Tk()
root.geometry('480x600+300+200')
root.resizable(False,False)
root.title('BMI Calculator')
root.configure(bg=bgcls)

def BMI():
    h=float(Height.get())
    w=float(Weight.get())

    #convert into mitter and bmi
    mitter= h/100
    bmiValue=round(float(w/mitter**2))
    bmi = bmiValue
    bmiText=""


    if bmiValue < 18.5:
        bmiText = "You Are under Weight \n Week Body "
    elif bmiValue>15.5 and bmiValue < 25:
        bmiText = "You Are Normal \n Healthy Body "
    elif bmiValue>25 and bmiValue <30:
        bmiText = "BMI Indicale that a persion is \n slightly overweight! \n A doctor may advise to lose weight"
    else:
        bmiText = "Obes ! \n Health may be at risk, if they do not \n lose weight! "


    Label(root, bg=BotomBoxColor, text=bmiText,font="arial 15 bold").place(x=130, y=400)
    Label(root, bg=BotomBoxColor, text=bmi,font="arial 60 bold", fg=bgcls2).place(x=280, y=500)



#icons
img_icon = PhotoImage(file="images/icon.png")
root.iconphoto(False, img_icon)

#top

top = PhotoImage(file="images/top.png")
top_img = Label(root, image=top, background=bgcls)
top_img.place(x=-10, y=-10)

#two Box
box = PhotoImage(file="images/box.png")
Label(root,image=box,).place(x=20,y=100)
Label(root,image=box,).place(x=240,y=100)

#bottom box
Label(root, width=72, height=18, bg=BotomBoxColor).pack(side=BOTTOM)

#scale
Scale = PhotoImage(file="images/scale.png")
Label(root, image=Scale, bg=BotomBoxColor).place(x=20, y=330)

#-----------------------------------Height Slider---------------

current_value = tk.DoubleVar()

def GetCurrentValue():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(GetCurrentValue())

    size = int(float(GetCurrentValue()))
    img = (Image.open("images/man.png"))
    resize_img = img.resize((50,30+size))
    man_img = ImageTk.PhotoImage(resize_img)
    man_img_lable.config(image=man_img)
    man_img_lable.place(x=70, y=550-size)
    man_img_lable.image=man_img
    


slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed, variable=current_value)
slider.place(x=80, y=250)
style = ttk.Style()
style.configure("TScale", background=bgcls2)


#--------------------------------Weight Slider---------------------------

weight_current_value = tk.DoubleVar()

def get_weight_current_value():
    return '{: .2f}'.format(weight_current_value.get())

def weight_slider_changed(event):
    Weight.set(get_weight_current_value())


slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=weight_slider_changed, variable=weight_current_value)
slider.place(x=300, y=250)
style = ttk.Style()
style.configure("TScale", background=bgcls2)




#-------------------------------Entry Box 
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font='arial 50', bg='#fff', fg='#000', bd =0, justify=CENTER)
height.place(x=35, y=160)
Height.set(GetCurrentValue())

weight = Entry(root, textvariable=Weight,  width=5, font='arial 50', bg='#fff', fg='#000', bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_weight_current_value())



#man image
man_img_lable =Label(root, bg=bgcls)
man_img_lable.place(x=70, y=530)



Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg=bgcls2, command=BMI).place(x=300, y=340)





















root.mainloop()