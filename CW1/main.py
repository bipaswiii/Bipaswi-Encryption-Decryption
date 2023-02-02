import tkinter as tk
import tkinter.font as tkfont
from getpass import getpass
import datetime
import base64

root = tk.Tk()
root.title("Ceaser Encryptor-Decryptor")
root.geometry("400x500")
root.resizable(width=False, height=False)

canvas = tk.Canvas(root, height=500, width=400, bg="MediumPurple1")
canvas.pack()

bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

label1 = tk.Label(root, text="Enter the Text", width=20, bg="MediumPurple1", font=bold_font)
canvas.create_window(200, 100, window=label1)

user_text = tk.Entry(root, show="*")
canvas.create_window(200, 150, window=user_text)

label2 = tk.Label(root, text="Choose an Operation", width=25, bg="MediumPurple1", font=bold_font)
canvas.create_window(200, 200, window=label2)

v = tk.IntVar()
def log_event(event):
    with open("log.csv", "a") as f:
        f.write(f"{datetime.datetime.now()},{event}\n")

def choice():
    if not user_text.get():
        error_handler()
    else:
        x = v.get()
        if x == 1:
            encryption()
        elif x == 2:
            decryption()
            
def error_handler():
    error_message = "Input Field Empty"
    label = tk.Label(root, text=error_message, width=20, bg="light yellow", font=bold_font)
    canvas.create_window(200, 350, window=label)
    
def encryption():
    plain_text = user_text.get()
    log_event(f"{plain_text},Encrypted")
    cipher_text = ""
    key = 5
    for i in range(len(plain_text)):
        letter = plain_text[i]
        if letter.isdigit():
            char_code = int(letter)
            cipher_text += str((char_code + key) % 10)
        elif letter.isalpha() or (ord(letter) >= 33 and ord(letter) <= 126):
            char_code = ord(letter)
            if char_code + key > 126:
                cipher_text += chr(char_code + key - 95)
            else:
                cipher_text += chr(char_code + key)
        else:
            cipher_text += letter
    cipher_text = base64.b64encode(cipher_text.encode()).decode()
    label3 = tk.Label(root, text=cipher_text, width=20, bg="light yellow", font=bold_font)
    canvas.create_window(200, 350, window=label3)
    user_text.delete(0, 'end')


    

def decryption():
    cipher_text = user_text.get()
    log_event(f"{cipher_text},Decrypted")
    plain_text = ""
    key = 5
    cipher_text = base64.b64decode(cipher_text.encode()).decode()
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
        char_code = ord(letter)
        if char_code in range(32, 127):
            if char_code - key < 32:
                plain_text += chr(char_code - key + 95)
            else:
                plain_text += chr(char_code - key)
        else:
            plain_text += letter
    label4 = tk.Label(root, text=plain_text, width=20, bg="light yellow", font=bold_font)
    canvas.create_window(200, 350, window=label4)
    user_text.delete(0, 'end')

  

def show_value(value):
    new_window = tk.Toplevel(root)
    new_window.title("Input Value")
    new_window.geometry("200x100")
    label = tk.Label(new_window, text=value, width=20, bg="light yellow", font=bold_font)
    label.pack()




encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=v, value=1, command=choice, bg="MediumPurple1")
canvas.create_window(100, 250, window=encrypt_radio)


decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=v, value=2, command=choice, bg="MediumPurple1")
canvas.create_window(300, 250, window=decrypt_radio)

view_button = tk.Button(root, text="View", bg="light green", command=lambda: show_value(user_text.get()))
canvas.create_window(300, 150, window=view_button)

run_button = tk.Button(root, text="Run", bg="light green", command=choice)
canvas.create_window(200, 300, window=run_button)



...


root.mainloop()

