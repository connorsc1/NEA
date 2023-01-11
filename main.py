from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from login import *

# create the window

root = Tk()
root.title('BlackJack Card Game NEA')
root.iconbitmap('assets/icon.ico')

# open window in full screen

root.geometry("900x500")
root.state('zoomed')

root.configure(background="#333333")

# opening screen

opening = Frame(root, bg="#333333").pack(pady=20)

# icon inside opening screen

icon_text = Label(opening, text='21', font=("Secular One", 200),
                  bg="#333333", fg="#FFFFFF").pack(pady=20)

# user authentication


def login():
    print("User pressed login button")
    # change to new frame
    # take inputs and call login function from other file login(username, password)


def signup():
    print("User pressed sign up button")

# log in button


login_btn = PhotoImage(file='assets/login.png')
login = Button(opening, image=login_btn, bg="#333333", activebackground="#333333",
               borderwidth=0, command=login).pack()

# sign up button

signup_btn = PhotoImage(file='assets/signup.png')
signup = Button(opening, image=signup_btn, bg="#333333", activebackground="#333333",
                borderwidth=0, command=signup).pack(pady=10)

# quit button

quit_btn = PhotoImage(file='assets/quit.png')
quitb = Button(opening, image=quit_btn, bg="#333333", activebackground="#333333",
               borderwidth=0, command=quit).pack()

root.mainloop()
