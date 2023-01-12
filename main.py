# importint necessary libraries

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
import json

# main app


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = Font(family='Secular One')

        # creating the container

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # adding navigation

        self.frames = {}
        for F in (opening, login, signup, mainmenu):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("opening")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class opening(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#333333")
        self.controller = controller

        # icon inside opening screen

        self.icon_text = tk.Label(self, text='21', font=("Secular One", 200),
                                  bg="#333333", fg="#FFFFFF").pack(pady=20)

        # log in button

        self.login_btn = tk.PhotoImage(file='assets/login.png')
        ttk.login = tk.Button(self, image=self.login_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=lambda: controller.show_frame("login")).pack()

        # sign up button

        self.signup_btn = tk.PhotoImage(file='assets/signup.png')
        ttk.signup = tk.Button(self, image=self.signup_btn, bg="#333333", activebackground="#333333",
                               borderwidth=0, command=lambda: controller.show_frame("signup")).pack(pady=10)

        # quit button

        self.quit_btn = tk.PhotoImage(file='assets/quit.png')
        ttk.quitb = tk.Button(self, image=self.quit_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=quit).pack()


class login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame

        self.configure(background="#333333")

        # invisible label

        ilabel = tk.Label(self, text="", bg="#333333")
        ilabel.pack(side="top", fill="x", pady=120)

        login_text = Label(self, text='Log in', font=("Secular One", 50),
                           bg="#333333", fg="#FFFFFF")
        login_text.pack(pady=20)

        # input fields

        u = StringVar(self, value='Username')
        username_entry = Entry(self, width=17, bg="#D9D9D9",
                               font=("Secular One", 28), textvariable=u)
        username_entry.pack()

        p = StringVar(self, value='Password')
        password_entry = Entry(self, width=17, bg="#D9D9D9",
                               font=("Secular One", 28), textvariable=p)
        password_entry.pack(pady=10)

        # user authentication

        incorrect = Label(self, text='', font=("Secular One", 20),
                          bg="#333333", fg="red")

        def log_in():
            with open("info.txt") as f:
                data = f.read()
            info = json.loads(data)
            usern = username_entry.get()
            passw = password_entry.get()
            incorrect.config(text='')
            if usern.lower() in info and info[usern.lower()] == passw:
                # make it go to the main menu
                controller.show_frame("mainmenu")
            else:
                incorrect.config(text='Incorrect, try again')
                incorrect.pack(pady=20)

        # enter button

        self.enter_btn = tk.PhotoImage(file='assets/enter.png')
        ttk.enter = tk.Button(self, image=self.enter_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=log_in).pack()

        # back button

        self.back_btn = tk.PhotoImage(file='assets/back.png')
        ttk.back = tk.Button(self, image=self.back_btn, bg="#333333", activebackground="#333333",
                             borderwidth=0, command=lambda: controller.show_frame("opening"))
        ttk.back.pack(anchor="w", side="bottom")


class signup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame

        self.configure(background="#333333")

        # invisible label

        ilabel = tk.Label(self, text="", bg="#333333")
        ilabel.pack(side="top", fill="x", pady=120)

        signup_text = Label(self, text='Sign up', font=("Secular One", 50),
                            bg="#333333", fg="#FFFFFF")
        signup_text.pack(pady=20)

        # input fields

        u = StringVar(self, value='Username')
        username_entry = Entry(self, width=17, bg="#D9D9D9",
                               font=("Secular One", 28), textvariable=u)
        username_entry.pack()

        p = StringVar(self, value='Password')
        password_entry = Entry(self, width=17, bg="#D9D9D9",
                               font=("Secular One", 28), textvariable=p)
        password_entry.pack(pady=10)

        # user auth

        incorrect = Label(self, text='', font=("Secular One", 20),
                          bg="#333333", fg="red")

        def sign_up():
            with open("info.txt") as f:
                data = f.read()
            info = json.loads(data)
            usern = username_entry.get()
            passw = password_entry.get()
            incorrect.config(text='')
            if usern.lower() in info:
                incorrect.config(text='Username is taken, try again')
                incorrect.pack(pady=20)
            else:
                f = open("info.txt", "r+")
                lines = f.readlines()
                f.seek(0)
                f.truncate()
                f.writelines(lines[:-1])
                f.write(f',"{usern.lower()}" : "{passw}"\n')
                f.write("}")
                controller.show_frame("login")

        # submit button

        self.submit_btn = tk.PhotoImage(file='assets/submit.png')
        ttk.enter = tk.Button(self, image=self.submit_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=sign_up)
        ttk.enter.pack()

        # back button

        self.back_btn = tk.PhotoImage(file='assets/back.png')
        ttk.back = tk.Button(self, image=self.back_btn, bg="#333333", activebackground="#333333",
                             borderwidth=0, command=lambda: controller.show_frame("opening"))
        ttk.back.pack(anchor="w", side="bottom")


class mainmenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame

        self.configure(background="#333333")


if __name__ == "__main__":

    # open the main app

    app = App()
    app.title('BlackJack Card Game NEA')
    app.iconbitmap('assets/icon.ico')

    # configuring the app

    app.geometry("900x500")
    app.state('zoomed')
    app.configure(background="#333333")

    app.mainloop()
