import tkinter as tk
from tkinter import filedialog,messagebox

def new_file():
    text.delete(1.0,tk.END)

def open_file():
    file_path= filedialog.askopenfilename(defaultextension=".txt", filetypes=[('Text Files', "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.askopenfilename(defaultextension=".tex", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open (file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo('info', 'File Save Sccessfully')

root =tk.Tk()
root.title("Asif Text Editor")
root.geometry("800×600")

menu =tk.Menu(root)
root.config(menu=menu)
file_menu= tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label="new", command=new_file)
file_menu.add_cascade(label="Open", command=open_file)
file_menu.add_cascade(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue")
text.pack(expand=tk.YES,fill=tk.BOTH)

root.mainloop()
