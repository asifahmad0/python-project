from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector

pid = random.randint(1,10)*1234567890 #genrate pationt id random

class hospital:
    def __init__(self, root):
        self.root = root
        self.root.title('Hospital Managemant system')
        self.root.geometry("1540x800+0+0")

        self.dateValue = StringVar()
        self.idValue = StringVar()
        self.comboValue =StringVar()
        self.nameValue =StringVar()
        self.AddressValue=StringVar()
        self.pinValue=StringVar()
        self.mobileValue=StringVar()
        self.dobvalue=StringVar()
        self.BloodValue=StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE,text="HOSPITAL MANAGEMANT SYSTEM", fg="green", bg="white", font=("time now roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #---------------------------Data Frame-------------------------------
        dataFrame= Frame(self.root, bd=20, relief=RIDGE)
        dataFrame.place(x=0,y=130, width=1530, height=400)

        dataFrameLeft = LabelFrame(dataFrame, bd=20, relief=RIDGE, padx=10,font=("time now roman",12,"bold"), text="Patient Information")
        dataFrameLeft.place(x=0,y=5, width=980,height=350 )

        dataFrameRight= LabelFrame(dataFrame, bd=20, relief=RIDGE,padx=10, font=("time now roman",12,"bold"), text="Save information")
        dataFrameRight.place(x=980, y=5, width=510, height=350)
       #-----------------------------------button frame---------------------------
        btnframe = Frame(self.root, bd=15, relief=RIDGE)
        btnframe.place(x=0, y=525, width=1530, height=80)

       #-----------------------------------bottam frame---------------------------
        dataFramebottom = Frame(self.root, bd=20, relief=RIDGE)
        dataFramebottom.place(x=0,y=600, width=1530,height=200)

        #------------------------------------Data Frame Left entry fild---------------
        date = Label(dataFrameLeft, text="Date", fg="red", font=("time new roman", 12, "bold"))
        date.grid(row=0, column=0)
        datelabel = Label(dataFrameLeft, textvariable=self.dateValue, text="Date", font=("times new roman", 12, "bold"), width=10)
        datelabel.grid(row=0,column=1)

        id = Label(dataFrameLeft, text="Pesiont ID", fg="red", font=("time new roman", 12, "bold"))
        id.grid(row=0, column=2)
        idlabel = Label(dataFrameLeft, textvariable=self.idValue, text=pid, font=("times new roman", 12, "bold"), width=10)
        idlabel.grid(row=0,column=3)

        idDepartment = Label(dataFrameLeft, text="Department", fg="red", font=("time new roman", 12, "bold"),padx=2, pady=6)
        idDepartment.grid(row=1, column=0)
        comboLabletab = ttk.Combobox(dataFrameLeft,textvariable=self.comboValue, font=("times new roman", 12, "bold"), width=33)
        comboLabletab["values"]=("Cardiology","Neorology","Aurthology","Corona Vacacine")
        comboLabletab.grid(row=1,column=1)

        name = Label(dataFrameLeft, text="Pesent Name", fg="red", font=("time new roman", 12, "bold"),padx=2, pady=6)
        name.grid(row=1, column=2)
        nametab = Entry(dataFrameLeft,textvariable=self.nameValue,font=("times new roman", 12, "bold"), width=33)
        nametab.grid(row=1,column=3)

        Address = Label(dataFrameLeft, text="Address", fg="red", font=("time new roman", 12, "bold"),padx=2, pady=6)
        Address.grid(row=2, column=0)
        Addresstab = Entry(dataFrameLeft,textvariable=self.AddressValue, font=("times new roman", 12, "bold"), width=33)
        Addresstab.grid(row=2,column=1)


        pin = Label(dataFrameLeft, text="Pin Code", fg="red", font=("time new roman", 12, "bold"),padx=2, pady=6)
        pin.grid(row=2, column=2)
        pintab = Entry(dataFrameLeft, textvariable=self.pinValue, font=("times new roman", 12, "bold"), width=33)
        pintab.grid(row=2,column=3)

        mobile = Label(dataFrameLeft, text="Mobile", fg="red", font=("time new roman", 12, "bold"),padx=2, pady=6)
        mobile.grid(row=3, column=0)
        mobiletab= Entry(dataFrameLeft, textvariable=self.mobileValue, font=("times new roman", 12, "bold"), width=33)
        mobiletab.grid(row=3,column=1)

        dob = Label(dataFrameLeft, text="D.O.B", fg="red", font=("time new roman", 12, "bold"),padx=2, pady=6)
        dob.grid(row=3, column=2)
        dobtab = Entry(dataFrameLeft, textvariable=self.dobvalue,  font=("times new roman", 12, "bold"), width=33)
        dobtab.grid(row=3,column=3)

        Blood = Label(dataFrameLeft, text="Blood Group", fg="red", font=("time new roman", 12, "bold"),padx=2, pady=6)
        Blood.grid(row=4, column=0)
        Bloodtab = Entry(dataFrameLeft,textvariable=self.BloodValue, font=("times new roman", 12, "bold"), width=33)
        Bloodtab.grid(row=4,column=1)

         #------------------------------------right fild---------------
        self.priscription=Text(dataFrameRight, font=("time new roman", 12, "bold"), width=50, height=16, padx=2, pady=6)
        self.priscription.grid(row=0, column=0)

        #------------------------------------Buttoms---------------
        btnPresc = Button(btnframe, text="prescription", font=("arial",12,"bold"),bg="green", fg="white", width=23, height=2, padx=6)
        btnPresc.grid(row=0,column=0)

        btnPrescData = Button(btnframe, text="prescription Data", font=("arial",12,"bold"),bg="green", fg="white", width=23, height=2, padx=6)
        btnPrescData.grid(row=0,column=1)

        btnUpdate = Button(btnframe, text="Update", font=("arial",12,"bold"),bg="green", fg="white", width=23, height=2, padx=6)
        btnUpdate.grid(row=0,column=2)

        btnDelet = Button(btnframe, text="Delete", font=("arial",12,"bold"),bg="green", fg="white", width=23, height=2, padx=6)
        btnDelet.grid(row=0,column=3)

        btnClear = Button(btnframe, text="Clear", font=("arial",12,"bold"),bg="green", fg="white", width=23, height=2, padx=6)
        btnClear.grid(row=0,column=4)

        btnExit = Button(btnframe, text="Exsit", font=("arial",12,"bold"),bg="green", fg="white", width=23, height=2, padx=6)
        btnExit.grid(row=0,column=5)


        #=======================================botom_tabale=======================================
        #=======================================scrolbar===========================================
        scrolBarX = ttk.Scrollbar(dataFramebottom, orient=HORIZONTAL) 
        scrolBarY = ttk.Scrollbar(dataFramebottom, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(dataFramebottom, columns=("datelabel", "idlabel", "comboLabletab","nametab",
                            "Addresstab","pintab","mobiletab","dobtab","Bloodtab"),xscrollcommand=scrolBarX.set, yscrollcommand=scrolBarY.set) 
        scrolBarX.pack(side=BOTTOM, fill=X)
        scrolBarY.pack(side=RIGHT, fill=Y)

        scrolBarX = ttk.Scrollbar(command=self.hospital_table.xview)
        scrolBarY = ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("datelabel", text="Date")
        self.hospital_table.heading("idlabel", text="Pasiont Id")
        self.hospital_table.heading("comboLabletab", text="Department")
        self.hospital_table.heading("nametab", text="Name")
        self.hospital_table.heading("Addresstab", text="Address")
        self.hospital_table.heading("pintab", text="Pin Code")
        self.hospital_table.heading("mobiletab", text="Mobile")
        self.hospital_table.heading("dobtab", text="Date Of Birth")
        self.hospital_table.heading("Bloodtab", text="Blood")

        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("datelabel", width=100)
        self.hospital_table.column("idlabel", width=100)
        self.hospital_table.column("comboLabletab", width=100)
        self.hospital_table.column("nametab", width=100)
        self.hospital_table.column("Addresstab", width=100)
        self.hospital_table.column("pintab", width=100)
        self.hospital_table.column("mobiletab", width=100)
        self.hospital_table.column("dobtab", width=100)
        self.hospital_table.column("Bloodtab", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)


       






root = Tk()
obj= hospital(root)
root.mainloop()