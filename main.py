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
        for F in (opening, login, signup, mainmenu, settings, game):
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
        self.controller = controller

        # configuring the frame

        self.configure(background="#333333")

        # icon inside opening screen

        self.icon_text = tk.Label(self, text='21', font=("Secular One", 200),
                                  bg="#333333", fg="#FFFFFF")
        self.icon_text.pack(pady=20)

        # log in button

        self.login_btn = tk.PhotoImage(file='assets/buttons/login.png')
        ttk.login = tk.Button(self, image=self.login_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=lambda: controller.show_frame("login"))
        ttk.login.pack()

        # sign up button

        self.signup_btn = tk.PhotoImage(file='assets/buttons/signup.png')
        ttk.signup = tk.Button(self, image=self.signup_btn, bg="#333333", activebackground="#333333",
                               borderwidth=0, command=lambda: controller.show_frame("signup"))
        ttk.signup.pack(pady=10)

        # quit button

        self.quit_btn = tk.PhotoImage(file='assets/buttons/quit.png')
        ttk.quitb = tk.Button(self, image=self.quit_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=quit)
        ttk.quitb.pack()


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

        def on_entry_click_username(event):
            if username_entry.cget('fg') == 'grey':
                # delete all the text in the entry
                username_entry.delete(0, "end")
                username_entry.insert(0, '')
                username_entry.config(fg='black')

        def on_focusout_username(event):
            if username_entry.get() == '':
                username_entry.insert(0, 'Username')
                username_entry.config(fg='grey')

        username_entry = Entry(
            self, width=17, bg="#D9D9D9", font=("Secular One", 28))
        username_entry.insert(0, 'Username')
        username_entry.bind('<FocusIn>', on_entry_click_username)
        username_entry.bind('<FocusOut>', on_focusout_username)
        username_entry.config(fg='grey')
        username_entry.pack()

        def on_entry_click_password(event):
            password_entry.config(show='*')
            if password_entry.cget('fg') == 'grey':
                password_entry.delete(0, "end")
                password_entry.insert(0, '')
                password_entry.config(fg='black')

        def on_focusout_password(event):
            if password_entry.get() == '':
                password_entry.insert(0, 'Password')
                password_entry.config(fg='grey', show='')

        password_entry = Entry(
            self, width=17, bg="#D9D9D9", font=("Secular One", 28))
        password_entry.insert(0, 'Password')
        password_entry.bind('<FocusIn>', on_entry_click_password)
        password_entry.bind('<FocusOut>', on_focusout_password)
        password_entry.config(fg='grey')
        password_entry.pack(pady=10)

        # user authentication

        incorrect = Label(self, text='', font=("Secular One", 20),
                          bg="#333333", fg="red")

        def log_in():
            if username_entry.get() != "Username":
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
            else:
                incorrect.config(text='No Input')
                incorrect.pack(pady=20)

        # enter button

        self.enter_btn = tk.PhotoImage(file='assets/buttons/enter.png')
        ttk.enter = tk.Button(self, image=self.enter_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=log_in).pack()

        # back button

        self.back_btn = tk.PhotoImage(file='assets/buttons/back.png')
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

        def on_entry_click_username(event):
            if username_entry.cget('fg') == 'grey':
                username_entry.delete(0, "end")
                username_entry.insert(0, '')
                username_entry.config(fg='black')

        def on_focusout_username(event):
            if username_entry.get() == '':
                username_entry.insert(0, 'Username')
                username_entry.config(fg='grey')

        username_entry = Entry(
            self, width=17, bg="#D9D9D9", font=("Secular One", 28))
        username_entry.insert(0, 'Username')
        username_entry.bind('<FocusIn>', on_entry_click_username)
        username_entry.bind('<FocusOut>', on_focusout_username)
        username_entry.config(fg='grey')
        username_entry.pack()

        def on_entry_click_password(event):
            password_entry.config(show='*')
            if password_entry.cget('fg') == 'grey':
                # delete all the text in the entry
                password_entry.delete(0, "end")
                password_entry.insert(0, '')
                password_entry.config(fg='black')

        def on_focusout_password(event):
            if password_entry.get() == '':
                password_entry.insert(0, 'Password')
                password_entry.config(fg='grey', show='')

        password_entry = Entry(
            self, width=17, bg="#D9D9D9", font=("Secular One", 28))
        password_entry.insert(0, 'Password')
        password_entry.bind('<FocusIn>', on_entry_click_password)
        password_entry.bind('<FocusOut>', on_focusout_password)
        password_entry.config(fg='grey')
        password_entry.pack(pady=10)

        # user auth

        incorrect = Label(self, text='', font=("Secular One", 20),
                          bg="#333333", fg="red")

        def sign_up():
            if username_entry.get() != "Username":
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
            else:
                incorrect.config(text='No Input')
                incorrect.pack(pady=20)

        # submit button

        self.submit_btn = tk.PhotoImage(file='assets/buttons/submit.png')
        ttk.enter = tk.Button(self, image=self.submit_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=sign_up)
        ttk.enter.pack()

        # back button

        self.back_btn = tk.PhotoImage(file='assets/buttons/back.png')
        ttk.back = tk.Button(self, image=self.back_btn, bg="#333333", activebackground="#333333",
                             borderwidth=0, command=lambda: controller.show_frame("opening"))
        ttk.back.pack(anchor="w", side="bottom")


class mainmenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame

        self.configure(background="#333333")

        # invisible label

        ilabel = tk.Label(self, text="", bg="#333333")
        ilabel.pack(side="top", fill="x", pady=200)

        # play button

        self.play_btn = tk.PhotoImage(file='assets/buttons/play.png')
        ttk.play = tk.Button(self, image=self.play_btn, bg="#333333", activebackground="#333333",
                             borderwidth=0, command=lambda: controller.show_frame("game"))
        ttk.play.pack()

        # settings button

        self.settings_btn = tk.PhotoImage(file='assets/buttons/settings.png')
        ttk.settings = tk.Button(self, image=self.settings_btn, bg="#333333", activebackground="#333333",
                                 borderwidth=0, command=lambda: controller.show_frame("settings"))
        ttk.settings.pack(pady=10)

        # quit button

        self.quit_btn = tk.PhotoImage(file='assets/buttons/quit2.png')
        ttk.quitb = tk.Button(self, image=self.quit_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=quit)
        ttk.quitb.pack()


class settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame

        self.configure(background="#333333")

        # maybe use global variables to tell the game what settings a user has used
        # if they have solo they are alone
        # if they have chosen hard they use more decks
        # if they choose easy its just one deck
        # if they choose multi then there could be 7 players?


class game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame

        self.configure(background="#35654d")
        self.configure(pady=20)

        # dealer frame

        dealer_frame = tk.LabelFrame(self, text='Dealer', bd=0, bg='#FFFFFF')
        dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

        # cards in dealer frame

        dealer_label = ttk.Label(dealer_frame, text='')
        dealer_label.pack(pady=20)

        # player frame

        player_frame = LabelFrame(self, text='Player', bd=0, bg='#FFFFFF')
        player_frame.grid(row=0, column=1, ipadx=20)

        # cards in player frame

        player_label = ttk.Label(player_frame, text='')
        player_label.pack(pady=20)


class blank(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame

        self.configure(background="#333333")


if __name__ == "__main__":

    # configuring the app

    app = App()
    app.title('BlackJack Card Game NEA')
    app.iconbitmap('assets/icon.ico')
    app.geometry("900x500")
    app.state('zoomed')
    app.configure(background="#333333")

    # open the main app

    app.mainloop()
