from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("500x400")
root.resizable(0, 0)
root.title("PASSWORD GENERATOR")

Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()

pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

pass_str = StringVar()


# function that generates a password
# must contain uppercase and lowercase letters, digits and punctuation
def generator():
    password = ''

    # first 4 characters will be uppercase, lowercase, digit and punctuation
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) \
                   + random.choice(string.digits) + random.choice(string.punctuation)
    # other characters of a password will be random
    for y in range(pass_len.get() - 4):
        password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


Button(root, text="GENERATE PASSWORD", command=generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()


def copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text="COPY TO CLIPBOARD", command=copy_password).pack(pady=5)
root.mainloop()

