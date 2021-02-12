import tkinter as tk
from tkinter import *

#decrypted = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,./1234567890 "
#encrypted = b"0896745231`-+=/.,<>?'#~@}{[]zcxbvmnadsgfhjlkpioyurteAZCXBVMNLJIOTY"

decrypted = b"abcdefghijklmnopqrstuvwxyz "
encrypted = b"zcxbvmnlkjhgfasdqewtruyoip "

encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

result = ''
choice = ''
message = ''

#setting up window and canvas
root = tk.Tk()
root.title("Encryptor")
root.configure(bg= "pale turquoise")

frame = Frame(root)
root.geometry('600x300')

message = StringVar()
mess = Entry(textvariable = message)
mess.grid(column = 2, row = 2)

def encrypt():

    result = str(message.get()).translate(encrypt_table)
    res = Label(root, text = result, bg="pale turquoise")
    print(message)
    res.grid(row = 3, column = 1)

def decrypt():

    result = str(message.get()).translate(decrypt_table)
    res = Label(root, text = result, bg="pale turquoise")
    res.grid(row = 3, column = 2)

button = Button(text="Encrypt", command = encrypt)
button2 = Button(text="Decrypt", command = decrypt)
button.grid(row = 1, column = 1)
button2.grid(row = 1, column = 2)

