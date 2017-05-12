from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tut

def encrypt_file():
    if len(filename.get())==0 and text.get("1.0",END)!="\n":
        inp = tut.encrypt_text(tut.getKey(password.get()),text.get("1.0", END))
        text.delete('1.0', END)
        text.insert(END, inp)
    elif text.get("1.0",END)=="\n" and len(filename.get())!=0:
        tut.encrypt(tut.getKey(password.get()),filename.get())
    elif len(filename.get())==0 and len(text.get("1.0",END))==0:
        messagebox.showerror("Darpher v2.1", "No input for Encryption")
        return 0
    elif len(filename.get())==0 and text.get("1.0",END)=="\n":
        messagebox.showerror("Darpher v2.1", "Multiple inputs for Encryption")
        return 0
    else:
        messagebox.showerror("Darpher v2.1", "Unknown Error occured")
        return 0
    messagebox.showinfo("Darpher v2.1", "File Encrypted Successfully")
    e1.delete(0, END)
    e2.delete(0, END)

def decrypt_file():
    if len(filename.get())==0 and text.get("1.0",END)!="\n":
        inp = tut.decrypt_text(tut.getKey(password.get()),text.get("1.0", END))
        print(inp)
        text.delete('1.0', END)
        text.insert(END, inp)
    elif text.get("1.0",END)=="\n" and len(filename.get())!=0:
        tut.decrypt(tut.getKey(password.get()),filename.get())
    elif len(filename.get())==0 and len(text.get("1.0",END))==0:
        messagebox.showerror("Darpher v2.1", "No input for Decryption")
        return 0
    elif len(filename.get())==0 and text.get("1.0",END)=="\n":
        messagebox.showerror("Darpher v2.1", "Multiple inputs for Decryption")
        return 0
    else:
        messagebox.showerror("Darpher v2.1", "Unknown Error occured")
        return 0
    messagebox.showinfo("Darpher v2.1", "File Decrypted Successfully")
    e1.delete(0, END)
    e2.delete(0, END)

def browse_file():
    y = filedialog.askopenfile(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    e1.insert(END, y.name)

window = Tk()

window.wm_title("Darpher v2.1")

l1=Label(window, text="Filename: ")
l1.grid(row=1, column=1,rowspan=2)

l2=Label(window, text="Password: ")
l2.grid(row=10, column=1)

filename=StringVar()
e1=Entry(window, textvariable=filename)
e1.grid(row=1, column=3)

password=StringVar()
e2=Entry(window, textvariable=password)
e2.grid(row=10, column=3)

text = Text(window, height=4, width=40, pady=2,font=('Lucida Console', 8))
text.grid(row=4, column=1, columnspan=4)

b1=Button(window, text="Encrypt", command=encrypt_file)
b1.grid(row=10,column=4, columnspan=2)

b2=Button(window, text="Decrypt", command=decrypt_file)
b2.grid(row=11, column=4, columnspan=2)

b3 = Button(window, text="Browse File", command=browse_file)
b3.grid(row=1, column=4, columnspan=2)

l3=Label(window, text="WELCOME TO DARPHER v2.1")
l3.grid(row=12, column=2, columnspan=2)

l4=Label(window, text="Message")
l4.grid(row=3, column=1)

window.mainloop()
