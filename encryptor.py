import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#decrypted = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,./1234567890 "
#encrypted = b"0896745231`-+=/.,<>?'#~@}{[]zcxbvmnadsgfhjlkpioyurteAZCXBVMNLJIOTY"


decrypted = b"abcdefghijklmnop!qrstuvwxyz1234567_890ABCDEFGHIJKLMNOPQRSTUVWXYZ "
encrypted = b"zcxBVMNlkjhgFASDqewT RUyoIPZCXbvmnLKJHGfas!dQEWtruYOip0793682541_"

encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

result = ''
choice = ''
message = ''

#setting up window and canvas
root = tk.Tk()
root.title("Encryptor")
root.configure(bg= "pale turquoise")
root.resizable(0,0)
root.geometry('400x300')

#importing images
load = Image.open("assets\decrypt_button.png")
load = load.resize((63, 25), Image.ANTIALIAS)
di = ImageTk.PhotoImage(load)

load = Image.open("assets\encrypt_button.png")
load = load.resize((63, 25), Image.ANTIALIAS)
ei = ImageTk.PhotoImage(load)

message = StringVar()
mess = Entry(textvariable = message, width = 60, borderwidth=0)
mess.place(x= 18, y = 50)

def encrypt():
	global res
	result = str(message.get()).translate(encrypt_table)
	res = Label(root, text = result, bg="pale turquoise")
	res.place(x=200, y=150, anchor = 'center')
	print(result)

def decrypt():
	global res
	result = str(message.get()).translate(decrypt_table)
	res = Label(root, text = result, bg="pale turquoise")
	res.place(x=200, y=150, anchor = 'center')
	print(result)

def dellabels():
	global res
	res.destroy()

button = Button(image = ei, command = encrypt, borderwidth=0, bg="pale turquoise", activebackground = "pale turquoise")
button2 = Button(image= di, command = decrypt, borderwidth=0, bg="pale turquoise", activebackground = "pale turquoise")
button.place(x=200, y=85, anchor = 'center')
button2.place(x=200, y=110, anchor = 'center')

delbutton = Button(text = "Clear Last Encryption", command = dellabels, borderwidth=0, bg="pale turquoise", activebackground = "pale turquoise", fg = "red")
delbutton.place(x=200, y=200, anchor = 'center')