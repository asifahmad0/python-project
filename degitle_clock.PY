from time import strftime
import tkinter as tk

root = tk.Tk()
root.title("Degitle Clock ")

def time ():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

label =tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='red')
label.pack(anchor='center')

time()

root.mainloop()