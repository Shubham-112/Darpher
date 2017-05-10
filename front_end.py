from tkinter import *
import tut

def encrypt_file():
    tut.encrypt(tut.getKey(password.get()),filename.get())
    l3.text = "Successfully Encrypted"
    e1.delete(0, END)
    e2.delete(0, END)


def decrypt_file():
    filename_str=str(filename.get())
    tut.decrypt(tut.getKey(password.get()),filename_str)
    l3.text= "Successfulle Decrypted"
    e1.delete(0, END)
    e2.delete(0, END)

window = Tk()

window.wm_title("Darpher v1.3")

l1=Label(window, text="Filename: ")
l1.grid(row=1, column=1,rowspan=2)

l2=Label(window, text="Password: ")
l2.grid(row=3, column=1)

filename=StringVar()
e1=Entry(window, textvariable=filename)
e1.grid(row=1, column=3)

password=StringVar()
e2=Entry(window, textvariable=password)
e2.grid(row=3, column=3)

b1=Button(window, text="Encrypt", command=encrypt_file)
b1.grid(row=1,column=6)

b2=Button(window, text="Decrypt", command=decrypt_file)
b2.grid(row=3, column=6)

l3=Label(window, text="WELCOME TO DARPHER v1.3")
l3.grid(row=5, column=2, columnspan=2)

window.mainloop()
